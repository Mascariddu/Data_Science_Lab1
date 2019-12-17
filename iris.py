import csv
import math
from matplotlib import pyplot as plt
from scipy.stats import norm
import numpy as np

# es 1

IrisList = [[], [], [], [], []]
measurements = ["Sepal length", "Sepal width", "Petal length", "Petal width"]
types = []

with open("iris.csv") as f:
    for row in csv.reader(f):
        if len(row) == 5:
            for i in range(4):
                IrisList[i].append(float(row[i]))
            IrisList[4].append(row[4])
            if not types.__contains__(row[4]):
                types.append(row[4])

print(IrisList)
# for x in IrisList:
    # print(x)

# es 2


def mean(x):
    return sum(x) / len(x)


def std(x):
    u = mean(x)
    return (mean([(x_i - u) ** 2 for x_i in x])) ** 0.5


# general mean and st dev
for i, m in enumerate(measurements):
    print(f"{m} mean {mean(IrisList[i]): 4f} std {std(IrisList[i]):.4f}")

# es 3
setMean = ["Iris-setosa"]
virMean = ["Iris-virginica"]
verMean = ["Iris-versicolor"]

for i, m in enumerate(measurements):
    print(m)
    for irisType in types:
        values = [v for v, t in zip(IrisList[i], IrisList[4]) if t == irisType]
        print(f"{irisType} mean: {mean(values): 4f} std: {std(values):.4f}")
        if irisType == "Iris-setosa":
            setMean.append(mean(values))
        elif irisType == "Iris-virginica":
            virMean.append(mean(values))
        elif irisType == "Iris-versicolor":
            verMean.append(mean(values))

# es 4
# i have to choose the most characterizing value for the species
colors = ['b','g','r']
for i, m in enumerate(measurements):
    plt.figure()
    plt.title(m)
    for iris_type, color in zip(types, colors):
        # For each measurement and for each type of iris, build a list of values
        values = [v for v,t in zip(IrisList[i], IrisList[4]) if t == iris_type ]
        plt.hist(values, density=True, alpha=0.2, color=color)
        u = mean(values)
        s = std(values)
        x = np.linspace(u-5*s, u+5*s, 100)
        plt.plot(x, norm(u,s).pdf(x), label=iris_type, color=color)
        plt.legend()
    plt.show()

# es 5
print(setMean)
print(verMean)
print(virMean)
first = [5.2, 3.1, 4.0, 1.2]
second = [4.9, 2.5, 5.6, 2.0]
third = [5.4, 3.2, 1.9, 0.4]
vector = [first, second, third]

tipo = ["Anyone", "Anyone", "Anyone"]
for index, x in enumerate(vector):
    minimo = 100
    diff = [0, 0, 0]
    for id, value in enumerate(x):
            diff[0] += abs(value - setMean[id+1])
            diff[1] += abs(value - virMean[id+1])
            diff[2] += abs(value - verMean[id+1])
    for i, val in enumerate(diff):
        if val < minimo:
            indice = i
            minimo = val
    if indice == 0:
        tipo[index] = "Setosa"
    elif indice == 1:
        tipo[index] = "Virginica"
    elif indice == 2:
        tipo[index] = "Versicolor"

print(tipo)
