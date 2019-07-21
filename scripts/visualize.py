import json
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Visualize index in a bar plot')
parser.add_argument('input_json', help='Input path for json file')
args = parser.parse_args()

json_data = None
with open(args.input_json, 'r') as json_file:
    json_data = json.loads(json_file.read())
json_data["data"] = json_data["data"][::-1]
y = []
for index in json_data["data"]:
    y.append(index["open"])
    y.append(index["low"])
    y.append(index["high"])
    y.append(index["close"])
x = [i for i, _ in enumerate(y)]

plt.style.use('ggplot')
plt.bar(x, y, color=("green", "red", "red", "green"))
plt.xlabel("Time")
plt.ylabel("Index (OMXS30)")
plt.show()