

class InfiniteNumbers:
    """
    creates an iterator that iterates through
    numbers starting from 1, stopping at stop value
    or indefinitely
    """
    def __init__(self, stop=None):
        self.a = 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        """ returns val or raise StopIteration """
        if self.stop and self.a > self.stop:
            raise StopIteration
        else:
            val = self.a
            self.a += 1
            return val

if __name__ == '__main__':
    # iterate manually
    print(f'stop=5, calling next 5 times')
    numbers = InfiniteNumbers(stop=5)
    iter_numbers = iter(numbers)
    print(next(iter_numbers))
    print(next(iter_numbers))
    print(next(iter_numbers))
    print(next(iter_numbers))

    # iterate using a while loop inside a try/except
    print(f'stop=6, using while inside try')
    numbers = InfiniteNumbers(stop=6)
    try:
        while each := next(numbers):
            print(each)
    except StopIteration:
        pass

    # iterates using for loop
    print(f'stop=7, using for')
    numbers = InfiniteNumbers(stop=7)
    for each in numbers:
        print(each)
