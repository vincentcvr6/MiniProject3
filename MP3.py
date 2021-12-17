import gensim.downloader as api
import pandas as pd
import csv
import numpy as np

chosenModel = "glove-twitter-50"
infoModel = api.info(chosenModel)
lengthOfVocab = infoModel["nbrOfInstances"]
model = api.load(chosenModel)
synonymdata = pd.read_csv("synonyms.csv")
correctChoise, incorrectChoise = 0
listOfQuestions, listOfAns, firstWordList, secondWordList, thirdWordList, fourthWordList = ([] for i in range(6))
arrOflists = np.array([firstWordList, secondWordList, thirdWordList, fourthWordList])
lines = synonymdata.loc[:, :].values
DataAnalysis = open('analysis.csv', 'a+', newline='')
analysisOutput = csv.writer(DataAnalysis)
accuracy = correctChoise/incorrectChoise
data = [chosenModel, lengthOfVocab, correctChoise, incorrectChoise, accuracy]
analysisOutput.writerow(data)

f = open('{}-details.csv'.format(chosenModel), 'w', newline='')
writer = csv.writer(f)

for line in lines:
        listOfQuestions.append(line[0]),listOfAns.append(line[1]),firstWordList.append(line[2]),secondWordList.append(line[3]),thirdWordList.append(line[4]),fourthWordList.append(line[5])
for i in range(len(listOfQuestions)):
        cosine = []
        count = 0
        correctAnswer, closest = ""
        valMax = max(cosine)
        idxMax = cosine.index(valMax)

        try:
            rslt = model.most_similar(listOfQuestions[i])
            closest, similar = rslt[0]
        except KeyError:
            correctAnswer = "wrong"
            closest = "word not found in model"
            data = [listOfQuestions[i], listOfAns[i], closest, correctAnswer]
            writer.writerow(data)
            continue

for j in range(len(arrOflists)):
        try:
            cosine.append(model.similar(listOfQuestions[i], firstWordList[j]))
        except Exception:
            count += 1
            cosine.append(0)

for k in range(len(arrOflists)):
        if idxMax == k:
            closest = arrOflists[k]
        if (closest == listOfAns[i]):
            incorrectChoise += 1
            correctChoise += 1
        elif (closest == firstWordList[i] or closest == secondWordList[i] or closest == thirdWordList[i] or closest == fourthWordList[i] and closest != listOfAns[i]):
            incorrectChoise += 1
        data = [listOfQuestions[i], listOfAns[i], closest, correctAnswer]
        writer.writerow(data)
