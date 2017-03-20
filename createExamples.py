# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 08:17:35 2017

@author: SHRADDHA
"""
from PIL import Image
import numpy as np

def createExamples():
    ArrayExamples = open('numArr.txt','a')
    numberWeHave = range(0,10)
    VersionWeHave = range(1,10)
    
    for eachNum in numberWeHave:
        for eachVer in VersionWeHave:
            ImagePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            i = Image.open(ImagePath)
            iar = np.array(i)
            strn = str(iar.tolist())
            linetoWrite = str(eachNum)+'::'+strn+'\n'
            ArrayExamples.write(linetoWrite)
            