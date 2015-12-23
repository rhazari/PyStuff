

def anagrams(wordList):
	dict = {}
	for word in wordList:
		dict[word] = "".join(sorted(word))
	for w in sorted(dict, key = dict.get):
		print w, dict[w]

anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])