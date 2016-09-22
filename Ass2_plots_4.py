import numpy
import numpy as np
import urllib
import scipy.optimize
import random
from collections import defaultdict
import nltk
import string
from nltk.stem.porter import *
from sklearn import linear_model
import random

from collections import Counter, namedtuple
stops = set(nltk.corpus.stopwords.words('english'))
from nltk.collocations import *
from prettytable import PrettyTable
from scipy.stats import norm
import matplotlib.pyplot as plt
from itertools import groupby, chain
import pylab as pl

import time
import datetime

#print (datetime.datetime.fromtimestamp(1234817823).strftime('%Y-%m-%d %H:%M:%S'))


bAroma_overall      = defaultdict(list)
bTaste_overall      = defaultdict(list)
bPalate_overall     = defaultdict(list)
bappearance_overall = defaultdict(list)


### Assignment 2 DATASET STATISTICS
def parseData(fname):
  for l in urllib.urlopen(fname):
    yield eval(l)

print "Reading data..."
data = list(parseData("/home/am/UCSD_CSE190/Assignment2/beeradvocate_200K.json"))
#data = list(parseData("/home/am/UCSD_CSE190/Assignment2/Temp.json"))

#print "done"
#ax2.scatter(np.arange(30),
def feature(datum):
  feat = [1, datum]
  return feat

bABV = []
bAroma = []

#data2 = [d for d in data if d.has_key('user/ageInSeconds')]
for d in data:
    bAroma_overall[d['review/aroma']].append(d['review/overall'])
    bappearance_overall[d['review/appearance']].append(d['review/overall'])
    bPalate_overall [d['review/palate']].append(d['review/overall'])
    bTaste_overall [d['review/taste']].append(d['review/overall'])

    



def xydata(data):
    X = []
    Y = []
    for k in data.keys():
        X.append(k)
        Yt = [float(i) for i in  data[k]]
        Y.append(np.mean(Yt))
    return X,Y
xAroma,yaroma_overall           = xydata(bAroma_overall)
xappearance,yappearance_overall = xydata(bappearance_overall)
xpalate,ypalate_overall         = xydata(bPalate_overall)
xtaste,ytaste_overall           = xydata(bTaste_overall)

colors = ['red','green','magenta','purple','orange','brown','maroon','darkred',
          'blue','darkblue','hotpink','gold','gray','crimson']


####### style/Aroma  ########
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.scatter(xAroma,yaroma_overall,color=random.choice(colors),s=40,edgecolor='none')
ax1.set_title('Rating based on Aroma vs. Avrage Overall Rating ')
ax1.set_ylabel('Avrage Overall Ratin')
ax1.set_xlabel('Rating based on Aroma')
ax1.yaxis.grid()
ax1.set_xlim([0.5,6])
plt.show()

###### style/appearance  ########
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.scatter(xappearance,yappearance_overall,color=random.choice(colors),s=40,edgecolor='none')
ax2.set_title('Rating based on Appearance vs. Avrage Overall Rating')
ax2.set_xlabel('Rating Based on Appearance')
ax2.set_ylabel('Avrage Overall Rating')
ax2.yaxis.grid()
ax2.set_xlim([0.5,6])
plt.show()
#
###### style/palate  ########
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.scatter(xpalate,ypalate_overall,color=random.choice(colors),s=40,edgecolor='none')
ax3.set_title('Rating based on Palate vs.Avrage  Overall Rating')
ax3.set_xlabel('Rating Based on Palate')
ax3.set_ylabel('Avrage Overall Rating')
ax3.yaxis.grid()
ax3.set_xlim([0.5,6])
plt.show()

###### style/taste  ########
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.scatter(xtaste,ytaste_overall,color=random.choice(colors),s=40,edgecolor='none')
ax4.set_title('Rating based on Taste vs. Avrage Overall Rating')
ax4.set_xlabel('Rating based on Taste')
ax4.set_ylabel('Avrage Overall Rating')
ax4.yaxis.grid()
ax4.set_xlim([0.5,6])
plt.show()

###### style/Overall  ########
#fig5 = plt.figure()
#ax5 = fig5.add_subplot(111)
#ax5.scatter(xbrewerId_overall,ybrewerId_overall,color=random.choice(colors),s=20,edgecolor='none')
#ax5.set_title('Avrage Review/Overall vs. BrewerId')
#ax5.set_xlabel('BrewerId')
#ax5.set_ylabel('Avrage Review/Overall')
#ax5.set_xlim([0,30000])
#ax5.yaxis.grid()
#plt.show()
