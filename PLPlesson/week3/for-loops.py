fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(f"i love {x}")

#for is used for finite loops where the number of iterations is known

for number in range(1,6):
    print(f"Number: {number}")

#looping index starts from zero
list = [10, 20, 30, 40, 50]
for i in range(len(list)):
    print(f"Element at index {i}: {list[i]}")

print("printing odd numbers in aloop")

for number in range(1,10):
    if number % 2 == 0:
        continue
    print(f"Odd number: {number}")