import sys, locale

def readInput():
    text = raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True))
    return text.split(' ')

def getMatchingText(input):
    reviews = []
    for review in reviews:
        food_mentions = []
        for index, menu in enumerate(review.menu_items):
            food_mention = {
                'menu_item': menu,
                'sentiment': review.sentiment[index]
            }
            food_mentions.append(food_mention)
            pass

if __name__ == '__main__':
    words = readInput()
    print words