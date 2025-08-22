class SRU_Student:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department

    def Student_Data(self, filename="student_data.txt"):
        with open(filename, "a") as file:
            file.write(f"Name: {self.name}, Roll No: {self.roll_no}, Department: {self.department}\n")
        print("Student data saved to", filename)

if __name__ == "__main__":
    print("SRU_Student class initialization")
    while True:
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        department = input("Enter department: ")
        student = SRU_Student(name, roll_no, department)
        print("Student_Data")
        student.Student_Data()
        cont = input("Add another student? (y/n): ")
        if cont.lower() != 'y':
            break