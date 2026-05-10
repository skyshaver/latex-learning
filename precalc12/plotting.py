import matplotlib.pyplot as plt

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

domain = [0, -2, -4, 2, 4]
range = [2 * x + 1 for x in domain]

print(domain)
print(range)

d2 = [0, 1, 2, 3, -2, -3, -4]
r3 = [-9, 8, 8, 13, 5, -4, 14]

# has to be 2 lists
# calculate range from domain
# plt.plot(domain, [2 * x + 1 for x in domain], 'ro')
plt.plot(d2, r3,'r')
plt.axis((-20, 20, -20, 20))
plt.show()
