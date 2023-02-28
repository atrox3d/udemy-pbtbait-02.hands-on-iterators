fruits = ('lemon', 'banana', 'orange')  # tuple

# the for loop creates an iterator based on the tuple
# and calls iter on every item of the sequence
for each in fruits:
    print(each)

# the for loop creates an iterator based on the string
# and calls iter on every char of the string
for each in "orange":
    print(each)

