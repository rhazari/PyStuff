
def flatten_dict(collection, left_key=''):

	Dict = {}
	for right_key, value in collection.items():
		key = left_key+right_key
		if isinstance(value, dict):
			Dict.update(flatten_dict(value,key+'.'))
		else:
			Dict[key] = value
	return Dict	


print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})