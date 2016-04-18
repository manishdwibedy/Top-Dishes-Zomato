import pickle
import math

test=[['chocolate'],['strawberry','shake']]

test=[['बेहतर'],['एक','एक']]


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
        for items in item:
            if items in dict_pos:
                sum_pos+=math.log(dict_pos[items])
    else:
        sum_pos=0

    if dic_prior['neg_prior']!=0:
        sum_neg=math.log(dic_prior['neg_prior'])
        for items in item:
            if items in dict_neg:
                sum_neg+=math.log(dict_neg[items])
    else:
        sum_neg=0

    if dic_prior['neu_prior']!=0:
        sum_neu=math.log(dic_prior['neu_prior'])
        for items in item:
            if items in dict_neu:
                sum_neu+=math.log(dict_neu[items])
    else:
        sum_neu=0

    sum=[sum_pos,sum_neg,sum_neu]
    if max(sum)==sum_pos:
        print(item,' Positive')
    elif max(sum)==sum_neg:
        print(item,' Negative')
    else:
        print(item,' Neutral')