list1 = [1,22,4,66,7,88,99,65,44,3,22,15,87,99]
counter = 0
num_to_check: int = 99
for number in list1:
    if number == num_to_check:
        counter += 1
        print(f"the number {number} appears {counter} times")


list1.pop()
print(list1)

list1.remove(99)
print(list1)

print("99 in list", 5 in list1)

list1.append(1)
print(list1)

while 99 in list1:
    list1.remove(99)
print(list1)





# input names from the user and append to a list
# if the name already exist in the list then do NOT append (continue)
# if the given name was 'exit' then ==> break

#לעשות רשימה של שמות, המשתמש יוסיף כל פעם את השמות לרשימה וכשירצה לצאת יכתוב EXIT, אם המשתמש יוסיף שם שכבר קיים ברשימה יש להתעלם

list_names: list[str] = []
while True:
    name: str = input("enter a mane: ")
    if name == "exit":
            break
    if name in list_names:
        continue
    list_names.append(name)
print(list_names)


#
list_names = []
while True:
    name: str = input('whats your name?')
    if name == 'exit':
        break
    if name in list_names:
        print(f"we already have a {name}")
        continue
    list_names.append(name)
print(list_names)
