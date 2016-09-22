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


beerStyle         = defaultdict(int)
beerABV           = defaultdict(int)
beerName          = defaultdict(int)
beerBrewerId      = defaultdict(int)
beerId            = defaultdict(int)
reviewAroma       = defaultdict(int)
reviewAppearance  = defaultdict(int)
reviewProfileName = defaultdict(int)
reviewPalate      = defaultdict(int)
reviewTaste       = defaultdict(int)
reviewOverall     = defaultdict(int)
reviewText        = defaultdict(int)

bABV_Aroma      = defaultdict(list)
bABV_appearance = defaultdict(list)
bABV_palate     = defaultdict(list)
bABV_taste      = defaultdict(list)
bABV_overall    = defaultdict(list)

bstyle_Aroma      = defaultdict(list)
bstyle_appearance = defaultdict(list)
bstyle_palate     = defaultdict(list)
bstyle_taste      = defaultdict(list)
bstyle_overall    = defaultdict(list)


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
    bABV_Aroma[d['beer/ABV']].append(d['review/aroma'])
    bABV_appearance[d['beer/ABV']].append(d['review/appearance'])
    bABV_palate[d['beer/ABV']].append(d['review/palate'])
    bABV_taste[d['beer/ABV']].append(d['review/taste'])
    bABV_overall[d['beer/ABV']].append(d['review/overall'])
    
    beerStyle        [d['beer/style']]    +=1
    beerABV          [d['beer/ABV']]      +=1
    beerName         [d['beer/name']] +=1
    beerBrewerId     [d['beer/brewerId']] +=1
    beerId           [d['beer/beerId']] +=1    
    reviewAroma      [d['review/aroma']]  +=1
    reviewAppearance [d['review/appearance']] +=1
    reviewProfileName[d['review/profileName']] +=1
    reviewPalate     [d['review/palate']] +=1
    reviewTaste      [d['review/taste']] +=1
    reviewOverall    [d['review/overall']] +=1
    reviewText       [d['review/text']] +=1
    
    bABV.append(float(d['beer/ABV']))
    bAroma.append(float(d['review/aroma']))



def xydata(data):
    X = []
    Y = []
    for k in data.keys():
        X.append(float(k))
        Yt = [float(i) for i in  data[k]]
        Y.append(np.mean(Yt))
    return X,Y

xABV_Aroma,yABV_Aroma = xydata(bABV_Aroma)
xABV_appearance,yABV_appearance = xydata(bABV_appearance)
xABV_palate,yABV_palate = xydata(bABV_palate)
xABV_taste,yABV_taste = xydata(bABV_taste)
xABV_overall,yABV_overall = xydata(bABV_overall)


color = np.random.rand(len(bABV))
area = np.pi*(15 * np.random.rand(len(bABV)))**2
#plt.scatter(np.array(bABV), np.array(bAroma), s=area, c=color,alpha=0.5)


          
##### ABV/Aroma  ########
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.scatter(xABV_Aroma,yABV_Aroma,color='blue',s=20,edgecolor='none')
ax1.set_ylim([0.5,5.0])
ax1.set_xlim([0,25.0])
ax1.set_title('Avrage Review/Aroma vs. ABV')
ax1.set_xlabel('ABV')
ax1.set_ylabel('Avrage Review/Aroma')
ax1.yaxis.grid()
plt.show()

##### ABV/appearance  ########
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.scatter(xABV_appearance,yABV_appearance,color='magenta',s=20,edgecolor='none')
#ax2.set_ylim([0.5,5.0])
ax2.set_title('Avrage Review/Appearance vs. ABV')
ax2.set_xlim([0,25.0])
ax2.set_xlabel('ABV')
ax2.set_ylabel('Avrage Review/Appearance')
ax2.yaxis.grid()
plt.show()

##### ABV/palate  ########
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.scatter(xABV_palate,yABV_palate,color='green',s=20,edgecolor='none')
#ax2.set_ylim([0.5,5.0])
ax3.set_xlim([0,25.0])
ax3.set_title('Avrage Review/Palate vs. ABV')
ax3.set_xlabel('ABV')
ax3.set_ylabel('Avrage Review/Palate')
ax3.yaxis.grid()
plt.show()

##### ABV/taste  ########
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.scatter(xABV_taste,yABV_taste,color='orange',s=20,edgecolor='none')
#ax2.set_ylim([0.5,5.0])
ax4.set_xlim([0,25.0])
ax4.set_title('Avrage Review/Taste vs. ABV')
ax4.set_xlabel('ABV')
ax4.set_ylabel('Avrage Review/Taste')
ax4.yaxis.grid()
plt.show()

##### ABV/Overall  ########
fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
ax5.scatter(xABV_overall,yABV_overall,color='brown',s=20,edgecolor='none')
#ax2.set_ylim([0.5,5.0])
ax5.set_xlim([0,25.0])
ax5.set_title('Avrage Review/Overall vs. ABV')
ax5.set_xlabel('ABV')
ax5.set_ylabel('Avrage Review/Overall')
ax5.yaxis.grid()
plt.show()
