import re
import Porter_Stemmer_Python



stopFile = "stop_words.txt"
sentenceFile = "sentences.txt"


def getSetFromFile(filename = sentenceFile):
	with open(filename) as f:
    		return f.read().splitlines()


def trimString(s):
	return "".join([c for c in s.lower() if c.isalpha() or c.isspace()]).split()

def getUniqueWords(sentences):
	ret = {}
	i = 0
	for s in sentences:
		for w in s:
			if w not in ret:
				ret[w] = i
				i += 1
	return ret

def getSentences():
	stem = Porter_Stemmer_Python.PorterStemmer()
	stopWords = getSetFromFile(stopFile)
	sentences = getSetFromFile(sentenceFile)

	trimmedSentences = []
	print type(sentences)

	for s in sentences:
		nextLine = []
		for w in trimString(s):
			if w not in stopWords:
				nextLine.append(stem.stem(w,0,len(w)-1))

		trimmedSentences.append(nextLine)

	return trimmedSentences

def sentencesToVector(sentences,uniques):
	ret = []
	for s in sentences:

		vector = [0 for x in range(len(uniques))]
		for w in s:
			vector[uniques[w]]+=1
			print w
		print "\n"
		ret.append(vector)

	return ret