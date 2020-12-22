# Problem 11
# Working with random data and random library
import random

values = range(30, 120)

# Choosing from a list
x = random.choice(values)
y = random.choice(values)

# Choosing more than one item
z = random.sample(values, 2)
w = random.sample(values, 4)

# Shuffle a list
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)

# Getting random number
a = random.randint(0, 100)

# A random number between 0 to 1
b = random.random()

# To get N random bits
c = random.getrandbits(200)


# Since this library is working with Mersenne Twister Algorithm we can initial
# the seed.
random.seed()
random.seed(12345)