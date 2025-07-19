import os

def AlphabeticSorter(wordList, word):
    alphabeth = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    for i in range(0, len(wordList)):
        j = 0
        while j in range(0, min(len(word), len(wordList[i]))):
            if word[i] not in alphabeth:
                j = j + 1
            elif (alphabeth.index(word[j]) + 1) % (len(alphabeth)/2) == (alphabeth.index(wordList[i][j]) + 1) % (len(alphabeth)/2):
                if j == len(word) - 1:
                    wordList.insert(i, word)
                    return wordList
                j = j + 1
            elif (alphabeth.index(word[j]) + 1) % (len(alphabeth)/2) > (alphabeth.index(wordList[i][j]) + 1) % (len(alphabeth)/2):
                if i == len(wordList) - 1:
                    wordList.append(word)
                    return wordList
                break
            elif (alphabeth.index(word[j]) + 1) % (len(alphabeth)/2) < (alphabeth.index(wordList[i][j]) + 1) % (len(alphabeth)/2):
                wordList.insert(i, word)
                return wordList


newWord = input("Add the word: ")
directory = "MyGithubPythonProjects/Dictionary/Words.txt"
print("Looking for:", os.path.abspath(directory))
with open(directory, "r+" ,encoding="utf8") as t:
    content = t.read()
    wordsList = content.split("\n")
    print(wordsList)
    newlist = AlphabeticSorter(wordsList, newWord)
    print(newlist)
    t.seek(0)
    t.write("\n".join(newlist))