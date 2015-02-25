import sys
import os.path as op
import collections

def unicount(sent):
    res = dict()
    for word in sent:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res

def bicount(sent):
    res = dict()
    if len(sent) <= 1:
        return res

    for i in xrange(len(sent)-1):
        bigram = sent[i] + " " + sent[i+1]
        if bigram in res:
            res[bigram] += 1
        else:
            res[bigram] = 1

    return res

def bleu_for_n_ref(ref_list, evl):
    unicorrect = 0
    bicorrect = 0
    
    evl = evl.lower().split()
    N = len(evl)

    if N == 0:
        return None

    ref_dicts = []
    all_ref_dict_uni = collections.defaultdict(lambda:0)
    all_ref_dict_bi = collections.defaultdict(lambda:0)

    min_ref_len = float("+inf")
    for ref in ref_list:
        ref = ref.lower().split()

        N_ref = len(ref)
        if N_ref == 0:
            pass

        if N_ref < min_ref_len:
            min_ref_len = N_ref

        ref_unicount = unicount(ref)
        eval_unicount = unicount(evl)
        ref_bicount = bicount(ref)
        eval_bicount = bicount(evl)

        for word in ref_unicount:
            all_ref_dict_uni[word] += 1
        for word in ref_bicount:
            all_ref_dict_bi[word] += 1

    for unigram in eval_unicount:
        if unigram in all_ref_dict_uni:
            unicorrect += min(eval_unicount[unigram], all_ref_dict_uni[unigram])

    for bigram in eval_bicount:
        if bigram in all_ref_dict_bi:
            bicorrect += min(eval_bicount[bigram], all_ref_dict_bi[bigram])

    brievity = min(1.0, N * 1.0 / min_ref_len)
    uniprec = 1.0 * unicorrect / N
    if N > 1:
        biprec = 1.0 * bicorrect / (N-1)
    else:
        biprec = 1.0
        
    return 100.0 * brievity * uniprec, 100.0 * brievity * uniprec * biprec

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage: %s reference_file your_output_file" % (__file__)
        sys.exit(0)

    ref_filename = sys.argv[1]
    eval_filename = sys.argv[2]

    if not op.exists(ref_filename):
        print "Reference file '%s' does not exist." % (ref_filename)
        sys.exit(0)

    if not op.exists(eval_filename):
        print "Output file '%s' does not exist." % (eval_filename)
        sys.exit(0)

    with open(ref_filename) as f_ref:
        with open(eval_filename) as f_eval:
            n_sent = 0
            bleu1 = 0.0
            bleu2 = 0.0

            list_of_translations = []
            three_translations = []
            for ref_line in f_ref:
                if "*" in ref_line:
                    list_of_translations.append(three_translations)
                    three_translations = []
                
                elif "*" not in ref_line:
                    ref_line = ref_line.replace("\n", "")
                    three_translations.append(ref_line)
                

            for i in xrange(len(list_of_translations)):
                eval_line = f_eval.readline()
                # list_of_originals.append(eval_line)
                if len(eval_line) == 0:
                    print "Error: The output file should at least have the same number of sentences as the reference file."
                    sys.exit(0)

                t1, t2 = bleu_for_n_ref(list_of_translations[i], eval_line)
                if t1 is not None:
                    bleu1 += t1
                    bleu2 += t2
                    n_sent += 1

                print "%d sentences evaluated.\n" \
                % (n_sent)
                print "Evaluation Sentence: " + eval_line
                print "Reference Sentences:"
                for translation in list_of_translations[i]:
                    print translation
                print
                print "BLEU-1 score: %3.6f\nBLEU-2 score: %3.6f" \
                % (bleu1 / n_sent, bleu2 / n_sent)
                print
