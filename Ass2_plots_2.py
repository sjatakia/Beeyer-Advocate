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
    bstyle_Aroma[d['beer/style']].append(d['review/aroma'])
    bstyle_appearance[d['beer/style']].append(d['review/appearance'])
    bstyle_palate[d['beer/style']].append(d['review/palate'])
    bstyle_taste[d['beer/style']].append(d['review/taste'])
    bstyle_overall[d['beer/style']].append(d['review/overall'])
    



def xydata(data):
    X = []
    Y = []
    for k in data.keys():
        X.append(k)
        Yt = [float(i) for i in  data[k]]
        Y.append(np.mean(Yt))
    return X,Y

xstyle_Aroma,ystyle_Aroma = xydata(bstyle_Aroma)
xstyle_appearance,ystyle_appearance = xydata(bstyle_appearance)
xstyle_palate,ystyle_palate = xydata(bstyle_palate)
xstyle_taste,ystyle_taste = xydata(bstyle_taste)
xstyle_overall,ystyle_overall = xydata(bstyle_overall)

colors = ['red','green','magenta','purple','orange','brown','maroon','darkred',
          'blue','darkblue','hotpink','gold','gray','crimson','sienna']


##### style/Aroma  ########
x = [i for i in xrange(len(xstyle_Aroma))]
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.scatter(x,ystyle_Aroma,color=random.choice(colors),s=20,edgecolor='none')
ax1.set_title('Avrage Review/Aroma vs. Style of Beer')
ax1.set_xlabel('Style-Each Style represented by an integer')
ax1.set_ylabel('Avrage Review/Aroma')
ax1.set_xlim([0,120])
ax1.yaxis.grid()
plt.show()

##### style/appearance  ########
x = [i for i in xrange(len(xstyle_appearance))]
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.scatter(x,ystyle_appearance,color=random.choice(colors),s=20,edgecolor='none')
ax2.set_title('Avrage Review/Appearance vs. Style of Beer')
ax2.set_xlabel('Style-Each Style represented by an integer')
ax2.set_ylabel('Avrage Review/Appearance')
ax2.set_xlim([0,120])
ax2.yaxis.grid()
plt.show()

##### style/palate  ########
x = [i for i in xrange(len(xstyle_palate))]
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
ax3.scatter(x,ystyle_palate,color=random.choice(colors),s=20,edgecolor='none')
ax3.set_title('Avrage Review/Palate vs. Style of Beer')
ax3.set_xlabel('Style-Each Style represented by an integer')
ax3.set_ylabel('Avrage Review/Palate')
ax3.set_xlim([0,120])
ax3.yaxis.grid()
plt.show()

##### style/taste  ########
x = [i for i in xrange(len(xstyle_taste))]
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
ax4.scatter(x,ystyle_taste,color=random.choice(colors),s=20,edgecolor='none')
ax4.set_title('Avrage Review/Taste vs. Style of Beer')
ax4.set_xlabel('Style-Each Style represented by an integer')
ax4.set_ylabel('Avrage Review/Taste')
ax4.set_xlim([0,120])
ax4.yaxis.grid()
plt.show()

##### style/Overall  ########
x = [i for i in xrange(len(xstyle_overall))]
fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
ax5.scatter(x,ystyle_overall,color=random.choice(colors),s=20,edgecolor='none')
ax5.set_title('Avrage Review/Overall vs. Style of Beer')
ax5.set_xlabel('Style-Each Style represented by an integer')
ax5.set_ylabel('Avrage Review/Overall')
ax5.set_xlim([0,120])
ax5.yaxis.grid()
plt.show()
