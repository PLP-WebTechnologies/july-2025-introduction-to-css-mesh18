from re import L


languages = ["english","kiswahili","germany","spanish","french"]
print(languages[1])

print(languages[1:4])

print(f"the list of languages has {len(languages)} items")

#checking if the items belong to a list
if "kiswahili" in languages:
    print("yes kiswahili belongs to the languages list")

#changing the value of the items in the list
languages[1] = "sheng"
print("languges after modification is :",languages)

#to insert the item in a list
languages.insert(2,"mexican")
print("languges after insertion is : ",languages)

#to insert items at the end of the list 
languages.append("portugees")
print("languages after appending an items(portugees) to the end of the list :",languages)

language_country = ["congoleese","dutch","philipinno","chineese"]
languages.extend(language_country)
print("languages after adding elements from Sanother list is " ,languages)
print("the length od the list is: ",len(languages))

languages.remove("congoleese")
print("languages after removing an item from the list is:",languages)
languages.pop(1)
print("languages after poping an  item :",languages)
print("and the lenght of the list is",len(languages))

#sorting the list
languages.sort()
print("languages after sorting in ascending order is :",languages)

languages.sort(reverse= True)
print("languages after sorting in descending order is: ",languages)

new_languages = languages.copy()
print("the new languages list after copying is: ",new_languages)

#looping through lists
for x in languages:
    print(x)
print("this are the items in the list:")
[print(x) for x in languages]