#Section 2.3

#sum the numbers 1 through N

#N = int(input("Enter your N value here: "))

"""
summation = 0

j = 1

while j <= N:
    summation = summation + j
    j = j + 1
print("Our summation is equal to ", summation)
"""

counter = 0

while counter <= 5:
    print("Interior loop value")
    counter = counter +1
else:
    print("Exterior loop value")