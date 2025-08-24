count = 1

while count<=5:
    print(f"count: {count}")
    count += 1

#break and continue statements 
print("creating new loop wiht a break  and continue statement")
count = 1

while count <= 5:
    if count == 3:
        count += 1
        continue
    print(f"count: {count}")
    count += 1