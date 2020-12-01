# Problem 1:
# You want to round a floting point number to a fixed number of decimal places

# For simple rounding just do round(value, ndigits)

# Simple float
float_num = 13.42575

print(round(float_num, 1)) # 13.4
print(round(float_num, 2)) # 13.42
print(round(float_num, 3)) # 13.426

# Round to decimal
a = round(float_num, 0)
print(a) # 13

# You can use negetive numbers in ndigits to round to powers of 10
c_num = 1236

print(round(c, -2)) # 1200
print(round(c, -1)) # 1240

# Note :
# This is not a useful way to format a value, this method
# will change the basics of number, if you want to change the output
# of number use .format with its arguments.
d_num = 54.238
d_d = format(d_num, '0:2f') # 54.23
d_a = format(d_num, '0:0f') # 54


# Final word
# Round method is useful when working with floats in mathmatics operations,
# to fix the tiny overflows or underflows.
# Ex :
x = 1.5
y = 2.6
z = x + y # 4.100000000000000001 ( the result has overflow )
z = round(z, 2) # 4.1 (now its better)
