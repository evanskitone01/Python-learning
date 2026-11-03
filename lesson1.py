print("I am Evans Kitone")
print("I am learning Coding")
print("I want to become software Engineer")
name = "Evans"
age = 20
city = "Nairobi"
height = 1.75
is_learning = True
print(name)
print(age)
print(type(city))
print(type(age))
print(type(height))
a = 20
b = 4
print(a + b)
print(a - b)
print(a % b)
print(a / b)
print(a * b)
x = 10
y = 5
print(x > y)
print(x < y)
print(x == y)
print(x != y)
if age >= 18:
    print("you are an adult.")
else:
    print("you are under 18")
print(age >= 18 and age <=60)
print(age < 18 or age > 60)
print(not age < 18)
for number in range(1, 6):
    print(number)
number = 1
while number <= 5:
    print(number)
    number = number + 1
languages = ["Python", "Java", "Javascript", "c++"]
print(languages)
print(languages[0])
print(languages[1])
languages.append("HTML")
languages.remove("Java")
print(languages)
def introduce():
    print("Hey")
    print("I am learning software engineering")
introduce()
def introduce(name):
    print("Hey, " + name + "!")
introduce("Evans")
introduce("John")
introduce("mary")
def add_numbers(a, b):
    print(a + b)
add_numbers(10, 5)
def rectangle_area(length, width):
    return length * width
area = rectangle_area(8, 4)
print(area)
def hratio(big, small):
    return big / small
ratio = hratio(22, 7)
print(ratio)
def square(number):
    return number * number
ans = square(4)
print (ans)
student = {
    "name": "Evans",
    "age": 20,
    "course": "software engineering"
}
print(student["name"])
print(student["age"])
print(age + student["age"] + ratio)