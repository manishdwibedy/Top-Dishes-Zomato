#Before this I have to get 2 files-snippets and food items and then match sentiment with the snippet and
#remove the food item from the snippet then that file with the snippet and sentiment is passed to this

import csv

a=[]
with open('NB_training_snippets.txt',encoding='utf8') as f:
    reader = csv.reader(f,delimiter='\t')
    for line in reader:
        a.append([line[0],line[1]])
        print(line[0],' ',line[1])
#print(a)

f_pos=open('positive.txt','w',encoding='utf8')# in final file it will be a instead of w
f_neg=open('negative.txt','w',encoding='utf8')
f_neu=open('neutral.txt','w',encoding='utf8')

#a=[['chocolate shake','So-so'],['peri peri chicken pizza','Nice'],['crusty pizza','Nice'],['peri shake','Bad'],['strawberry shake','Bad']]
for item in a:
    if item[1]=='Nice':
        f_pos.write(item[0]+'\n')
    elif item[1]=='Bad':
        f_neg.write(item[0]+'\n')
    else:
        f_neu.write(item[0]+'\n')





