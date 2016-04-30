import pickle

import csv

with open('nbmodel_eval.txt', 'rb') as handle:
  model_list = pickle.loads(handle.read())
a=[]
with open('NB_actual_snippets.txt',encoding='utf8') as f:
    reader = csv.reader(f,delimiter='\t')
    for line in reader:
        a.append([line[0],line[1]])
        #print(line[0],' ',line[1])
print(a)

labels=['Nice','Bad','So-so']
f1=0
for label in labels:
    count_tp=0
    count_fn=0
    count_fp=0
    count_tn=0

    for i in range(len(model_list)):
        if model_list[i][-1]==label and model_list[i][-1]==a[i][-1]:
            count_tp+=1
        elif model_list[i][-1]==label and model_list[i][-1]!=a[i][-1]:
            count_fp+=1
        elif model_list[i][-1]!=label and model_list[i][-1]==a[i][-1]:
            count_tn+=1
        else:
            count_fn+=1


    if not(count_tp==0 and count_fp==0):
        precision=(count_tp)/(count_tp+count_fp)
    else:
        precision=0
    if not(count_tp==0 and count_fn==0):
        recall=(count_tp)/(count_tp+count_fn)
    else:
        recall=0

    if not(precision==0 and recall==0):
        f1+=(2*precision*recall)/(precision+recall)
    else:
        f1+=0

f1=f1/3
print(f1)

