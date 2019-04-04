#/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import nltk
import WordNetDemo

from nltk.corpus import stopwords
from nltk import word_tokenize

#Stopwords removing
def removeStopWords(worList):
    sword = stopwords.words('english')
    sword2 = []
    for s in [',','.','/','<','>','?',';',':',"'",'"','[',']','{','}','\\','|','!','@','#','$','%','^','&','*','(',')','-','_','=','+']:
		sword2.append(s)
    result = []
    for i in worList:
        if i not in sword:
            result.append(i)
    return result


#Two sentence similarity functions comparing
def sentenceSim(sent,sent2):
	
	a=word_tokenize(sent)
	b=word_tokenize(sent2)
	
	wordList = removeStopWords(a)
	wordList2 = removeStopWords(b)
	
	#print "第一句话预处理后的结果为：" + str(wordList)+"\n"
	#print "第二句话预处理后的结果为：" + str(wordList2)+"\n"
	
	pos = nltk.pos_tag(wordList)
	pos2 = nltk.pos_tag(wordList2)
	
	#print "第一句话PoS处理后的结果为：" + str(pos)+"\n"
	#print "第二句话PoS处理后的结果为：" + str(pos2)+"\n"
	
	simNN = 0
	simVB = 0
	simA = 0
	wordNN=' '
	wordNN2=' '
	wordVB=' '
	wordVB2=' '
	wordJJ=' '
	wordJJ2 =' ' 
	for m,n in pos:
		for m2,n2 in pos2:
			if "NN" in n and "NN" in n2:
				temp = WordNetDemo.getWordSimilar(m,m2)
				if simNN < temp:
					simNN = temp
					wordNN = m
					wordNN2 = m2
					#if int(simNN)==1:
					#	print m+n+"\t"+m2+n2
			elif "VB" in n and "VB" in n2:
				temp2 = WordNetDemo.getWordSimilar(m,m2)
				if simVB < temp2:
					simVB = temp2
					wordVB = m
					wordVB2 = m2
					#if int(simVB)==1:
					#	print m+n+"\t"+m2+n2
			elif "JJ"  in n or "RB"  in n  and "JJ"  in n2 or "RB"  in n2:
				temp3 = WordNetDemo.getWordSimilar(m,m2)
				if simA < temp3:
					simA = temp3
					wordJJ = m
					wordJJ2 = m2
					#if int(simA)==1:
					#	print m+n+"\t"+m2+n2
	score = 0.50*simNN + 0.5*simVB
	score2 = 0.25*simNN + 0.25*simVB + 0.5*simA
	return (score,score2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA)
