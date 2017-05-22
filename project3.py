import os
import re

GLOBAL_DICT = {}

def createDict(fileName):
    '''Opens file and creates dictionary out of tokens'''
    file_object = open(fileName, "r")
    wordDict = {}
    lineList = [] # WOULD BE BETTER AS A SET?
    
    for line in file_object:
        lineList = re.split('\W', line)

        for word in lineList:
            if word.lower() not in wordDict and word != "":
                wordDict[word.lower()] = 1
            elif word.lower() in wordDict:
                wordDict[word.lower()] = wordDict[word.lower()] + 1

    return wordDict

def dirWalk(directory): # directory is the path to WEBPAGES_CLEAN
    '''Returns a list of paths for every file in a directory'''
    file_list = []
    for dirs in os.walk(directory):
        for files in dirs[2]:
            file_path = dirs[0] + '\\' +  files
            file_list.append(file_path)
    return file_list


def createDirectoryDict(fileList): # get fileList from dirWalk
    '''Iterates through list of files and updates GLOBAL_DICT'''
    global GLOBAL_DICT
    # Skipping the first two entries, which are the .json and .tsv; really forced solution for now
    iterFiles = iter(fileList)
    next(iterFiles)
    next(iterFiles)
    
    for f in iterFiles:
        fileDict = createDict(f)
        pathSplit = f.split('\\')
        docID = pathSplit[6] + '/' + pathSplit[7]

        for word in fileDict:
            if word not in GLOBAL_DICT:
                GLOBAL_DICT[word] = [(docID, fileDict[word])]
            else:
                GLOBAL_DICT[word].append((docID, fileDict[word]))

    print GLOBAL_DICT
        


createDirectoryDict(dirWalk('D:\MyDocuments\School\INF 141\project3\WEBPAGES_CLEAN'))
