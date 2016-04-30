import pickle
from collections import defaultdict
from functools import partial
import codecs

tagset = {'start', 'B', 'I', 'O'}
A = defaultdict(partial(defaultdict, int))
B = defaultdict(partial(defaultdict, int))
input_dict = defaultdict(partial(defaultdict, int))
input_dict['start']['count'] = 0
input_dict['start']['end'] = 0
prev_tag = 'start'
word_freq = defaultdict(int)

with open('Finput_NER.txt', 'r', encoding="utf8") as train_file:
    for sentence in train_file.read().splitlines():
            if prev_tag != 'start':
                input_dict[prev_tag]['end'] += 1
            prev_tag = 'start'
            input_dict['start']['count'] += 1
        
            for word in sentence[1:-1].split():
                if word == codecs.BOM_UTF8.decode("utf8"):
                    word = word.lstrip(codecs.BOM_UTF8.decode("utf8"))
                # print(word)
                tag = word[-1:]
                # print(tag)
                tagset.add(tag)
                token = word[:-2]
                # print(token)
                word_freq[token] += 1

                input_dict[tag]['count'] += 1
                input_dict[tag][prev_tag] += 1
                input_dict[tag][token] += 1

                prev_tag = tag
    input_dict[prev_tag]['end'] += 1

for tag in tagset:
    if tag != 'start':
        for prev_tag in tagset:
            # A[prev_tag][tag] = (input_dict[tag][prev_tag] + 1) / (input_dict[prev_tag]['count'] - input_dict[prev_tag]['end'] + len(tagset) - 1)
            A[prev_tag][tag] = input_dict[tag][prev_tag] / (input_dict[prev_tag]['count'] - input_dict[prev_tag]['end'])
        for token in input_dict[tag]:
            if token not in tagset and token != 'end' and token != 'count':
                B[token][tag] = input_dict[tag][token] / word_freq[token]

with open('Fmodel.txt', 'wb') as model:
    pickle.dump([A,B,tagset], model)

with open('Fmodel1.txt', 'w', encoding="utf8") as model:
        model.write(str(A))
        model.write(str(B))
