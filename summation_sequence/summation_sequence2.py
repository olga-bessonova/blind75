# A number's summation is the sum of all positive numbers less than or equal to
# the number. For example: the summation of 3 is 6 because 1 + 2 + 3 = 6, the
# summation of 6 is 21 because 1 + 2 + 3 + 4 + 5 + 6 = 21. Write a function
# summation_sequence that takes in two numbers: start and length. The
# function should return a list containing length total elements. The first
# number of the sequence should be the start number. At any point, to generate
# the next element of the sequence we take the summation of the previous element.
# You can assume that length is not zero

def summation_sequence(start, length):

print(summation_sequence(3, 4)) # [3, 6, 21, 231]
print(summation_sequence(5, 3)) # [5, 15, 120]