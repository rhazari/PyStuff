class reverse_iter:
    def __init__(self, list):
        self.i = len(list)-1
        self.array = list

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def next(self):
        if (self.i >= 0):
            idx = self.i
            self.i -= 1
            return self.array[idx]
        else:
            raise StopIteration()

it = reverse_iter([1,4,6,9,8])
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()