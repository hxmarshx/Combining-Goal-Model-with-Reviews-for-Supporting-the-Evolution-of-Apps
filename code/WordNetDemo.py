# -*- coding: utf-8 -*-
"""
@author:Xinglong Yin
@software:PyCharm
@file:WordNetDemo.py
@time:2018/5/27 20:30

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
from nltk.corpus import wordnet

def getWordSimilar(word1, word2):
    max = 0
    x = wordnet.synsets(word1)
    y = wordnet.synsets(word2)
    for i in x:
        for j in y:
            temp = wordnet.path_similarity(i, j)
            if max < temp:
                max = temp
    return max


if __name__ == "__main__":
    word1 = "picture"
    word2 = "photo"
    print getWordSimilar(word1, word2)