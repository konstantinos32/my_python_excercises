favorite_food =["Gyros", "Pizza", "Souvlaki", "Pasta", "Salad"]
print(favorite_food)

print(favorite_food[0])
print(favorite_food[4])
print(favorite_food[-2])
print(favorite_food[1:3])

if "Pizza"  in favorite_food:
    print("Pizza is one of my favorite foods!")

favorite_food.append("Ice Cream")
print(favorite_food)
favorite_food.insert(2, "Tacos")
print(favorite_food)
tuple_test=("", 10)
print(type(tuple_test))
