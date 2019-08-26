from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# create a D6

die = Die(6)

# make some rolls, and store result in a list
results = []
for roll_num in range(6000):
    result = die.roll()
    results.append(result)

# print(results)
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
