# If you want a way to convert the numbers and string
# into any bases from any base with one order, use python library
# 	"baseconvert".

# To install :
# 	pip install baseconvert

# Ex :
#   Basic form of usage
# 	base(number, input_base, output_base)
#
# 	>>> base((15, 15, 0, ".", 8), 16, 10)
# 	(4, 0, 8, 0, '.', 5)
# 	>>> base("FF0.8", 16, 10, string=True)
# 	'4080.5'
# 	>>> base("4080.5", 10, 16, string=True)
# 	'FF0.8'


# Ex :
# 	>>> n = (15,15,".",0,8)
# 	>>> base(n, 16, 10)
# 	(2, 5, 5, '.', 0, 3, 1, 2, 5)
# 	>>> base(n, 16, 10, string=True)
# 	'255.03125'

# 	>>> base("FF.08", 16, 10) == base((15,15,".",0,8), 16, 10)
# 	True

# A callable BaseConverter object can also be created.
# This is useful for when several numbers need to be converted.

# 	>>> b = BaseConverter(input_base=16, output_base=8)
# 	>>> b("FF")
# 	(3, 7, 7)
# 	>>> b((15, 15))
# 	(3, 7, 7)
# 	>>> b("FF") == b((15,15))
# 	True

# 	>>> base(0.1, 3, 10, string=True)
# 	'0.[3]'
