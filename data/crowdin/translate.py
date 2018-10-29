import os
import json
import pandas as pd

import time

FLODER_PATH = './edm_data'
KEYS = [ 'title', 'sub_title',  'description' ]

outDict = {}

def createMap(fileName, content):
    with open('./outmap/' + fileName + '.map.json', 'w') as f:
        json.dump(content, f)

def outputFile(content):
    with open('./outfile/source.json', 'w') as f:
        json.dump(content, f)


def readFile(name, dir):
    list = []
    i = 0
    filename = os.path.splitext(name)[0]
    with open(dir, 'r', encoding='utf-8') as f:
        datas = json.loads(f.read())['datas']
        for item in datas:
            it = item['data']
            for key in KEYS:
                if not pd.isnull(it[key]):
                    list.append(it[key])
                    it[key] = '*#' + filename + '_' + str(i) + '#*'
                    i += 1
            if (not pd.isnull(it['btn'])) and (not pd.isnull(it['btn']['text'])):
                list.append(it['btn']['text'])
                it['btn']['text'] = '*#' + filename + '_' + str(i) + '#*'
                i += 1

        createMap(filename, datas)
        for item in list:
            outDict[filename + '_' + str(list.index(item))] = item


def openfile(rootdir):
    for lists in os.listdir(rootdir):
        path = os.path.join(rootdir, lists)
        if os.path.isdir(path):
            openfile(path)
        else:
            if os.path.splitext(lists)[1] == '.json':
                readFile(lists, path)
    outputFile(outDict)
    print('Done!')

openfile(FLODER_PATH)

