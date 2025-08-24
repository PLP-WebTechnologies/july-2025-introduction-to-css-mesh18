#writing a python file to calculate the length if a string
x = "program"
count = 0

for i in x:
    count+=1

print(f"the number of letters in the word is: {count}")
print(len(x))

#writing a program to sum all the items in the list
numbers = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for numb in numbers:
    sum +=numb

print(f"the sum os the items in the list is: {sum}")

#writing a program that multiplies the items of a list
product = 1
for numb in numbers:
    product *= numb

print(f"the product of the items in the list is: {product}")

#writing a program to get the largest number in the list

largest_number = numbers[0]

for numb in numbers:
    if largest_number < numb:
        largest_number = numb

print(f"the largest number in the list is: {largest_number}")