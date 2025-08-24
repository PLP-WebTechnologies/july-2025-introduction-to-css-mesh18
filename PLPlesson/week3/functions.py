#creating a function definittion
def greet(name):
    """greet a person by name"""
    return f"Hello, {name}!"
#function call
print(greet('Alice'))

#a function to add two numbers
def add(a, b):
    return a + b

sum = add(22,3)

print(f"the sum : {sum}")

def square(a):
    # Complex logic or implementation details
    return a * a

# Abstracting the details of another operation
def cube(x):
    # Another complex logic or implementation details
    return x * x * x

def main():
    # Using the abstracted functions without knowing their implementations
    result1 = square(3)
    result2 = cube(4.0)

    # Displaying the results
    print("Result of square:", result1)
    print("Result of cube:", result2)
    return main()

print(main())