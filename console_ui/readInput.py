import sys, locale

def readInput():
    text = raw_input().decode(sys.stdin.encoding or locale.getpreferredencoding(True))
    return text.split(' ')

if __name__ == '__main__':
    words = readInput()
    print words