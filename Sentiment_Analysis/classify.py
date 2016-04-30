import pickle
import math
import csv

test=[]
with open('NB_actual_snippets.txt',encoding='utf8') as f:
    reader = csv.reader(f,delimiter='\t')
    for line in reader:
        test.append([line[0]])
print(test)



synonyms_list=['बेहतर','उत्तमतर','बढ़कर','बीस','उत्तर','श्रेष्ठतर','सरस']

with open('nbmodel.txt', 'rb') as handle:
  model_dic = pickle.loads(handle.read())

dic_prior=model_dic['dic_prior']
dict_pos=model_dic['dic_prob']['dict_pos']
dict_neg=model_dic['dic_prob']['dict_neg']
dict_neu=model_dic['dic_prob']['dict_neu']

a=[]

for item in test:
    if dic_prior['pos_prior']!=0:
        sum_pos=math.log(dic_prior['pos_prior'])
    else:
        sum_pos=0
        for items in item:
            if items in dict_pos:
                sum_pos+=math.log(dict_pos[items])
        else:
            if items in synonyms_list:
                for i in synonyms_list:
                    if i in dict_pos:
                        sum_pos+=math.log(dict_pos[i])



    if dic_prior['neg_prior']!=0:
        sum_neg=math.log(dic_prior['neg_prior'])
    else:
        sum_neg=0
        for items in item:
            if items in dict_neg:
                sum_neg+=math.log(dict_neg[items])


    if dic_prior['neu_prior']!=0:
        sum_neu=math.log(dic_prior['neu_prior'])
    else:
        sum_neu=0
        for items in item:
            if items in dict_neu:
                sum_neu+=math.log(dict_neu[items])


    sum=[sum_pos,sum_neg,sum_neu]
    if max(sum)==sum_pos:
        b=[]
        for i in item:
            b.append(i)
        b.append('Nice')
        a.append(b)
        #print(item,' Positive')
    elif max(sum)==sum_neg:
        b=[]
        for i in item:
            b.append(i)
        b.append('Bad')
        a.append(b)
        #print(item,' Negative')
    else:
        b=[]
        for i in item:
            b.append(i)
        b.append('So-so')
        a.append(b)
        #print(item,' Neutral')
print(a)
with open('nbmodel_eval.txt', 'wb') as handle:
  pickle.dump(a, handle)