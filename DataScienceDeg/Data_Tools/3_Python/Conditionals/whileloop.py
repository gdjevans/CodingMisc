x = 0
z = 5
mylst = [9,3,0,1,6]
seclist = []

while x <5:
    print("x is " + str(x))
    x += 1

for g in range(z):
    print(g)

for v in mylst:
    print("This item is " + str(v))
    newItem = v+ 1
    seclist.append(newItem)
print(seclist)