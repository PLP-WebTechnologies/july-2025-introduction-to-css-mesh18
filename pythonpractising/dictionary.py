student ={
    "name":"justin",
    "adm_no": "20gr24",
    "course":"computer_science",
    "age":20,
    "house":"Naivasha"
}
print(f"the new database for the student is: {student}")

print("accessing the student admissino number of the student:",student["adm_no"])
print("accessing the course of the student :",student["course"])

age = student.get("age")
print(f"the student is {age} years old")

course = student.get("course")
print(f"the student is doing {course}")

name = student.get("name")
print(f"the name of the student is {name}")

house = student.get("house")
print(f"The student lives in {house}")

#--------getting key values from the dictinary-----------
key_details = student.keys()
print(f"the key attributes we need from a student is : {list(key_details)}")

print("is house one of the key elements?")
if "house" in key_details:
    print("yes!, house is one of the key details we need from a student")

student["age"] = 19
print(f"the student changed their age from 20 to 19 as shown:",student)

student.update({"year_of_admission":2024})
print("we added another key detail :", student)

for x,y in student.items():
    print(f"{x}: {y}")

classroom = {
    "student_1":{
        "name":"Jacob Makoye",
        "adm_no":"cs2308",
        "Age":19,
        "house":"nakuru",
        "year_of admission":2024,
    },
    "student_2":{
        "name":"Joseph Linda",
        "adm_no":"cs2898",
        "Age":19,
        "house":"naivasha",
        "year_of admission":2024,
    },
    "student_3":{
        "name":"Ian Opande",
        "adm_no":"cs3308",
        "Age":19,
        "house":"Kisumu",
        "year_of admission":2024,
    },
    "student_4":{
        "name":"Abigael Kemunto",
        "adm_no":"cs2428",
        "Age":19,
        "house":"nairobi",
        "year_of admission":2024,
    },
    "student_5":{
        "name":"calpin colince",
        "adm_no":"cs6438",
        "Age":19,
        "house":"narok",
        "year_of admission":2024,
    }
}
#Accessing items in the nested dictionary
print("Accessing details of the second student",classroom["student_2"])

print(f"the house of the second student is: {classroom["student_2"]["house"]}")

print(f"the name of the last student in the class is {classroom['student_5']["name"]}")

for x,y in classroom.items():
    print(x)

    for i,j in y.items():
        print(i,j)