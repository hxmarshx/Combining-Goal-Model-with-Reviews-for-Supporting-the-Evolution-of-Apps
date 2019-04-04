#/usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb
import Mysql_Goal
import Sent
from nltk import word_tokenize
import Format
import csv
import re


#file reading
def readCommentDic(appName):
    fileName = "AllComments/" + Format.normalizeFileName(appName) + "_all_comments.txt"
    try:
        f = open(fileName, "r")
    except IOError:
        print "File open error"
        print fileName
        return
    cut = "\n-----\n"
    c_cut = "\n====================\n\n"
    temp = f.read()
    comments = temp.split(c_cut)
    commentDicList = []
    for comment in comments[: -1]:
        information = comment.split(cut)
        reviewDate = information[0][13: ]
        rate = information[1][6: ]
        reviewContent = information[2][17: ]
        sent_score = information[3].split("\n")
        sentAndScore = []
        # print len(sent_score)
        for i in range(0, len(sent_score) - 1, 2):
            sent = sent_score[i]
            score = sent_score[i + 1]
            score = float(score)
            sentAndScore.append((sent, score))
        commentDic = {}
        commentDic["reviewDate"] = reviewDate
        commentDic["rate"] = int(rate)
        commentDic["reviewContent"] = reviewContent
        commentDic["sentAndScore"] = sentAndScore
        commentDicList.append(commentDic)
    f.close()
    return commentDicList


#count the number of the words in a sentence
def countSentences(sentences):
	count = 0
	r='[a-z]+'
	ws = re.findall(r,sentences)
	for c in ws:
		count += 1
	return count
	
	
#file writing
def  writeDemo(a,appName):
	fileName = "Results"+Format.normalizeFileName(appName)+".csv"
	try:
		f = open(fileName, "ab+")
	except IOError:
		print "File open error"
		print fileName
		return
	csvwriter = csv.writer(f,dialect = ("excel"))
	print "Writing..."
	csvwriter.writerow(a)
	print("Successfully written\n")
	f.close()


#main function
def Main(fileName,password,threshold):
	if "Clash Royale" in fileName:
		for s in sentences:
			word_function = ""
			word_function2 =""
			sim_NN = ""
			word_function3 =""
			word_function4 =""
			sim_VB = ""
			word_function5 =""
			word_function6 = ""
			sim_A = ""
			a = 0
			b = ""
			c = 0
			dlist = set()
			count = countSentences(s["reviewContent"])
			tuple_1 = []
			tuple_1.append(s["reviewContent"])
			tuple_1.append(count)
			print "Database connecting..."
			db = Mysql_1.connectdb(password)    
			Mysql_1.createtable(db)     
			Mysql_1.insertdb_1(db)        
			Mysql_1.querydb(db)
			print "Successfully connection"
			for n in [5,6,7,10,8,9,4,1,2,3,11]:
				a,b,c = Mysql_1.Catch_m(db,n)
				if a not in dlist:
					if a not in [4,11]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						print(float(sim) >= float(threshold))
						if float(sim) >= float(threshold):
							try:
								dlist.add(c)
								functionSim = sim
								temp = "G" + str(n)
								print temp 
								tuple_1.append(temp)
								print tuple_1
								print sim
								tuple_1.append(sim)
								print tuple_1
								dlist.add(c)	
							except Exception,e:	
								print e						
					if a in [4,11]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						if sim2 >= threshold:
							try:
								dlist.add(c)
								functionSim = sim2
								temp = "G" + str(n)
								tuple_1.append(temp)
								tuple_1.append(sim2)
								dlist.add(c)
							except Exception,e:	
								print e			
			Mysql_1.closedb(db)
			writeDemo(tuple_1)
					
	if "Duolingo  Learn Languages Free" in fileName:
		for s in sentences:
			word_function = ""
			word_function2 =""
			sim_NN = ""
			word_function3 =""
			word_function4 =""
			sim_VB = ""
			word_function5 =""
			word_function6 = ""
			sim_A = ""
			a = 0
			b = ""
			c = 0
			dlist = set()
			count = countSentences(s["reviewContent"])
			tuple_1 = []
			tuple_1.append(s["reviewContent"])
			tuple_1.append(count)
			print "Database connecting..."
			db = Mysql_1.connectdb(password)    # 连接MySQL数据库
			Mysql_1.createtable(db)     # 创建表
			Mysql_1.insertdb_2(db)        # 插入数据
			Mysql_1.querydb(db)
			print "Successfully connection"
			for n in [8,9,10,3,4,5,6,7,1,2]:
				a,b,c = Mysql_1.Catch_m(db,n)
				if a not in dlist:
					if a not in [2]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						print(float(sim) >= float(threshold))
						if float(sim) >= float(threshold):
							try:
								
								functionSim = sim
								temp = "G" + str(n)
								print temp 
								tuple_1.append(temp)
								print tuple_1
								print sim
								tuple_1.append(sim)
								print tuple_1
								dlist.add(c)
								if 	a in [8,9,10]:
									dlist.add(1)
									dlist.add(3)
									dlist.add(4)
									dlist.add(5)
							except Exception,e:	
								print e						
					if a in [2]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						if sim2 >= threshold:
							try:
								dlist.add(c)
								functionSim = sim2
								temp = "G" + str(n)
								tuple_1.append(temp)
								tuple_1.append(sim2)
								dlist.add(c)
							except Exception,e:	
								print e	
			Mysql_1.closedb(db)
			writeDemo(tuple_1)
			
	if "Google Photos" in fileName:
		for s in sentences:
			word_function = ""
			word_function2 =""
			sim_NN = ""
			word_function3 =""
			word_function4 =""
			sim_VB = ""
			word_function5 =""
			word_function6 = ""
			sim_A = ""
			a = 0
			b = ""
			c = 0
			dlist = set()
			count = countSentences(s["reviewContent"])
			tuple_1 = []
			tuple_1.append(s["reviewContent"])
			tuple_1.append(count)
			print "Database connecting..."
			db = Mysql_1.connectdb(password)    # 连接MySQL数据库
			Mysql_1.createtable(db)     # 创建表
			Mysql_1.insertdb_3(db)        # 插入数据
			Mysql_1.querydb(db)
			print "Successfully connection"
			for n in [6,7,8,9,10,1,2,3,4,5]:
				a,b,c = Mysql_1.Catch_m(db,n)
				if a not in dlist:
					if a not in [2,4]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						print(float(sim) >= float(threshold))
						if float(sim) >= float(threshold):
							try:
								dlist.add(c)
								functionSim = sim
								temp = "G" + str(n)
								print temp 
								tuple_1.append(temp)
								print tuple_1
								print sim
								tuple_1.append(sim)
								print tuple_1
								dlist.add(c)	
							except Exception,e:	
								print e						
					if a in [2,4]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						if sim2 >= threshold:
							try:
								dlist.add(c)
								functionSim = sim2
								temp = "G" + str(n)
								tuple_1.append(temp)
								tuple_1.append(sim2)
								dlist.add(c)
							except Exception,e:	
								print e
					
			Mysql_1.closedb(db)
			writeDemo(tuple_1)

	if "Instagram" in fileName:
		for s in sentences:
			word_function = ""
			word_function2 =""
			sim_NN = ""
			word_function3 =""
			word_function4 =""
			sim_VB = ""
			word_function5 =""
			word_function6 = ""
			sim_A = ""
			a = 0
			b = ""
			c = 0
			dlist = set()
			count = countSentences(s["reviewContent"])
			tuple_1 = []
			tuple_1.append(s["reviewContent"])
			tuple_1.append(count)
			print "Database connecting..."
			db = Mysql_1.connectdb(password)    # 连接MySQL数据库
			Mysql_1.createtable(db)     # 创建表
			Mysql_1.insertdb_4(db)        # 插入数据
			Mysql_1.querydb(db)
			print "Successfully connection"
			for n in [9,10,11,12,13,14,4,5,6,7,8,1,2,3]:
				a,b,c = Mysql_1.Catch_m(db,n)
				if a not in dlist:
					if a not in [3]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						print(float(sim) >= float(threshold))
						if float(sim) >= float(threshold):
							try:
								
								functionSim = sim
								temp = "G" + str(n)
								print temp 
								tuple_1.append(temp)
								print tuple_1
								print sim
								tuple_1.append(sim)
								print tuple_1
								dlist.add(c)
								if a in [9,10]:
									dlist.add(1)
									dlist.add(4)
									dlist.add(5)
								if a in [11,12,13,14]:
									dlist.add(2)
									dlist.add(6)
									dlist.add(7)
									dlist.add(8)
										
							except Exception,e:	
								print e					
					if a in [3]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						if sim2 > threshold:
							try:
								dlist.add(c)
								functionSim = sim2
								temp = "G" + str(n)
								tuple_1.append(temp)
								tuple_1.append(sim2)
								dlist.add(c)
							except Exception,e:	
								print e		
			Mysql_1.closedb(db)
			writeDemo(tuple_1)
			
	if "Maps - Navigation & Transit" in fileName:
		for s in sentences:
			word_function = ""
			word_function2 =""
			sim_NN = ""
			word_function3 =""
			word_function4 =""
			sim_VB = ""
			word_function5 =""
			word_function6 = ""
			sim_A = ""
			a = 0
			b = ""
			c = 0
			dlist = set()
			count = countSentences(s["reviewContent"])
			tuple_1 = []
			tuple_1.append(s["reviewContent"])
			tuple_1.append(count)
			print "Database connecting..."
			db = Mysql_1.connectdb(password)    # 连接MySQL数据库
			Mysql_1.createtable(db)     # 创建表
			Mysql_1.insertdb_5(db)        # 插入数据
			Mysql_1.querydb(db)
			print "Successfully connection"
			for n in [11,12,4,5,6,7,8,9,10,1,2,3]:
				a,b,c = Mysql_1.Catch_m(db,n)
				if a not in dlist:
					if a not in [2]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						print(float(sim) >= float(threshold))
						if float(sim) >= float(threshold):
							try:
								dlist.add(c)
								functionSim = sim
								temp = "G" + str(n)
								print temp 
								tuple_1.append(temp)
								print tuple_1
								print sim
								tuple_1.append(sim)
								print tuple_1
								dlist.add(c)
								if a in [11,12]:
									dlist.add(1)
									dlist.add(4)
									dlist.add(5)
									dlist.add(6)
									dlist.add(7)	
							except Exception,e:	
								print e			
					if a in [2]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						if sim2 > threshold:
							try:
								dlist.add(c)
								functionSim = sim2
								temp = "G" + str(n)
								tuple_1.append(temp)
								tuple_1.append(sim2)
								dlist.add(c)
							except Exception,e:	
								print e	
			Mysql_1.closedb(db)
			writeDemo(tuple_1)
			
	if "NFL Mobile" in fileName:
		for s in sentences:
			word_function = ""
			word_function2 =""
			sim_NN = ""
			word_function3 =""
			word_function4 =""
			sim_VB = ""
			word_function5 =""
			word_function6 = ""
			sim_A = ""
			a = 0
			b = ""
			c = 0
			dlist = set()
			count = countSentences(s["reviewContent"])
			tuple_1 = []
			tuple_1.append(s["reviewContent"])
			tuple_1.append(count)
			print "Database connecting..."
			db = Mysql_1.connectdb(password)    # 连接MySQL数据库
			Mysql_1.createtable(db)     # 创建表
			Mysql_1.insertdb_6(db)        # 插入数据
			Mysql_1.querydb(db)
			print "Successfully connection"
			for n in [11,12,4,5,6,7,8,9,10,1,2,3]:
				a,b,c = Mysql_1.Catch_m(db,n)
				if a not in dlist:
					if a not in [2]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						print(float(sim) >= float(threshold))
						if float(sim) >= float(threshold):
							try:
								dlist.add(c)
								functionSim = sim
								temp = "G" + str(n)
								print temp 
								tuple_1.append(temp)
								print tuple_1
								print sim
								tuple_1.append(sim)
								print tuple_1
								dlist.add(c)
								if a in [11,12]:
									dlist.add(1)
									dlist.add(4)
									dlist.add(5)
									dlist.add(6)
									dlist.add(7)	
							except Exception,e:	
								print e					
					if a in [2]:
						sim,sim2,wordNN,wordNN2,simNN,wordVB,wordVB2,simVB,wordJJ,wordJJ2,simA=Sent.sentenceSim(s["reviewContent"],b)
						if sim2 > threshold:
							try:
								dlist.add(c)
								functionSim = sim2
								temp = "G" + str(n)
								tuple_1.append(temp)
								tuple_1.append(sim2)
								dlist.add(c)
							except Exception,e:	
								print e	
			Mysql_1.closedb(db)
			writeDemo(tuple_1)				
	print "End of program"


#main function entry
if __name__ == '__main__':
	
	
	p = raw_input("please input the password of your Mysql Database\n")
	print "Clash Royale"
	print "Duolingo  Learn Languages Free"
	print "Google Photos"
	print "Instagram"
	print "Maps - Navigation & Transit"
	print "NFL Mobile"
	f = raw_input("please input one from the above apps\n")
	sentences = readCommentDic(a)
	t = raw_input("please input threshold\n")
	
	
	Main(f,p,t)
















