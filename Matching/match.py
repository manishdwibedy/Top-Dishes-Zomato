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

def fuzzyMatch(reviewFoodItem, menuItem):
    possibleMatches=[]
    for item in menuItem:
        if numWordsMatch(reviewFoodItem,item):
            possibleMatches.append(item)
    return '' . join(possibleMatches)


def numWordsExactMatches(mention, item):
    words = mention.split(" ")
    words_menuItem=item.split(" ")
    numMatches = 0
    for i in words:
        for item in words_menuItem:
            if i==item:
                numMatches =numMatches+1
    return numMatches

def numWordsMatch(mentionWords, itemWords):
    distance ={}
    for i in xrange(-1, len(mentionWords) + 1):
        distance[(i, -1)] = i + 1
    for j in xrange(-1, len(itemWords) + 1):
        distance[(-1, j)] = j + 1
    for i in xrange(len(mentionWords)):
        for j in xrange(len(itemWords)):
            if mentionWords[i] == itemWords[j]:
                cost = 0
            else:
                cost = 1
            distance[(i, j)] = min(
                                distance[(i - 1, j)] + 1,
                                distance[(i, j - 1)] + 1,
                                distance[(i - 1, j - 1)] + cost,
                            )
            if i and j and mentionWords[i] == itemWords[j - 1] and mentionWords[i - 1] == itemWords[j]:
                distance[(i, j)] = min(distance[(i, j)], distance[i - 2, j - 2] + cost)
    distance = distance[len(mentionWords) - 1, len(itemWords) - 1]
    if distance < 0.5 * len(mentionWords):
        return True
    else:
        return False



reviewFoodItem="Chicken Tikka Masala"
menuItem=['Butter Chicken','Chicken Tikka Masala', 'Tikka Chicken Masala', 'Chicken Tika Masala', 'Chicken Tikka Tandori','Paneer Tikka Masala','Mango Lassi','Tandori','Tikka']
partialMatch(reviewFoodItem,menuItem)
exactMatch(reviewFoodItem,menuItem)


print fuzzyMatch("chicken tipa", ["Chicken Tikka", "Panner Tikka"])

