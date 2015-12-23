from collections import defaultdict
def unflatten_dict(collection):
	Dict = defaultdict(dict)
	for key, value in collection.items():
		k1, delim, k2 = key.partition('.')
		if delim:
			Dict[k1].update({k2:value})
		else:
			Dict[k1] = value

	return Dict


print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})