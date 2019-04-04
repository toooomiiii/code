def CheckNbyN(wordArray):
    return True

def IsSameWordArray(array1, array2):
    if len(array1) != len(array2):
        return False
    isSame = True
    for (word1, word2) in zip(array1, array2):
        isSame = isSame and word1 == word2
    return isSame

def transposeWordArray(wordArray):
    tWordArray = []
    N = len(wordArray[0])
    for i in range(N):
        tWord = ''
        for word in wordArray:
            tWord = tWord + word[i]
        tWordArray.append(tWord)
    return tWordArray

def IsWordSquare(wordArray):
    if not CheckNbyN(wordArray):
        return False
    transposedWordArray = transposeWordArray(wordArray)
    return IsSameWordArray(wordArray, transposedWordArray)

def ListUpPossibleWordsArray(input):
    wordLen = len(input[0])
    resArray, resWordList = AddWordListToArray([()], [tuple(input)], wordLen)
    return resArray

def AddWordListToArray(arrayOfWordsArray, arrayOfWordList, wordLen):
    if not arrayOfWordsArray[0] == ():
        if arrayOfWordList == [] or len(arrayOfWordsArray[0]) == wordLen:
            return arrayOfWordsArray, arrayOfWordList
    newArrayOfWordsArray = []
    newArrayOfWordList = []
    for arrayOfWords, wordList in zip(arrayOfWordsArray, arrayOfWordList):
        for word in wordList:
            newArrayOfWords = list(arrayOfWords)
            newWordList = list(wordList)
            newArrayOfWords.append(word)
            newWordList.remove(word)
            newArrayOfWordsArray.append(tuple(newArrayOfWords))
            newArrayOfWordList.append(tuple(newWordList))

    resArrayOfWordsArray, resWordList = AddWordListToArray(newArrayOfWordsArray, newArrayOfWordList, wordLen)
    return resArrayOfWordsArray, resWordList

def FindWordSquare(input):
    possibleWordsArray = ListUpPossibleWordsArray(input)
    wordSquare = []
    for wordArray in possibleWordsArray:
        if IsWordSquare(wordArray):
            wordSquare.append(wordArray)
    return wordSquare

def main():
    testWordArray = ['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD']
    expectedWordArrayOfArray = [('BALL', 'AREA', 'LEAD', 'LADY'), ('LADY', 'AREA', 'DEAR', 'YARD')]
    print(FindWordSquare(testWordArray))

if __name__ == '__main__':
    main()
