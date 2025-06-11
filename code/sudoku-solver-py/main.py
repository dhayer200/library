import random as rd

x = rd.randint
completeNumbers = list(range(1, 10))
randomBox = rd.sample(range(1, 10), x)

temp = list(range(1, 10))

for i in sorted(randomBox, reverse=True):
    if 0 <= i <= len(randomBox):
        temp.pop(i)
print(completeNumbers)
print(randomBox)
print(f"missing numbers: {temp}")
