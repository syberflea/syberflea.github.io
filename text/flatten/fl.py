from pprint import pprint


# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
num = []

# [num for elem in vec for num in elem]
for elem in vec:
    for m in elem:
        num.append(m)

pprint(num)