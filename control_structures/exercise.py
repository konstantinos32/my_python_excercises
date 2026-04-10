number=0
if number>0:
    print("The number is positive")
elif number<0:
    print("The number is negative")
else:
    print("The number is zero")

grade=100

if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
else:    print("F")


age=12
status="minor" if age<18 else "adult"
print(status)

vehicles=["ferrari","lamborghini","porsche"]
for vehicle in vehicles:
    print(f"{vehicle} is a luxury car")

    for num in range(1,11):
        if num % 2 !=0:
            continue
        print(num)


total=0
num=1

while num in range(1,101):
    total += num
    num += 1
print(total)

words = ["cat", "apples", "grape", "chair"]

for word in words:
    if len(word) > 5:
        print("Word with more than 5 letters:", word)
        break
else:
    print("All words are not bigger than 5 letters.")


people = ["Alice", "Bob", "Charlie", "David"]
pets=["cat", "dog", "hamster", "parrot"]

for person in people:
    for pet in pets:
        print(f"{person} has a {pet}")


food=["pizza", "sushi", "burger", "salad"]
for item in food:
    if item=="sushi":
        print("I love sushi!")
        break
else:
    print("item not found in the list.")


fruits=["apple","carrot","banana", "orange", "grape"]
vegies=["carrot", "broccoli", "spinach", "pepper"]
meat=["chicken", "beef", "pork", "fish"]

item="carrot"

match item:
    case _ if item in fruits:
        print(f"{item} is a fruit.")
    case _ if item in vegies:
        print(f"{item} is a vegetable.")
    case _ if item in meat:
        print(f"{item} is a meat.")
    case _:
            print(f"{item} is not found in any category.")