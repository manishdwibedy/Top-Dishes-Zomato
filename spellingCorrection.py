from textblob import TextBlob

def correctSpelling(text):
    '''
    Correcting the spelling of the words
    :param text: the input text
    :return: corrected the spelling in the words
    '''
    textBlob = TextBlob(text)

    return textBlob.correct()

if __name__ == "__main__":
    print correctSpelling("refilling")