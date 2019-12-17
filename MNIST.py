import csv
import math

# es1
myList = []

with open("mnist_test.csv") as f:
    for row in csv.reader(f):
        l = []
        for x in row:
            l.append(x)
        myList.append(l)

# es2


def picture(n):
    r = myList[n]
    count = 0
    string = ""

    for i in range(1, len(r)):
        if int(r[i]) < 64:
            string += " "
        elif int(r[i]) < 128:
            string += "."
        elif int(r[i]) < 192:
            string += "*"
        elif int(r[i]) < 256:
            string += "#"
        count += 1
        if count == 28:
            string += "\n"
            count = 0
    return string


print(picture(9))

# es3


def euclidean(vec1, vec2):
    dist = 0
    for x, y in zip(vec1[1:], vec2[1:]):
        dist += (int(x) - int(y))**2
    return math.sqrt(dist)


l1 = myList[25]
l2 = myList[29]
l3 = myList[31]
l4 = myList[34]

distance1 = [round(euclidean(l1, l2), 2), round(euclidean(l1, l3), 2), round(euclidean(l1, l4), 2)]
print(distance1)
distance2 = [round(euclidean(l2, l3)), round(euclidean(l2, l4), 2)]
print(distance2)
distance3 = round(euclidean(l3, l4), 2)
print(distance3)

# es4

rank1 = sum(distance1)
rank2 = distance1[0] + sum(distance2)
rank3 = distance3 + distance1[1] + distance2[0]
rank4 = distance1[2] + distance2[1] + distance3

print(l1[0], l2[0], l3[0], l4[0])
print(round(rank1, 2), round(rank2, 2), round(rank3, 2), round(rank4, 2))

# es5
z = []
o = []

for i in range(0, 784):
    z.append(0)
    o.append(0)

for digit in myList:
    if int(digit[0]) == 0:
        for i in range(1, 785):
            if int(digit[i]) >= 128:
                z[i-1] += 1
    elif int(digit[0]) == 1:
        for i in range(1, 785):
            if int(digit[i]) >= 128:
                o[i-1] += 1

best = 0
index = None

for j in range(0, 784):
    if abs(z[j] - o[j]) > best:
        best = abs(z[j] - o[j])
        index = j

s = ""
count = 0

for i in range(0, 784):
    count += 1
    if i != index:
        s += "."
    else:
        s += "X"
    if count == 28:
        s += "\n"
        count = 0

print(s)
diff = [abs(z - o) for z, o in zip(z, o)]

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

plt.title("Z")
sns.heatmap(np.reshape(z, (28, 28)), cmap='binary')
plt.figure()
plt.title("O")
sns.heatmap(np.reshape(o, (28, 28)), cmap='binary')
plt.figure()
plt.title("diff")
sns.heatmap(np.reshape(diff, (28, 28)), cmap='binary')
plt.show()