fruits={"apple","banana","orange","grape","kiwi"}
print(fruits)

if "banana" in fruits:
    print("banana is in the set!")

    if "watermelon" in fruits:
        print("watermelon is in the set!")
    else:
        print("watermelon is not in the set!")

        fruits.add("watermelon")
        print(fruits)

        more_fruits = {"pear","peach","strawberry"}
        fruits.update(more_fruits)
        print(fruits)  

        fruits.remove("watermelon")
        print(fruits)
        fruits.discard("watermelon")
        print(fruits) 
        fruits.pop()
        print(fruits)
        fruits.clear()
        print(fruits)