# Iterable:
# for x in something:
#    Code and stuff
#
# Iterating


lsit = ["cx32", "agfds", "Emily", "Frany", "Rex"]
for element in lsit:
    print(element)

for element in ("Jose", "Joh", "Rusti"):
    print(element)

for letter in 'Socraticanus':
    print(letter)

for byte in b'Binaryus':
    print(byte)

# --- This will not work, because integer is not loopable
# for digit in 3243456325:
#     print(digit)

# for loop over integer you have to do it like this:
c = 3243456325
digits = [int(d) for d in str(c)]

for digit in digits:
    print(digit)

# What makes an object iterable?

usernames = ('Rainer', 'Alfonz', 'Flatsheep')
looper1 = usernames.__iter__()
print(type(looper1))

print(looper1.__next__())
print(looper1.__next__())
print(looper1.__next__())
# print(looper1.__next__()) --- error - StopIteration

print(usernames)

looper2 = iter(usernames)
print(next(looper2))
print(next(looper2))
print(next(looper2))
# print(next(looper2))

users = ['laust', 'maust', 'rust', 'somons', 'nemons']

for user in users:
    print(user)

looper = iter(users)
while True:
    try:
        user = next(looper)
        print(user)
    except StopIteration:
        break


class Portfolio:
    def __init__(self):
        self.holdings = {} # Key = ticker, Value = number of shares

    def buy(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) + shares

    def sell(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) - shares

    def __iter__(self):
        return iter(self.holdings.items())
    


p = Portfolio()
p.buy('ALPHA', 15)
p.buy('BETA', 23)
p.buy('GAMMA', 5)
p.buy('GAMMA', 76)
p.buy('ALPHA', 145)


for (ticker, shares) in p:
    print(ticker, shares)

# itertools - Functions creating iterators for efficient looping
# https://docs.python.org/3/library/itertools.html 


import itertools

ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
print(ranks)
ranks = [str(rank) for rank in ranks]

print(ranks)

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [card for card in itertools.product(ranks, suits)]

# dck = itertools.product(ranks, suits)
# i = 1
# for d in dck:
#     print(i, d)
#     i+=1

# this gives the same result:

for (index, card) in enumerate(deck):
    print(1 + index, card)


hands = [hand for hand in itertools.combinations(deck, 5)]

print(f"The number of 5-card poker hands is {len(hands)}.")