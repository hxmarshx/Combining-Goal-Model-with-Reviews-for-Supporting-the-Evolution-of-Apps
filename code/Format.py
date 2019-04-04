# -*- coding:utf-8 -*-
"""
@author:Xinglong Yin
@software:PyCharm
@file:Format.py
@time:2017-6-3 17:06

  ━━━━━━神兽出没━━━━━━
  　　　┏┓　　　┏┓
  　　┏┛┻━━━┛┻┓
  　　┃　　　　　　　┃
  　　┃　　　━　　　┃
  　　┃　┳┛　┗┳　┃
  　　┃　　　　　　　┃
  　　┃　　　┻　　　┃
  　　┃　　　　　　　┃
  　　┗━┓　　　┏━┛Code is far away from bug with the animal protecting
  　　　　┃　　　┃    神兽护体,永无bug
  　　　　┃　　　┃
  　　　　┃　　　┗━━━┓
  　　　　┃　　　　　　　┣┓
  　　　　┃　　　　　　　┏┛
  　　　　┗┓┓┏━┳┓┏┛
  　　　　　┃┫┫　┃┫┫
  　　　　　┗┻┛　┗┻┛
 
  ━━━━━━感觉萌萌哒━━━━━━
 
"""
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk

def getMonthDic():
    dic = {}
    dic["January"] = 1
    dic["February"] = 2
    dic["March"] = 3
    dic["April"] = 4
    dic["May"] = 5
    dic["June"] = 6
    dic["July"] = 7
    dic["August"] = 8
    dic["September"] = 9
    dic["October"] = 10
    dic["November"] = 11
    dic["December"] = 12
    return dic

def getMonth(month):
    dic = getMonthDic()
    return dic[month]

def removeStopWords(worList):
    sword = stopwords.words('english')
    result = []
    for i in worList:
        if i not in sword:
            result.append(i)
    return result

def getWordList(sent):
    wordList = word_tokenize(sent)
    finalList = []
    sword = stopwords.words('english')
    stemmer = SnowballStemmer("english")
    for i in wordList:
        temp = str(stemmer.stem(i))
        if temp in sword:
            pass
        else:
            finalList.append(temp)
    return finalList

def getWordFre(sum, wordList):
    # print wordList
    wordFreDic  = {}
    for word in wordList:
        if wordFreDic.has_key(word):
            wordFreDic[word] += 1
        elif len(word) != 1:
            wordFreDic[word] = 1

    result = sorted(wordFreDic.items(), key = lambda x: x[1], reverse = True)
    # print result
    result = [i[0] for i in result]
    # print result
    return result[: sum]

def clearSent(sent):
    symbol = ['-', '*', '.', "="]
    for i in range(1, 10):
        symbol.append(str(i))
    # if sent[0] in symbol:
    #     sent = sent[1: ]
    try:
        while sent[0] in symbol and len(sent) > 1:
            sent = sent[1:]
        sent = sent.strip()
        while sent[-1] in symbol and len(sent) > 1:
            sent = sent[: -1]
        if len(sent) == 1 and sent[0] in symbol:
            sent = ""
    except Exception, e:
        print repr(e)
        print sent + " has error"
    return sent

def writeList(f, l):
    for i in l:
        f.write(str(i) + " ")
    f.write("\n")

#May 23, 2017
def getDate(string):
    temp = string
    temp = string.replace(",", "")
    temp = temp.split(" ")
    buff = temp[2]
    buff += "-"
    month = str(getMonth(temp[0]))
    if len(month) == 1:
        buff += "0"
    buff += month
    buff += "-"
    if len(temp[1]) == 1:
        buff += "0"
    buff += temp[1]
    return buff

def isAllEnglish(string):
    return all(ord(c) < 128 for c in string)

def cutAppName(appName):
    if len(appName) > 40:
        # print appName + " the name is too long"
        appName = appName[:40]
    return appName

def addBlank(sent):
    buff = sent[0]
    symbol = [".", "!", "?", ":"]
    figure = [" "]
    for i in range(0, 10):
        figure.append(str(i))
    for i in range(1, len(sent) - 1):
        buff += sent[i]
        # if sent[i] in symbol and \
        #         (sent[i + 1].isupper() or sent[i + 1] not in figure) and \
        #         (sent[i - 1] not in figure or sent[i] != "."):
        #     buff += " "
        if sent[i] in symbol and sent[i] != "." or sent[i] == "." and sent[i - 1] not in figure\
                and sent[i + 1: i + 3] != "com":
            buff += " "
    buff += sent[-1]
    return buff


def cutMessyCode(string):
    news = ""
    for i in string:
        if ord(i) < 128:
            news += i
    news = news.replace('<br>' , '\n')
    news = news.replace('<p>' , '\n')
    news = news.replace('&#39;' , ' ')
    news = news.replace('&amp;' , 'and')
    news = news.replace('&quot;', ' ')
    news = news.replace('</p>' ,'')
    news = news.replace('\'',' ')
    news = news.replace('<b>' , '')
    news = news.replace('</b>' , '')
    news = news.replace("'", " ")
    return news

def getClearSentsList(string):
    sents = sent_tokenize(addBlank(string))
    finalList = []
    for i in sents:
        # print i + " len is " + str(len(i))
        temp = clearSent(i)
        if len(temp.split()) != 0:
            finalList.append(temp)
    return finalList

def normalizeFileName(fileName):
    illegalSymbol = ["/", "\\", ":", '"', "<", ">", "|", "?"]
    for i in illegalSymbol:
        fileName = fileName.replace(i, " ")
    return fileName

def getVerbAndNounSetTuple(string, cutStem = False):
    # print string
    sword = stopwords.words('english')
    stemmer = SnowballStemmer("english")
    sword.extend(["'s", "'re"])
    verbSet = []
    nounSet = []
    # string = string.replace(",", " ")
    # print word_tokenize(string)
    wordAndTag = nltk.pos_tag(word_tokenize(string))
    # print wordAndTag
    for i in wordAndTag:
        word = i[0]
        if word in sword:
            continue
        if "VB" in i[1]:
            if cutStem:
                word = str(stemmer.stem(word))
            verbSet.append(word)
        if "NN" in i[1]:
            if cutStem:
                word = str(stemmer.stem(word))
            nounSet.append(word)
    return (verbSet, nounSet)

def getVerbAndNounList(string, cutStem = False):
    wordList = []
    sword = stopwords.words('english')
    stemmer = SnowballStemmer("english")
    sword.extend(["'s", "'re"])
    # string = string.replace(",", " ")
    # print word_tokenize(string)
    wordAndTag = nltk.pos_tag(word_tokenize(string))
    # print wordAndTag
    for i in wordAndTag:
        word = i[0]
        if word in sword:
            continue
        if "VB" in i[1]:
            if cutStem:
                word = str(stemmer.stem(word))
            wordList.append(word)
        if "NN" in i[1]:
            if cutStem:
                word = str(stemmer.stem(word))
            wordList.append(word)
    return wordList
