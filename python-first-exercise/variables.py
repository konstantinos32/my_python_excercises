
#Variables 
name="Kostas"
age=45
height=1.87

#printing the variables and checking their types
print(name, type(name))
print(age, type(age))
print(height, type(height))

#Type casting
age_str = str(age)
print(age_str, type(age_str))
print(age, type(age))

print("My name is " + name + " and I am " + age_str + " years old.")


# Global variable
global_message = "Hello, world!"

def update_message():
    global global_message  # tell Python we mean the global variable
    global_message = "Hello from inside the function!"

# Before calling the function
print("Before:", global_message)

# Call the function
update_message()

# After calling the function
print("After:", global_message)

#strings exercise
first_name="Kostas"
last_name="Theodoropoulos"
bio="I am motivated to learn Python and become a software developer. Let us hope this print at the terminal"

print(first_name[0])
print(last_name[-1])
print(bio[slice(0, 10)])

for letter in first_name:
    print(letter)

    print("Length of bio:", len(bio))

    if "Python" in bio:
        print("The word 'Python' is in the bio.")

        if "Java" not in bio:
            print("The word 'Java' is not in the bio.")

            print("Uppercase in first name:", first_name.upper())
            print("Lowercase in last name:", last_name.lower())

            full_name= first_name + " " + last_name
            print("Full name:", full_name)

            message=f"Hello, my name is {full_name} and I love Python!"

            print(message)

            new_message = "My full name is {} and I am {} years old."

           
            print(new_message.format(full_name, age))


bio_centered= bio.center(50)
print(bio_centered)

counting_letters=full_name.count("a")
print("Number of 'a' in full name:", counting_letters)

#operators exercise
a=15
b=4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)