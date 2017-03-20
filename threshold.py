# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:46:45 2017

@author: SHRADDHA
"""

def threshold(imageArray):
    balancearr = []
    newArr = imageArray
    
    for eachRow in newArr:
        for eachPix in eachRow:
            avgnum = reduce(lambda x,y:x+y, eachPix[:3])/len(eachPix[:3])
            balancearr.append(avgnum)
    balance = reduce(lambda x,y:x+y,balancearr)/len(balancearr)
    
    for eachRow in newArr:
        for eachPix in eachRow:
            if (reduce(lambda x,y:x+y, eachPix[:3])/len(eachPix[:3]) > balance):
                eachPix[0]=255
                eachPix[1]=255
                eachPix[2]=255
                eachPix[3]=255
            else:
                eachPix[0]=0
                eachPix[1]=0
                eachPix[2]=0
                eachPix[3]=255
    return newArr