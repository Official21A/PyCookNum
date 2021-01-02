# Poblem 12
# Converting a date into seconds, hours, and ....
from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)

c = a + b
print(c.days, c.seconds, c.seconds / 3600, c.total_seconds / 3600)

# Now using datetime
from datetime import datetime
a = datetime.now()

print(a + timedelta(days=10))

d = a - datetime(2012, 12, 21)

print(d.days)

# For advanced operations use the dateutil library of the datetime
