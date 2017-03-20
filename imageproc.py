# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:35:21 2017

@author: SHRADDHA
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import threshold as t

i1 = Image.open('images/sentdex.png')
i2 = Image.open('images/numbers/0.1.png')
i3 = Image.open('images/numbers/y0.4.png')
i4 = Image.open('images/numbers/y0.5.png')

iar1 = np.array(i1)
iar2 = np.array(i2)
iar3 = np.array(i3)
iar4 = np.array(i4)

fig = plt.figure()

ax1 = plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)

t.threshold(iar1)
t.threshold(iar2)
t.threshold(iar3)
t.threshold(iar4)

ax1.imshow(iar1)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()


