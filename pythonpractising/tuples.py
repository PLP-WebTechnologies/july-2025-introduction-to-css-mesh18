country = ("Kenya","Uganda","Tanzania","Rwanda","Burundi","Somalia")

print(country)
print(country[1])

#changing tuples though they are immutable
north = ("Ethiopia","South Sudan")
country += north
print("new tuple is :",country)