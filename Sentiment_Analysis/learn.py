from collections import defaultdict
import pickle

f_pos=open('positive.txt',encoding='utf8')
f_neg=open('negative.txt',encoding='utf8')
f_neu=open('neutral.txt',encoding='utf8')

unique_words=[]
count_pos=0
dict_pos=defaultdict(lambda :0)
for line in f_pos:
    line=line.rstrip()
    items=line.split(' ')

    for item in items:
        dict_pos[item]+=1
        count_pos+=1
        if item not in unique_words:
            unique_words.append(item)

print(count_pos)
print(dict_pos)


count_neg=0
dict_neg=defaultdict(lambda :0)
for line in f_neg:
    line=line.rstrip()
    items=line.split(' ')

    for item in items:
        dict_neg[item]+=1
        count_neg+=1
        if item not in unique_words:
            unique_words.append(item)

# print(count_neg)
# print(dict_neg)

count_neu=0
dict_neu=defaultdict(lambda :0)
for line in f_neu:
    line=line.rstrip()
    items=line.split(' ')

    for item in items:
        dict_neu[item]+=1
        count_neu+=1
        if item not in unique_words:
            unique_words.append(item)

# print(count_neu)
# print(dict_neu)
# print(unique_words)
count=count_pos+count_neg+count_neu
pos_prior=count_pos/count
neg_prior=count_neg/count
neu_prior=count_neu/count


dic_prior={'pos_prior':pos_prior,'neg_prior':neg_prior,'neu_prior':neu_prior}
print(dic_prior)

# print(pos_prior)
# print(neg_prior)
# print(neu_prior)


for item in unique_words:
    if item not in dict_pos:
        dict_pos[item]=1/(count_pos+len(unique_words))
    else:
        dict_pos[item]+=1
        dict_pos[item]/=(count_pos+len(unique_words))

print(dict_pos)
dict_pos=dict(dict_pos)
count=0
for item in dict_pos:
    count+=dict_pos[item]
print(count)
print(dict_pos)


for item in unique_words:
    if item not in dict_neg:
        dict_neg[item]=1/(count_neg+len(unique_words))
    else:
        dict_neg[item]+=1
        dict_neg[item]/=(count_neg+len(unique_words))

print(dict_neg)
dict_neg=dict(dict_neg)
count=0
for item in dict_neg:
    count+=dict_neg[item]
print(count)

for item in unique_words:
    if item not in dict_neu:
        dict_neu[item]=1/(count_neu+len(unique_words))
    else:
        dict_neu[item]+=1
        dict_neu[item]/=(count_neu+len(unique_words))

print(dict_neu)
dict_neu=dict(dict_neu)
count=0
for item in dict_neu:
    count+=dict_neu[item]
print(count)

dic_prob={'dict_pos':dict_pos,'dict_neg':dict_neg,'dict_neu':dict_neu}
print(dic_prob)

model_dic={'dic_prior':dic_prior,'dic_prob':dic_prob}

with open('nbmodel.txt', 'wb') as handle:
  pickle.dump(model_dic, handle)


