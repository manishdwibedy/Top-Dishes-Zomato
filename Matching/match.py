# from fuzzywuzzy import fuzz
# from Levenshtein import *
def exactMatch(reviewFoodItem, menuItem):
    length = len(reviewFoodItem.split(" "))

    possibleMatches = []
    for item in menuItem:

        if numWordsExactMatches(reviewFoodItem, item) == length:
            possibleMatches.append(item)
    print possibleMatches
def partialMatch(reviewFoodItem, menuItem):
    length=len(reviewFoodItem.split(" "))

    possibleMatches=[]
    for item in menuItem:

        if numWordsExactMatches(reviewFoodItem,item) >= length / 2:
            possibleMatches.append(item)
    print possibleMatches

def numWordsExactMatches(mention, item):
    words = mention.split(" ")
    words_menuItem=item.split(" ")
    numMatches = 0
    for i in words:
        for item in words_menuItem:
            if i==item:
                numMatches =numMatches+1
    return numMatches

# def numWordsMatch(mention, item):
#     mentionWords = mention.split(" ")
#     itemWords = item.split(" ")
#     numMatches = 0
#     for i in len(mentionWords):
#         for j in len(itemWords):
#             if len(itemWords[j].strip) < 1:
#                 continue

# def damerau_levenshtein_distance(string1, string2):
#     distance = {}
#     lenstr1 = len(string1)
#     lenstr2 = len(string2)
#     for i in xrange(-1, lenstr1 + 1):
#         distance[(i, -1)] = i + 1
#     for j in xrange(-1, lenstr2 + 1):
#         distance[(-1, j)] = j + 1
#
#     for i in xrange(lenstr1):
#         for j in xrange(lenstr2):
#             if string1[i] == string2[j]:
#                 cost = 0
#             else:
#                 cost = 1
#             distance[(i, j)] = min(
#                             distance[(i - 1, j)] + 1,  # deletion
#                             distance[(i, j - 1)] + 1,  # insertion
#                             distance[(i - 1, j - 1)] + cost,  # substitution
#                         )
#             if i and j and string1[i] == string2[j - 1] and string1[i - 1] == string2[j]:
#                 distance[(i, j)] = min(distance[(i, j)], distance[i - 2, j - 2] + cost)  # transposition
#
#
#
#
#     return distance[lenstr1 - 1, lenstr2 - 1]














# public static int numWordsMatch(Mention m, MenuItem item) {
#     String[] mentionWords = clean(m.mentionText).split(" ");
#     String[] itemWords = clean(item.name + " " + item.description).split(" ");
#
#     DamerauLevenshtein d;
#     int numMatches = 0;
#     for (int i = 0; i < mentionWords.length; i++) {
#       for (int j = 0; j < itemWords.length; j++) {
#         if (trim(itemWords[j]).length() < 1) continue;
#
#         try {
#           d = new DamerauLevenshtein(mentionWords[i], itemWords[j]);
#           if (d.getDHSimilarity() <= DAMERAU_LEVENSHTEIN_MAX) {
#             numMatches++;
#             break;
#           }
#         } catch (Exception e) { }
#       }
#     }
#     return numMatches;

# reviewFoodItem="Chicken Tikka Masala"
# menuItem=['Butter Chicken','Chicken Tikka Masala', 'Tikka Chicken Masala', 'Chicken Tika Masala', 'Chicken Tikka Tandori','Paneer Tikka Masala','Mango Lassi','Tandori','Tikka']
# partialMatch(reviewFoodItem,menuItem)
# exactMatch(reviewFoodItem,menuItem)
# # fuzz.ratio("this is a test", "this is a test!")
print damerau_levenshtein_distance("this is a test", "Dhruv")