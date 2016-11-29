from tdm import getSentences,getUniqueWords,sentencesToVector

sentences = getSentences()
uniques = getUniqueWords(sentences)
vector = sentencesToVector(sentences,uniques)

print vector