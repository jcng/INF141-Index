import os
import re
import math
from collections import namedtuple
import sys

class Index:
    def __init__(self,directory):
        self.docLengthIndex ={}
        self.docindex={}
        self._index_a = {}
        self._index_b = {}
        self._index_c = {}
        self.index = {}
        self.docs = 0
        self.createDirectoryDict(self.dirWalk(directory))
        self.createStatsDict()
        self.createFinalDict()
        
        
        
    def createDict(self,fileName):
        '''Opens file and creates dictionary out of tokens'''
        file_object = open(fileName, encoding="utf8")
        wordDict = {}
        lineList = [] # WOULD BE BETTER AS A SET?
        
        for line in file_object:
            lineList = re.split('\W', line)
        
            for word in lineList:
                if word.lower().isalnum():
                    if word.lower() not in wordDict and word != "":
                        wordDict[word.lower()] = 1
                    elif word.lower() in wordDict:
                        wordDict[word.lower()] = wordDict[word.lower()] + 1
            
        return wordDict
    
    def dirWalk(self,directory): # directory is the path to WEBPAGES_CLEAN
        '''Returns a list of paths for every file in a directory'''
        file_list = []
        for dirs in os.walk(directory):
            for files in dirs[2]:
                self.docs+=1
                file_path = dirs[0] + '\\' +  files
                file_list.append(file_path)
        return file_list
    
    
    def createDirectoryDict(self,fileList): # get fileList from dirWalk
        '''Iterates through list of files and updates GLOBAL_DICT'''
        stats=namedtuple('stats',['tf','logtf'])
        # Skipping the first two entries, which are the .json and .tsv; really forced solution for now
        iterFiles = iter(fileList)
        next(iterFiles)
        next(iterFiles)
        
        for f in iterFiles:
            fileDict = self.createDict(f)
            pathSplit = f.split('\\')
            docID = pathSplit[1] + '/' + pathSplit[2]
    
            for word in fileDict:
                ID=docID
                tf=fileDict[word]
                logtf=math.log10(tf)
                if word not in self._index_a:
                    self._index_a[word] = {ID:stats(tf,logtf)}
                else:
                    self._index_a[word][ID]=stats(tf,logtf)
        
    def createStatsDict(self):
        stats=namedtuple('stats',['df','idf'])
        for key in self._index_a.keys():
            deg_freq=len(self._index_a[key])
            N=self.docs
            i_deg_freq=math.log10(N/deg_freq)
            self._index_b[key]=stats(deg_freq,i_deg_freq)
    
    def createFinalDict(self):
        stats=namedtuple('stats',['tf','logtf','df','idf','tfidf'])
        for key in self._index_a.keys():
            for item in self._index_a[key]:
                s=self._index_a[key][item]
                tf=s.tf
                logtf=s.logtf
                df=self._index_b[key].df
                idf=self._index_b[key].idf
                tfidf=1+logtf*idf
                if key not in self.index:
                    self.index[key]={item:stats(tf,logtf,df,idf,tfidf)}
                else:
                    self.index[key][item]=stats(tf,logtf,df,idf,tfidf)
                
    