import sys
import tdm
from cluster import kMeans
sentences = tdm.getSentences()
uniques = tdm.getUniqueWords(sentences)
print "sentences", sentences
vectors = tdm.sentencesToVector(sentences,uniques)
print vectors
def invlook(dd, val):
    return (key for key,value in dd.items() if value==val).next()
groups = kMeans(vectors, 2)
print "result", groups
for i,mean in enumerate(groups[1]):
    print i,":", "\n   ".join(str(x)+" "+invlook(uniques, i) \
        for i,x in enumerate(mean)),"\n"
lines = tdm.getSetFromFile()
print "".join(str(x)+" "+y+"\n" for x,y in zip(groups[2], lines))