# Write a function hand_score that takes in a string representing a hand of cards 
# and returns it's total score. You can assume the letters in the string are only A, K, Q, J. 
# A is worth 4 points, K is 3 points, Q is 2 points, and J is 1 point. 
# The letters of the input string are not necessarily uppercase.
def hand_score(hand):
  hash = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}
  score = list(map(lambda ch: hash[ch.upper()], hand))
  # score = map(lambda ch: hash[ch.upper()], hand)
  return sum(score)

# def hand_score(hand):
#   res = 0
#   hash = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}
#   for ch in hand:
#     res += hash[ch.upper()]
#   return res

print(hand_score("AQAJ")) #11
print(hand_score("jJka")) #9 