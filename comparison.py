import collections

def main():

    # dataOpen = open('fileName.txt','r') # change name of file
    with open('fileName.txt') as dataOpen:
        words = sorted(dataOpen)

    words.sort()
    
    with open('woah.txt') as openMe:
        werd = sorted(openMe)

    werd.sort()
    compare(words,werd)
        
    # words = dataOpen.split(",")
    # words.sort()
    # print(words)
    
    # databaseOG = dataOpen.readlines()
    for line in words:
        word = line.rsplit(",")
        print(" ".join(word))

def compare(s,t):
    return collections.Counter(s) == collections.Counter(t)

if __name__ == '__main__':
    main()
