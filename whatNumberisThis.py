# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 08:56:35 2017

@author: SHRADDHA
"""
from collections import Counter
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def whatNumberisThis(filePath):
    matchedArr = []
    
    loadExamps = open('numArr.txt','r').read()
    loadExamps = loadExamps.split('\n')
    
    i = Image.open(filePath)
    iar = np.array(i)
    iar1 = iar.tolist()
    
    inQuestion = str(iar1)
    
    for eachExamp in loadExamps:
        try:
            splitEx = eachExamp.split('::')
            currentNum = splitEx[0]
            print currentNum
            currentAr = splitEx[1]

        
            eachPixEx = currentAr.split('],')
            eachQPix = inQuestion.split('],')
            
            x=0
            
            while(x<len(eachPixEx)):
                if(eachPixEx[x] == eachQPix[x]):
                    matchedArr.append(int(currentNum))    
                x =x+1

        except Exception as e:
            print(str(e))
            
            
    print matchedArr
    y = Counter(matchedArr)
    print y
    
    graphX = []
    graphY = []

    for eachThing in y:
        graphX.append(eachThing)
        graphY.append(y[eachThing])
    
    plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=4)

    ax1.imshow(iar)

    ax2.bar(graphX,graphY,align='center')

    plt.ylim(400)
    
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    plt.show()