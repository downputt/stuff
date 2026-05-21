students = {
    "S001": {
        "Name:" : "Fish",
        "Age:" : 1000000,
        "Marks:" : {
            "Maths:" : 50,
            "English:" : 0,
            "Science:" : 60,
            "Sport:" : 0,
            "Swim:" : 100,
            "BlubBlub:" : 100

        }

    },

        "S002": {
        "Name:" : "Bug",
        "Age:" : "2 Days",
        "Marks:" : {
            "Maths:" : 0,
            "English:" : 0,
            "Science:" : 75,
            "Sport:" : 100,
            "Swim:" : 10,
            "BuzzBuzz:" : 100

        }

    },

    "S003": {
        "Name:" : "Dino",
        "Age:" : 5,
        "Marks:" : {
            "Maths:" : 5,
            "English:" : 0,
            "Science:" : 10,
            "Sport:" : 70,
            "Swim:" : 0,
            "Scare:" : 100

        }

    },

    "S004": {
        "Name:" : "Dog",
        "Age:" : 2,
        "Marks:" : {
            "Maths:" : 50,
            "English:" : 60,
            "Science:" : 0,
            "Sport:" : 100,
            "Swim:" : 68,
            "Bark:" : 95

        }

    }

}

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

for student_id, student_data in students.items():
    print("\n Student ID: " , student_id)
    print("Name: " , student_data["Name:"])
    print("Age: " , student_data["Age:"])
    print("Marks: ")
    for subject, score in student_data["Marks:"].items():
        print(" " , subject , score)

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")


for student_data in students.values():
    student_data["Marks:"]["English:"]+=5
print("\n Updated English Marks:")
for student_id,student_data in students.items():
    print(student_id,"-",student_data["Marks:"]["English:"])




print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
