arr = [4,5,0,1,9,0,5,0]

result = []

zero = 0

for i in arr:
    if i != 0:
        result.append(i)
    else:
        zero += 1

for i in range(zero):
    result.append(0)

print(result)
