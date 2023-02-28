fruit = 'orange'
str_iterator = iter(fruit)

try:
    print(next(fruit))
except TypeError as te:
    print(te)
print(next(str_iterator)) # o
print(next(str_iterator)) # r
print(next(str_iterator)) # a
print(next(str_iterator)) # n
print(next(str_iterator)) # g
print(next(str_iterator)) # e


