
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            print "level"+str(perm)
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                print i
                yield perm[:i] + elements[0:1] + perm[i:]

t = all_perms([1,2,3,4])

#print t.next()
#print t.next()