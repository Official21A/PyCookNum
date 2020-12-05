# Problem 5
# Converting large length integer into a byte string
# There are two methods to do this :
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004' # 16 bits 
a = int.from_bytes(data, 'little') # 691205656675113957766354792709
b = int.from_bytes(data, 'big') # 9452284252074728448711777277

# A good example handeling
x = 523 ** 23

nbytes, rem = divmod(x.bit_length(), 8)
if rem:
	nbytes += 1

c = x.to_bytes(nbytes, 'little')
