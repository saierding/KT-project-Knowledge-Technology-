
f1 = open('/Users/victor.ding/Desktop/2019S1-KTproj2-data/train-tweets.txt' ,'r')
f2 = open('/Users/victor.ding/Desktop/2019S1-KTproj2-data/eval-tweets.txt' ,'r')
f3 = open('/Users/victor.ding/Desktop/train.Emo.txt' ,'w+')
f4 = open('/Users/victor.ding/Desktop/eval.Emo.txt' ,'w+')
f5 = open('/Users/victor.ding/Desktop/2019S1-KTproj2-data/test-tweets.txt' ,'r')
f6 = open('/Users/victor.ding/Desktop/test.Emo.txt' ,'w+')

trainTweets = f1.readlines()
evalTweets = f2.readlines()
testTweets = f5.readlines()


sad_emoticons = {":-(", ":(", ":-|", ";-(", ";-<", "|-{"}
happy_emoticons = {":-)", ":)", ":o)", ":-}", ";-}", ":->", ";-)", ":)", "(:"}
positive = {"enjoy", "beautiful"}
negative = {"cry"}
def addEmoticonFeature(data, f):
    sad = 0
    happy = 0
    count = 1
    for row in data:
        row = row.replace("\"", " ")
        words = set(row.split())
        if (sad_emoticons | negative) & words:
            sad += 1
            f.write("0\n")
        elif (happy_emoticons | positive) & words:
            happy += 1
            f.write("2\n")
        else:
            f.write("1\n")
        count += 1

    print("Total sad emoticons: %d" % sad)
    print("Total happy emoticons: %d" % happy)
    print("Total emoticons: %d" % (happy + sad))
    print("Total tweets: %d" % count)


print
"Train data set: "
addEmoticonFeature(trainTweets, f3)
print
"\nDevelopment data set: "
addEmoticonFeature(evalTweets, f4)
print
"\nTest data set: "
addEmoticonFeature(testTweets, f6)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()