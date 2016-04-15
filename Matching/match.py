
import math
def partialmatch(reviewFoodItem, menuItem):
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

reviewFoodItem="Chicken Tikka Masala"
menuItem=['Butter Chicken', 'Chicken Tikka Tandori','Paneer Tikka Masala','Mango Lassi','Tandori','Tikka']
partialmatch(reviewFoodItem,menuItem)