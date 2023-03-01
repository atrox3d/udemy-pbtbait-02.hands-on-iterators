

class InfiniteNumbers:
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        val = self.a
        self.a += 1
        return val


numbers = InfiniteNumbers()
iter_numbers = iter(numbers)
print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))
print(next(iter_numbers))

while each := next(iter_numbers):
    if each < 20:
        print(each)
    else:
        break

while (each := next(iter_numbers)) < 25:
    print(each)

numbers = InfiniteNumbers()
for each in numbers:
    print(each)
    if each == 10:
        break



