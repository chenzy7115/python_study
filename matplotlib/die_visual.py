from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6 and D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll()+die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "投掷出的数字", 'dtick': '1'}
y_axis_config = {"title": "不同数字出现频率"}
my_layout = Layout(
    title="掷1个6面骰子和1个10面骰子 50 000次的结果",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
offline.plot({"data": data, "layout": my_layout}, filename="d6_d10.html")
