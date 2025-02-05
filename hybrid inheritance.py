class University:
    def __init__(self, name):
        self.name = name

    def showDetails(self):
        print(f"This is the detail about university: {self.name}")

class Course(University):
    def __init__(self, namecourse, nameUni):
        self.namecourse = namecourse
        super().__init__(self,nameUni)  # Calls University constructor

    def showDetails(self):
        print(f"This is the detail about course: {self.namecourse}")
        super().showDetails()  # Calls University.showDetails()

class Branch(University):
    def __init__(self, namebra, nameUni):
        self.namebra = namebra
        super().__init__(nameUni)  # Calls University constructor

    def showDetails(self):
        print(f"This is the detail about branch: {self.namebra}")
        super().showDetails()  # Calls University.showDetails()

class Student(Course, Branch):
    def __init__(self, stuname, nameUni, namebra, namecourse):
        self.stuname = stuname
        super().__init__(namecourse, nameUni)  # Calls Course → University (through MRO)
        Branch.__init__(self, namebra, nameUni)  # Explicitly initialize Branch after Course

    def showDetails(self):
        print(f"This is the detail about student: {self.stuname}")
        super().showDetails()  # Calls Course.showDetails() → Branch.showDetails() → University.showDetails()

class Faculty(Branch):
    def __init__(self, namefc, namebra, nameUni):
        self.namefc = namefc
        super().__init__(namebra, nameUni)  # Calls Branch → University

    def showDetails(self):
        print(f"This is the detail about faculty: {self.namefc}")
        super().showDetails()  # Calls Branch.showDetails() → University.showDetails()

# Creating a Student object
print("\nCreating a Student object...")
student1 = Student("Alice", "Harvard", "Computer Science", "B.Tech")

print("\nDisplaying Student Details:")
student1.showDetails()

# Creating a Faculty object
print("\nCreating a Faculty object...")
faculty1 = Faculty("Dr. Smith", "Mathematics", "Harvard")

print("\nDisplaying Faculty Details:")
faculty1.showDetails()
