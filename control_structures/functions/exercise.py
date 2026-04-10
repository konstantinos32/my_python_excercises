#1

numbers = [1, 2, 3, 4, 5]

def sum_list(numbers):
    total=0
    for num in numbers:
        total +=num
    return total
print(sum_list(numbers))

#2

def repeat_greeting(name, times):
    for _ in range(times):
        print(f"Hello, {name}!")

repeat_greeting("kostas", 3)

#3

def factrorial(n):
    result =1
    for num in range(1, n+1):
        result *=num
    return result
print(factrorial(5))

#4
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(10))

def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b
print(max_of_two(1, 4))

#6
def print_triangle(rows):
    for i in range(1, rows + 1):
        row = ""
        for j in range(i):
            row = row + "*"
        print(row)

print_triangle(5)