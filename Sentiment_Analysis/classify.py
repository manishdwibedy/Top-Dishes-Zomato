import pickle
import math

#test=[['chocolate'],['strawberry','shake']]

test=[['बढ़कर'],['एक','एक']]
synonyms_list=['बेहतर','उत्तमतर','बढ़कर','बीस','उत्तर','श्रेष्ठतर','सरस']
# for item in synonyms_list:
#     print(item)

with open('nbmodel.txt', 'rb') as handle:
  model_dic = pickle.loads(handle.read())

dic_prior=model_dic['dic_prior']
dict_pos=model_dic['dic_prob']['dict_pos']
dict_neg=model_dic['dic_prob']['dict_neg']
dict_neu=model_dic['dic_prob']['dict_neu']

# print(dic_prior)
# print(dict_pos)
# print(dict_neg)
# print(dict_pos)

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
        print(item,' Positive')
    elif max(sum)==sum_neg:
        print(item,' Negative')
    else:
        print(item,' Neutral')