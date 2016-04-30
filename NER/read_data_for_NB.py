import json
import csv
from collections import defaultdict
from functools import partial

def read_dependency_parser_output(filename):
    with open(filename, encoding='utf8') as dep_file:
        reader = csv.reader(dep_file, delimiter = '\t')
        d = list(reader)
        return d

def write_training_snippets(d, NE, sentiments, menu_items, id, filename):

    with open(filename, 'a', encoding='utf8') as output:
        i=0
        dep = []
        while(i < len(d)):
            if d[i] != []:
                dep.append(d[i])
            i += 1
            # else:
        for line in dep:
                    # print(dep)
                 #  if line[1] in NE:
                 #      # print(line[1])
                 #     #sub = line
                 #      while(line[4] != '0'):
                 #          output.write(line[1] + ' ')
                 #          line = dep[int(line[4]) - 1]
                 #      output.write(line[1] + '\n')

                if line[5] == 'nmod__adj':
                    str = ''
                    indexNE = int(line[4])-1
                    for index, item in enumerate(NE):
                        if dep[indexNE][1] in item:
                            if line[1] not in item:
                                str = str + line[1]
                            for sub in dep:
                                if sub[5] != 'nmod__adj' and ((int(sub[4])-1) == indexNE or line[0] == sub[4]) and sub[1] not in item:
                                    str = str + ' ' + sub[1]
                            output.write("{}\t{}\t{}\t{}\t{}\n".format(str, sentiments[index], item, menu_items[index], id))
                # dep = []


with open('Finput.js', 'r', encoding="utf8") as review_input:
    reviews = json.load(review_input)

# data = defaultdict(partial(defaultdict,list))

j=1
for review in reviews:
    with open('dependency' + str(j) + '.input.txt', 'w', encoding='utf8') as dep_input:

        id = review["id"]
        menu_items = review["menu_item"]
        sentiments = review["sentiment"]
        food_items = review["food_item"]
        review_text = review["hindi"]
        dep_input.write(review_text[0])
        # Call parser here
        dep_result_file = 'dependency' + str(j) + '.output.txt'
        parser_result = read_dependency_parser_output(dep_result_file)
        write_training_snippets(parser_result, food_items, sentiments, menu_items, id, 'NB_training_snippets.txt')
    j += 1