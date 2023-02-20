#COMPLETED

"""
Goal is to develop an application for grading in courses at IIIT-Delhi. The application should 
provide for (i) creating a course for grading with its name, credits, list of assessments with 
percentage  weight for each (e.g. [("quiz", 5), ("mid-sem", 15), …], a grading policy as a list 
percent for different grades (we will assume that only grades are: A, B, C, D, and F, so this 
can be [80, 65, 50, 40] (i.e. A above 80, B between 80 and 65, …, F below 30). However, the 
final cutoff for each grade will be within +/- 2 of the percent specified (i.e. for A it will be 
between 78 and 82) - it will be the higher of two consecutive marks within this range which have 
the highest difference. (So, if the marks are 81.9, 81.8, 81.7, 81, 80.9, 80.8…, then the cutoff 
will be midpoint of 81.7 and 81, which has a largest gap  (ii) adding students' marks for all 
assessments given in a file - these will be rollno followed by marks for each.  Once marks are 
given, it should do the grading - apply the policy to determine the grade for each student. 

It should then ask the professor what he wants to do: 1. Generate a summary - which should print 
the course info (name, credits), assessments and their weight, cutoffs for different grades, and 
grading summary (how many As, how many Bs, etc) 2. Print the grades of all the students in a 
file as: rollno, total marks, grade (one line for each student). 3. Search for a student 
record - given the roll no, show marks in different assessments, total marks, and final grade.

Develop this program and use it for grading the "IP" course. The assessments and the grading policy 
is given below (in the main program steps)

The main program can be something like (rough sketch):

1.cname, credits = "IP", 4
2.assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
3.policy = [80, 65, 50, 40, 30]
4.create-IP course (cname, credits, assessments, policy)
5.Upload-marks data - call a function/method with input as marks.txt
6.doGrading - call a function/method 
7.Loop asking for what operation (1, 2, 3); perform the operation till no input given

Write this program using class and objects - it seems that "Course" and "Student" will be 
natural classes. Write this program using classes and objects. You must have at least two main 
classes for course and student.
"""

#If highest consecutive difference occurs more than once, this code considers the last one for calculating cutoff

import time

class Course:
    def __init__(self, course, credits, assessments, grading_policy):
        self.course = course
        self.credits = credits
        self.assessments = assessments
        self.grading_policy = grading_policy
        self.grading_summary = dict()

    def cutoff(self,records):
        for i in self.grading_policy:
            if i!="F":
                cutoff_range = list()
                max_diff = 0
                new_cutoff = self.grading_policy[i]

                for j in records:
                    if self.grading_policy[i]-2<=j.total_marks<=self.grading_policy[i]+2:
                        cutoff_range.append(j.total_marks)

                cutoff_range.sort()

                for j in range(len(cutoff_range)-1):
                    if abs(cutoff_range[j+1]-cutoff_range[j])>=max_diff:
                        max_diff = abs(cutoff_range[j+1]-cutoff_range[j])
                        new_cutoff = (cutoff_range[j+1]+cutoff_range[j])/2

                self.grading_policy[i] = new_cutoff

        return None

    def grading_summ(self,records):
        # course.cutoff(records)

        for i in records:
            i.grading(course)

            course.grading_summary[i.grade] = course.grading_summary.get(i.grade, 0) + 1

        return None

    def __str__(self):
        # course.cutoff(records)
        # course.grading_summ(records)
        return f"Course Name: {self.course}\nCredits: {self.credits}\nAssessments: {self.assessments}\nGrading Policy:{self.grading_policy}\nGrading Summary: {self.grading_summary}"

class Student:
    def __init__(self, rollno, marks):
        self.rollno = rollno
        self.marks = marks
        self.total_marks = sum(marks)
        self.grade = ""

    def grading(self, course):
        # course.cutoff(records)

        for i in course.grading_policy:
            if self.total_marks>=course.grading_policy[i]:
                self.grade = i
                break

        return None

    def __str__(self):
        # self.grading(course)
        return f"\nRoll No.: {self.rollno}\nMarks: {self.marks}\nTotal Marks: {self.total_marks}\nGrade: {self.grade}"

course = Course("IP", 4, [("Labs", 30), ("Midsem", 15), ("Assignments", 30), ("Endsem", 25)], {"A": 80, "B": 65, "C": 50, "D": 40, "F": 0})

with open("student_marks.txt", "r") as file:
    records = file.readlines()

for stu in range(len(records)):
    records[stu] = records[stu].replace("\n", "")
    records[stu] = records[stu].split(",")
    records[stu] = Student(records[stu][0], [float(k) for k in records[stu][1:]])

course.cutoff(records)

for stu in records:
    stu.grading(course)

course.grading_summ(records)

while(True):

# for t in range(100):

    start_time = time.time()

    try:
        # query = 2
        query = int(input("\n1 to generate course summary\n2 to write final record in file student_grades.txt\n3 to search for student record\nAnything else to exit\n"))
    except:
        break

    if query==1:
        print(course)

    elif query==2:
        with open("student_grades.txt", "w") as f:
            for i in records:
                i.grading(course)
                f.write(f"{i.rollno}, {i.total_marks}, {i.grade}\n")

    elif query==3:
        stu_query = input("Roll no.: ")
        # with open("q4&5 test.txt", "r") as test:
        #     test = test.readlines()

        # for entry in test:
        #     stu_query = entry.replace("\n","")
        try:
            for i in records:
                if i.rollno==stu_query:
                    print(i)
                    break
            else:
                print("\nRecord does not exist.")

        except:
            print("Record does not exist.")

    else:
        break

    # with open("q4_query2_runtimes.txt","a") as f:
    #     f.write("%s\n" % (time.time() - start_time))