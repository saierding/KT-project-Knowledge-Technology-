

f1 = open('/Users/victor.ding/Desktop/2019S1-KTproj2-data-ARFF/train.arff', 'r')
f2 = open('/Users/victor.ding/Desktop/2019S1-KTproj2-data-ARFF/eval.arff', 'r')
f3 = open('/Users/victor.ding/Desktop/train.Emo.txt', 'r')
f4 = open('/Users/victor.ding/Desktop/eval.Emo.txt', 'r')
f5 = open('/Users/victor.ding/Desktop/train.Emo.arff', 'w+')
f6 = open('/Users/victor.ding/Desktop/eval.Emo.arff', 'w+')

trainData = f1.readlines()
evalData = f2.readlines()
trainEmo = f3.readlines()
evalEmo = f4.readlines()


def addEmoFeature(rawData, emoData, f, index1, index2):
    for i, row in enumerate(rawData):
        if i < index1:
            f.write(row)

        else:

            sentiment = row[index2:len(row)]

            row = row[0:index2]
            emo = emoData[i - index1][0] + ","
            row = row.replace(row, row + emo + sentiment)

            f.write(row)


addEmoFeature(trainData, trainEmo, f5, 49, 109)
addEmoFeature(evalData, evalEmo, f6, 49, 109)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
