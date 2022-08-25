s = {'a', 'b', 'c'}
print(s)  # sequence is not preserved.
s.add(5)  # to add single element.
print(s)
s.update({10, 20})  # must supply iterables.
print(s)
s.discard('a')  # if element is present in s  it will discard it.
print(s)
s.discard('d')  # we do not have d in our set so nothing will happen. But we will not get error either.
print(s)
s.pop()  # any random value will be removed and not the last value as here sequence us not preserved.
print(s)
a = frozenset({1, 2, 3})
print(a)
s.remove('d')  # we do not have d, so we will have key error.
# as we will have error so if we write any further code that won't be executed.
