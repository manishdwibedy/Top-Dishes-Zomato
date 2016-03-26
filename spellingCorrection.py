from textblob import TextBlob

def correctSpelling(text):
    wiki = TextBlob(text)

    return wiki.correct()

if __name__ == "__main__":
    print correctSpelling("refilling")