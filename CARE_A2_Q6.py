
n = 10
m = 12
p = 12
k = 2
j = 3

banana = m // k

if m % k != 0:
    banana += 1

peanut = p // j

if p % j != 0:
    peanut += 1

eat = banana + peanut

print(n - eat)
