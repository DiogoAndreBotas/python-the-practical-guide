#1 Create two variables – one with your name and one with your age
#2 Create a function which prints your data as one string
#3 Create a function which prints ANY data (two arguments) as one string
#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)

def print_name_and_age(name, age):
    print(f"Name: {name} ; Age: {age} years ; Decades lived: {calculate_decades_lived(age)}")

def print_data(first, second):
    print(f"First: {first} ; Second: {second}")

def calculate_decades_lived(age):
    return int(age / 10)

name = input('Provide your name: ')
age = int(input('Provide your age: '))

print_name_and_age(name, age)
print_data(name, age)
