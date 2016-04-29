import csv



with open('Synonym.txt',encoding='utf8') as f:
    reader = csv.reader(f,delimiter='\t')
    for line in reader:
        for item in line:
            item=item.split(',')
            for i in item:
                print(i.strip())