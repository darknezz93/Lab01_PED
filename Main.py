import csv


def readFile(filePath):
    f = open(filePath)
    reader = csv.reader(f)
    for row in reader:
        print(row)
    f.close()


def main():
    readFile("data/y_train.csv")




if __name__ == "__main__": main()