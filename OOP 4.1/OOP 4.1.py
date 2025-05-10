import copy

students = ["Alice", "Bob", "Charlie", "Diana"]
print(id(students))

chemistry_students = students
print(id(chemistry_students))  # Same as id(students)

print(students == chemistry_students)  # True


print(students is chemistry_students)  # True

physics_students = students[:]  # Creates a copy of the list
print(id(physics_students))  # Different from id(students)

# Modifying the new reference
chemistry_students.append("Eve")
print(students)  # ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

# Modifying the copied list
physics_students.append("Frank")
print(students)  # ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
print(physics_students)  # ['Alice', 'Bob', 'Charlie', 'Diana', 'Frank']

shallow_copy = copy.copy(students)

deep_copy = copy.deepcopy(students)


# Deep copy on dictionaries
original_dict = {"key1": [1, 2, 3], "key2": "value"}
deep_copied_dict = copy.deepcopy(original_dict)

# Deep copy on class objects
class Student:
    def __init__(self, name):
        self.name = name

original_student = Student("Alice")
deep_copied_student = copy.deepcopy(original_student)