from collections import Counter
import os, random, re
import math

#Method to read words from a file and clear it using regular expression
def read_words(words_file):
    with open(words_file, 'r') as word:
        string=word.read().lower()
        return re.findall(r"[\w']+", string)

#Finding probability of all the words belonging to a class and also avoiding zero probability error
def probablityword(myhash, word, denominator):
    word=word.lower()
    if word in myhash:
        return math.log(myhash[word]+1.0)/denominator
    return math.log(1.0/denominator)

#Finding total probability
def probability(filename, myhash, denominator):
    l = list(map(lambda x: probablityword(myhash, x, denominator), read_words(filename)))
    return reduce(lambda x,y: x+y, l)

#method used to classify the data
def classify(filename, mainhash, trainsum, totalcounter):
    print(filename)
    mykeys = trainsum.keys()
    probabilityvalues = list(map(lambda x: probability(filename, mainhash[x], trainsum[x]+totalcounter), mykeys))
    minval = min(probabilityvalues)
    maxval = max(probabilityvalues)
    median = (minval + maxval)/2
    probabilityvalues = list(map(lambda x: x - maxval, probabilityvalues))
    denominator = sum(list(map(lambda x: math.exp(x), probabilityvalues)))
    probabilityvalues = list(map(lambda x: math.exp(x)/denominator, probabilityvalues))
    maxval = max(probabilityvalues)
    print(maxval)
    maxindex = [i for i in range(len(probabilityvalues)) if probabilityvalues[i] == maxval]
    if(len(maxindex) > 1):
        print 'Tie'
        # TODO: Fix here
    return mykeys[maxindex[0]]

path=os.listdir(os.getcwd()+'/newsgroups')
filelist={}
testlist = {}
trainlist = {}
for foldername in path:
    appendpath = os.getcwd() + '/newsgroups/' + foldername + '/'
    filepath=os.listdir(os.getcwd()+'/newsgroups/'+foldername)
    filelist[foldername]= filepath
    randomlist = range(0,len(filepath))
    random.shuffle(randomlist)
    #testlist to hold half of the test data which is to be tested
    testlist[foldername] = list(map(lambda x: appendpath + filepath[x] , randomlist[:(len(filepath)/2)]))
    # trainlist to hold half of the train data which is used to train the model
    trainlist[foldername] = list(map(lambda x: filepath[x], randomlist[(len(filepath)/2):]))

#count the occurences of every unique word
count = dict(zip(path, list(map(lambda x: len(filelist[x]), path))))
traincount = {}
globalcounter = Counter()
trainsum = {}
for key in path:
    print key
    cwd = os.getcwd()+'/newsgroups/'+key+'/'
    c = Counter()
    for file in trainlist[key]:
        c = c + Counter(read_words(cwd + str(file)))
    globalcounter = globalcounter + c
    traincount[key] = dict(c)
    trainsum[key] = sum(traincount[key].values())
globalcounter = len(dict(globalcounter).keys())

#Classify the test data from the train model
print(testlist.keys()[0])
length=len(testlist.keys())
for i in range(0, length):
    lengthoffiles=len(testlist[testlist.keys()[i]])
    for j in range(0, lengthoffiles):
        print("starting classify.....")
        print(classify(testlist[testlist.keys()[i]][j], traincount, trainsum, globalcounter))