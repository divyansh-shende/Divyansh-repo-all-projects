students = [
    {"name": "Asha", "grades": [85, 90, 78]},
    {"name": "Ravi", "grades": [70, 65, 80]},
    {"name": "Priya", "grades": [95, 92, 88]},
]

for student in students:
    average = sum(student["grades"]) / len(student["grades"])
    print(student["name"], "Average:", average)