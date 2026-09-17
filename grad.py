class student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")

    def average(self):
        average = sum(self.marks)/len(self.marks)
        print(average)

student1 = student("Ug", 265084, "History", [0])
student2 = student("James", 5, "Quantum Science", [100])

student1.display()
student1.average()
student2.display()
student2.average()