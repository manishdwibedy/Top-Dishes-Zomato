total_tags = 0
correct_tags = 0

with open('Ftest_NER_tagged.txt', 'r', encoding="utf8") as input_file, open('Foutput_NER.txt', 'r', encoding="utf8") as output:
    for sentence1, sentence2 in zip(input_file.read().splitlines(), output.read().splitlines()):
        for word1, word2 in zip(sentence1[1:-1].split(), sentence2[1:-1].split()):
            if word1[-1:] == word2[-1:]:
                correct_tags += 1
            total_tags += 1

print(str(correct_tags/total_tags))