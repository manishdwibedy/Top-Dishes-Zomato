import pickle
from collections import defaultdict
from functools import partial

with open('Fmodel.txt', 'rb') as model:
    a, b, tagset = pickle.load(model)

with open('Ftest_NER.txt', 'r', encoding="utf8") as input_file, open('Foutput_NER.txt', 'w', encoding="utf8") as output:
    for sentence in input_file.read().splitlines():
        #print(sentence)
        p = defaultdict(partial(defaultdict, int))
        bp = defaultdict(partial(defaultdict, str))
        t = -1
        o = sentence[1:-1].split()
        path = [''] * len(o)

        for word in o:
         #   print(word)
            t += 1
            found = False
        #    print(found)

            for q in tagset:
                if q != 'start' and b[word][q] != 0:
                    found = True
         #           print(found)

                    if t != 0:
                        prob = 0
                        for qprime in tagset:
                            if qprime != 'start' and p[qprime][t-1] != 0:
                                if a[qprime][q] != 0:
                                    curr = p[qprime][t-1] * a[qprime][q] * b[word][q]
                                    if prob <= curr:
                                        prob = curr
                                        bp[q][t] = qprime
                                else:
                                    found = False
                        p[q][t] = prob

                    else:
                        qprime = 'start'
                        p[q][t] = a[qprime][q] * b[word][q]
                        bp[q][t] = qprime
          #      print(bp[q][t])
           #     print(p[q][t])
                    
            if found is False and t != 0:
                for q in tagset:
                    if (q != 'start'):
                        prob = 0
                        for qprime in tagset:
                            if qprime != 'start' and p[qprime][t - 1] != 0:
                                curr = p[qprime][t - 1] * a[qprime][q]
                                if prob <= curr:
                                    prob = curr
                                    bp[q][t] = qprime
                        p[q][t] = prob
            #    print('Not found:' + bp[q][t])
             #   print(p[q][t])

            elif found is False and t == 0:
                    qprime = 'start'

                    for q in tagset:
                        if q != 'start':
                            p[q][t] = a[qprime][q]
                            bp[q][t] = qprime

        maxp = 0
        for q in tagset:
            if maxp < p[q][t]:
                maxp = p[q][t]
                path[t] = q

        for n in range(t-1, -1, -1):
            path[n] = bp[path[n+1]][n+1]

        #print(path)

        for n in range(0, t+1):
            output.write(o[n] + '/' + str(path[n]) + ' ')
        output.write('\n')