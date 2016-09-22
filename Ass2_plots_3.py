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




bbrewerId_Aroma      = defaultdict(list)
bbrewerId_appearance = defaultdict(list)
bbrewerId_palate     = defaultdict(list)
bbrewerId_taste      = defaultdict(list)
bbrewerId_overall    = defaultdict(list)

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
    bbrewerId_Aroma[d['beer/brewerId']].append(d['review/aroma'])
    bbrewerId_appearance[d['beer/brewerId']].append(d['review/appearance'])
    bbrewerId_palate[d['beer/brewerId']].append(d['review/palate'])
    bbrewerId_taste[d['beer/brewerId']].append(d['review/taste'])
    bbrewerId_overall[d['beer/brewerId']].append(d['review/overall'])
    



def xydata(data):
    X = []
    Y = []
    for k in data.keys():
        X.append(k)
        Yt = [float(i) for i in  data[k]]
        Y.append(np.mean(Yt))
    return X,Y
xbrewerId_Aroma,ybrewerId_Aroma = xydata(bbrewerId_Aroma)
xbrewerId_appearance,ybrewerId_appearance = xydata(bbrewerId_appearance)
xbrewerId_palate,ybrewerId_palate = xydata(bbrewerId_palate)
xbrewerId_taste,ybrewerId_taste = xydata(bbrewerId_taste)
xbrewerId_overall,ybrewerId_overall = xydata(bbrewerId_overall)

colors = ['red','green','magenta','purple','orange','brown','maroon','darkred','sage',
          'blue','darkblue','hotpink','gold','gray','crimson','sienna']


###### style/Aroma  ########
#x = [i for i in xrange(len(xbrewerId_Aroma))]
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.scatter(xbrewerId_Aroma,ybrewerId_Aroma,color=random.choice(colors),s=20,edgecolor='none')
ax1.set_title('Avrage Review/Aroma vs. BrewerId')
ax1.set_xlabel('BrewerId')
ax1.set_ylabel('Avrage Review/Aroma')
ax1.set_xlim([0,30000])
ax1.yaxis.grid()
plt.show()

##### style/appearance  ########
#x = [i for i in xrange(len(xbrewerId_appearance))]
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.scatter(xbrewerId_appearance,ybrewerId_appearance,color=random.choice(colors),s=20,edgecolor='none')
ax2.set_title('Avrage Review/Appearance vs. BrewerId')
ax2.set_xlabel('BrewerId')
ax2.set_xlabel('Style-Each Style represented by an integer')
ax2.set_ylabel('Avrage Review/Appearance')
ax2.set_xlim([0,30000])
ax2.yaxis.grid()
plt.show()

##### style/palate  ########
#x = [i for i in xrange(len(xbrewerId_palate))]
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.scatter(xbrewerId_palate,ybrewerId_palate,color=random.choice(colors),s=20,edgecolor='none')
ax3.set_title('Avrage Review/Palate vs. BrewerId')
ax3.set_xlabel('BrewerId')
ax3.set_ylabel('Avrage Review/Palate')
ax3.set_xlim([0,30000])
ax3.yaxis.grid()
plt.show()

##### style/taste  ########
#x = [i for i in xrange(len(xbrewerId_taste))]
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.scatter(xbrewerId_taste,ybrewerId_taste,color=random.choice(colors),s=20,edgecolor='none')
ax4.set_title('Avrage Review/Taste vs. BrewerId')
ax4.set_xlabel('BrewerId')
ax4.set_ylabel('Avrage Review/Taste')
ax4.set_xlim([0,30000])
ax4.yaxis.grid()
plt.show()

##### style/Overall  ########
fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
ax5.scatter(xbrewerId_overall,ybrewerId_overall,color=random.choice(colors),s=20,edgecolor='none')
ax5.set_title('Avrage Review/Overall vs. BrewerId')
ax5.set_xlabel('BrewerId')
ax5.set_ylabel('Avrage Review/Overall')
ax5.set_xlim([0,30000])
ax5.yaxis.grid()
plt.show()
