import csv

import numpy as np
import matplotlib.pyplot as plt


def findPositiveValues(reader):
    counter = 0
    for row in reader:
        for col in row:
            if col != str(0.0):
                counter+=1
    return counter;


def collectColumnsAsLists(reader, featuresSize):
    finalList = [[] for a in range(featuresSize)]
    csvList = list(reader)
    for i in range(len(csvList)):
        for j in range(len(csvList[i])):
            finalList[j].append(float(csvList[i][j]))
    return finalList


def main():
    fileX = open("data/X_train.csv")
    readerX = csv.reader(fileX)
    print("Liczba cech: " + str(len(next(readerX))))
    fileX.seek(0)
    print("Liczba przykladow: " + str(len(list(readerX))))
    fileX.seek(0)
    positiveValues = findPositiveValues(readerX)
    print("Liczba niezerowych wartosci: " + str(positiveValues))
    fileX.seek(0)

    fileY = open("data/y_train.csv")
    firstColumn = [line.split(',')[0] for line in fileY]
    mostCommon = max(set(firstColumn), key=firstColumn.count)
    print("Dominujaca klasa: " + str(mostCommon))
    probability = float(firstColumn.count(mostCommon)) / float(len(firstColumn))
    print("Prawdopodobienstwo dominujacej klasy: " + str(probability));

    featuresSize = len(next(readerX))
    fileX.seek(0)
    listOfColumns = collectColumnsAsLists(readerX, featuresSize)
    variances = []
    avgValues = []
    uniquesValuesAmount = []


    for lst in listOfColumns:
        variances.append(np.var(lst))
        avgValues.append(float(sum(lst)) / max(len(lst), 1))
        uniquesValuesAmount.append(len(np.unique(lst)))

    print(variances)


    fig, axes = plt.subplots(nrows=2, ncols=2)
    ax0, ax1, ax2, ax3 = axes.flat


    n, bins, patches = ax0.hist(variances, bins="auto", normed=1, facecolor='green', alpha=0.75)
    ax0.set_xlabel("Features")
    ax0.set_ylabel('Values')
    ax0.set_title("Variances histogram")
    ax0.set_ylim(0, max(variances))
    ax0.set_xlim(0, 233)


    ax1.hist(avgValues, bins="auto", normed=1, facecolor='green', alpha=0.75)
    ax1.set_xlabel('Features')
    ax1.set_ylabel('Values')
    ax1.set_title("Avg values histogram")
    ax0.set_ylim(0, max(avgValues))
    ax0.set_xlim(0, 233)


    ax2.hist(uniquesValuesAmount, bins="auto", range=[0, 233], normed=1,  histtype='bar')
    ax2.set_xlabel('Features')
    ax2.set_ylabel('Values')
    ax2.set_title("Unique values amount histogram")

    plt.show()


if __name__ == "__main__": main()