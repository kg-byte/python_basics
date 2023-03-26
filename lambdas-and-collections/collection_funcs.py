from functools import reduce

domain = [1, 2, 3, 4, 5]
our_range = map(lambda num: num*2, domain)
print(list(our_range))

evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))

the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)

words = ['Boss', 'a', 'Alfa', 'fig', 'Dillon', 'denim']

print('Sorting default')
print(sorted(words))

# key function transforms values before comparison without changing the original values
print('Sorting with a lambda key')
print(sorted(words, key=lambda s: s.lower()))
print(sorted(words, key=lambda s: s.lower(), reverse=True))


#'String'.lower() == str.lower('String)
# function can be passed as objects as long as there's no ()
print('sorting with a method')
words.sort(key=str.lower)
print(words)
words.sort(key=str.lower, reverse=True)
print(words)
