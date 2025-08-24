#defining the function that compares the two number and return the maximum number
def max_of_two(a,b):
    if a > b:
        return a
    else:
        return b

#defining another function that compares the output of the previuos function with another interger(value)
def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z)) #returns the maximum value of the previuos function passed into the current function

print(f"the maximum number of the three is: {max_of_three(3,4,5)}")

#writing a python function that prints the the summ of all number is a list
def sum_of_list(numbers): #defining the list function
    total = 0         #assinging the value of zero to the function
    for num in numbers:
        total += num
    return total

print(f"the sum of the list is: {sum_of_list([1,2,3,4,5])}")
#a function  for printing the price aof the commodity after a given discount
def calculate_discount(price,discount_percent = 0):
    if discount_percent >= 20 :
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    
    else:
        final_price = price

    return f"the final price is {final_price}"

price = int(input("enter the price:"))
discount_percent = float(input("enter the discount percentage:"))

print(calculate_discount(price,discount_percent))
print(calculate_discount(40000))
    