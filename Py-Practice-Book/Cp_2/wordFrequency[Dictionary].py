
def word_frequency(words):
	frequency = {}
	for w in words:
		frequency[w] = frequency.get(w,0)+1
	return frequency

def read_words(file):
	return open(file).read().split()

def main(fileName):
	frequency = word_frequency(read_words(fileName))
	for word, count in frequency.items():
		print word, count

	print "Return Sorted.."
	for word in sorted(frequency, key=frequency.get, reverse=True):
		print word, frequency[word]


if __name__ == "__main__":
	import sys
	main(sys.argv[1])
