student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}
print(student)
print(student["name"])  # Output: Alice

student["grade"] = "A"  # Adds a new key-value pair
student["age"] = 23     # Updates the value for the key 'age'
print("-------")
print(student)
del student["major"]     # Removes the key 'major'
student.pop("grade")     # Removes 'grade' and returns its value

for key in student:
    print(key, student[key])
# or
for key, value in student.items():
    print(key, value)

students = {
    "Alice": {"age": 22, "major": "CS"},
    "Bob": {"age": 24, "major": "Math"}
}

fruits = {"apple", "banana", "cherry",}
print("the of fruits is:", type(fruits))

print(fruits)

fruits.add("orange")

empty_set = set()  # NOT empty_set = {} (which creates an empty dictionary)

fruits.remove("banana")  # Raises error if not found
fruits.discard("banana") # Does not raise error if not found

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Output: {1, 2, 3, 4, 5}
print(a & b)  # Output: {3}
print(a - b)  # Output: {1, 2}
print(a ^ b)  # Output: {1, 2, 4, 5}

print("apple" in fruits)  # True or False

for fruit in fruits:
    print(fruit)
