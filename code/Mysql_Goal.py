#!/usr/bin/env python
# coding=utf-8

import MySQLdb


#Database connecting
def connectdb(p):
    db = MySQLdb.connect(host = "127.0.0.1",
                         port = 3306, user = "root",
                         passwd = p,
                         db = "MYSQL")
    return db


#Table creating
def createtable(db):
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS Tree")
    sql = """CREATE TABLE Tree (
            ID INT NOT NULL,
            Text VARCHAR(1000),
            Parent INT )"""
    cursor.execute(sql)
    cursor.close()


#Goal Trees inserting	
def insertdb_1(db): 
    cursor = db.cursor()
    sql = """INSERT INTO Tree
         VALUES (1, 'Playing game', 0),
                (2, 'Purchasing game items with real money', 0),
                (3, 'Watching videos on TV Royale',0),
                (4, 'All the operations are real-time', 0),
                (5, 'Compete and duel with multiplayers from around the world and take their trophies', 1),
                (6, 'Operate on cards, which are items in the game. Players can earn, share, build, collect and upgrade cards', 1),
                (7, 'Group players, build battle community', 1),
                (8,'Searching things with keywords',2),
                (9,'Discover accounts by inputting user name',2),
                (10,'Set up password protection for purchases in the settings of your Google Play Store app',2),
                (11,'Safety: guarantee the account is safe',0)"""
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
    except Exception, e:
        print 'input error!'
        print e
        db.rollback()

def insertdb_2(db):
    cursor = db.cursor()
    sql = """INSERT INTO Tree
         VALUES (1, 'Learning Language, including Spanish, French, German, Italian, Russian, Portuguese, Turkish, Dutch, Irish, Danish, Swedish, Ukrainian, Esperanto, Polish, Greek, Hungarian, Norwegian, Hebrew, Welsh, English, Swahili and Romanian', 0),
                (2, 'Funny, interesting, painless and peppy', 0),
                (3, 'Leaning lessons: basic verbs, phrases, and sentences, and new words',1),
                (4, 'Practicing skills: speaking, reading, listening and writing skills', 1),
                (5, 'Have examinations for evaluating the level of ability', 1),
                (6, 'Playing a game', 1),
                (7, 'Communicate and share with friends', 1),
                (8,'Divide the lessons into blocks',3),
                (9,'Make schedules for assigning the time according to users',3),
                (10,'Tracking the learning progress and discovering the achievements',3)"""
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
    except Exception, e:
        print 'input error!'
        print e
        db.rollback()

def insertdb_3(db): 
    cursor = db.cursor()
    sql = """INSERT INTO Tree
         VALUES (1, 'Save photo and videos', 0),
                (2, 'Safe, secure, and private to users', 0),
                (3, 'Edit photo and videos',0),
                (4, 'Automatically', 0),
                (5, 'Share photo and videos with any contact, email, or phone number, right from the app', 0),
                (6, 'Organize photo, create and get album', 1),
                (7, 'Back up photos and videos in High Quality.', 1),
                (8,'Search for photos by the people, places and things in them',1),
                (9,'Enhance your photos, adjust lighting, contrast, color, and vignette, or pick from 14 innovative photo filters to make your pictures look great in one tap',3),
                (10,'Create movies, collages, animations, panoramas, and more from your photos',3)"""
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
    except Exception, e:
        print 'input error!'
        print e
        db.rollback()

def insertdb_4(db):
    cursor = db.cursor()
    sql = """INSERT INTO Tree
         VALUES (1, 'Capture moments and follow your friends and family to see what they are up to', 0),
                (2, 'Share moments: share things you love', 0),
                (3, 'Easy to use',0),
                (4, 'Discover accounts from all over the word', 1),
                (5, 'Searching the things by inputting key words', 1),
                (6, 'Handle photos', 2),
                (7, 'Handle vides', 2),
                (8,'Send text message',2),
                (9,'Discover accounts by inputting user name',4),
                (10,'Discover accounts by inputting phone number',4),
                (11,'Edit photo, including its color, light, contrast.',6),
                (12,'Post photos to your profile grid',6),
                (13,'Edit video, adjusting its color, light and contrast, and combine multiple clips into one video',7),
                (14,'Post video to your profile grid',7)"""
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
    except Exception, e:
        print 'input error!'
        print e
        db.rollback()

def insertdb_5(db): 
    cursor = db.cursor()
    sql = """INSERT INTO Tree
         VALUES (1, 'Navigating, guiding persons to their destinations', 0),
                (2, 'Real-time, quickly and timely', 0),
                (3, 'Travelling, supporting people to schedule their journey',0),
                (4, 'Discover places and explore like a local by inputting keywords', 1),
                (5, 'Save places you want to or often visit, and quickly find them later from any computer or device', 1),
                (6, 'Routing the road', 1),
                (7, 'Gaining traffic information, road closures and traffic incidents and transit schedules.', 1),
                (8,'Understanding places with reviews, ratings, and pictures of foods and interiors',3),
                (9,'Make reservations',3),
                (10,'Sharing information to help others by sharing reviews, photos',3),
                (11,'Find pit stops along your route like gas stations and coffee spots',4),
                (12,'Find business, including restaurants, shops, museums, along your route.',4)"""
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
    except Exception, e:
        print 'input error!'
        print e
        db.rollback()

def insertdb_6(db):
    cursor = db.cursor()
    sql = """INSERT INTO Tree
         VALUES (1, 'Watch football game, viewing all demanded videos', 0),
                (2, 'Real-time, quickly and timely', 0),
                (3, 'Track the teams in league for accessing them',0),
                (4, 'Searching for the games according to users demands', 1),
                (5, 'See the NFL Network schedule', 1),
                (6, 'Subscript the contents according to the users interest', 1),
                (7, 'Replay every game with NFL Game Pass', 1),
                (8,'Gain information around the NFL, reading articles, stories, topics and breaking news',3),
                (9,'Group fans of one team together and sharing information ',3),
                (10,'Browse NFL Shop for buying products of teams',3),
                (11,'Searching games by name of team',4),
                (12,'Searching games by time',4)"""
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
    except Exception, e:
        print 'input error!'
        print e
        db.rollback()


#Goal Trees querying
def querydb(db):
    cursor = db.cursor()
    sql = "SELECT * FROM Tree"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            ID = row[0]
            Text = row[1]
            Parent = row[2]
            print "ID: %d, Text: %s, Parent: %d" % \
                (ID, Text, Parent)
            cursor.close()
    except:
        print "Error: unable to fecth data"

def deletedb(db):
    cursor = db.cursor()
    sql = "DELETE FROM Tree WHERE Parent = '%d'" % (100)

    try:
       cursor.execute(sql)
       db.commit()
    except:
        print 'delete error!'
        db.rollback()

def updatedb(db): 
    cursor = db.cursor()
    sql = "UPDATE Tree SET Parent = Parent + 3 WHERE ID = '%s'" % ('003')
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print 'updata error!'
        db.rollback()


#Database closing
def closedb(db):
    db.close()


#Goal Trees Matching
def Catch_m(db,m):
	cursor = db.cursor()
	sql = "SELECT * FROM Tree"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			ID = row[0]
			Text = row[1]
			Parent = row[2]
			if ID == m :
				print "Successfully Match"
				cursor.close()
				return ID, Text, Parent
		
		else :
			print "match error"
			return 0,0,0
	except Exception,e:
		print e
		print "Error: unable to fecth data"

