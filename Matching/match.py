# from fuzzywuzzy import fuzz
# from Levenshtein import *
import math

def exactMatch(reviewFoodItem, menuItem):
    """
    Extracting exact matches from the list of menu items
    :param reviewFoodItem: the food item
    :param menuItem: the list of menu items
    :return: the list of exact matches
    """

    # Couning the number of words in the review food item
    length = len(reviewFoodItem.split(" "))

    # Collecting the possible matches
    possibleMatches = []

    # Loop over every menu item
    for item in menuItem:
        # If all the words in the menu item matched
        if numWordsExactMatches(reviewFoodItem, item) == length:
            # Add to the list of possible matches
            possibleMatches.append(item)
    # Returning the list of exact matches
    return possibleMatches

def partialMatch(reviewFoodItem, menuItem):
    length=len(reviewFoodItem.split(" "))

    possibleMatches=[]
    for item in menuItem:
        if numWordsExactMatches(reviewFoodItem,item) >= math.ceil(float(length) / 2):
            possibleMatches.append(item)
    return possibleMatches

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
#
#
#
#
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

reviewFoodItem="Chicken Tikka Masala"
menuItem=['Butter Chicken','Chicken Tikka Masala', 'Tikka Chicken Masala', 'Chicken Tika Masala', 'Chicken Tikka Tandori','Paneer Tikka Masala','Mango Lassi','Tandori','Tikka']
partialMatch(reviewFoodItem,menuItem)
exactMatch(reviewFoodItem,menuItem)
# # fuzz.ratio("this is a test", "this is a test!")
# print Levenshtein.distance("this is a test", "this is a test!")