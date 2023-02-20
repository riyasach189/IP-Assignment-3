#COMPLETED

"""
Goal is to develop an application for grading in courses at IIIT-Delhi. The application should 
provide for (i) creating a course for grading with its name, credits, list of assessments with 
percentage  weight for each (e.g. [("quiz", 5), ("mid-sem", 15), …], a grading policy as a list 
percent for different grades (we will assume that only grades are: A, B, C, D, and F, so this 
can be [80, 65, 50, 40, 30] (i.e. A above 80, B between 80 and 65, …, F below 30). However, the 
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

Write this program without using classes and objects. (You may find dictionaries as suitable 
data structure.) Do the same problem without using oop.
"""
#If highest consecutive difference occurs more than once, this code considers the last one for calculating cutoff

import time

marks = dict()
grades = dict()
grading_summ = dict()

with open("student_marks.txt", "r") as file:
    temp = file.readlines()

for stu in range(len(temp)):
    temp[stu] = temp[stu].replace("\n", "")
    temp[stu] = temp[stu].split(",")
    marks[temp[stu][0]] = marks.get(temp[stu][0], ([float(k) for k in temp[stu][1:]]))


def cutoff(grading_policy, marks):
    for i in grading_policy:
        if i!="F":
            cutoff_range = list()
            max_diff = 0
            new_cutoff = grading_policy[i]

            for j in marks:
                if grading_policy[i]-2<=sum(marks[j])<=grading_policy[i]+2:
                    cutoff_range.append(sum(marks[j]))

            cutoff_range.sort()

            for j in range(len(cutoff_range)-1):
                if abs(cutoff_range[j+1]-cutoff_range[j])>=max_diff:
                    max_diff = abs(cutoff_range[j+1]-cutoff_range[j])
                    new_cutoff = (cutoff_range[j+1]+cutoff_range[j])/2

            grading_policy[i] = new_cutoff

    return grading_policy


def grading(grading_policy,marks,grades):

    for j in marks:
        for i in grading_policy:
            if sum(marks[j])>=grading_policy[i]:
                grades[j] = grades.get(j,i)
                break

    return grades


def grading_summary(grades):

    grading_summ = dict()

    for i in grades:
        grading_summ[grades[i]] = grading_summ.get(grades[i], 0) + 1

    return grading_summ


course_name = "IP"
credits = 4
assessments = [("Labs", 30), ("Midsem", 15), ("Assignments", 30), ("Endsem", 25)]
grading_policy = {"A": 80, "B": 65, "C": 50, "D": 40, "F": 0}

grading_policy = cutoff(grading_policy,marks)
grades = grading(grading_policy,marks, grades)
grading_summ = grading_summary(grades)

while(True):
# for t in range(100):

    start_time = time.time()

    try:
        # query = 2
        query = int(input("\n1 to generate course summary\n2 to write final record in file student_grades.txt\n3 to search for student record\nAnything else to exit\n"))
    except:
        break

    if query==1:
        print(f"Course Name: {course_name}\nCredits: {credits}\nAssessments: {assessments}\nGrading Policy:{grading_policy}\nGrading Summary: {grading_summ}")

    elif query==2:
        with open("student_grades.txt", "w") as f:
            for i in marks:

                f.write(f"{i}, {sum(marks[i])}, {grades[i]}\n")

    elif query==3:
        stu_query = input("Roll no.: ")

        # with open("q4&5 test.txt", "r") as test:
        #     test = test.readlines()

        # for entry in test:
        #     stu_query = entry.replace("\n","")

        if stu_query in marks:
            print(f"\nRoll No.: {stu_query}\nMarks: {marks[stu_query]}\nTotal Marks: {sum(marks[stu_query])}\nGrade: {grades[stu_query]}")
        else:
            print("Record does not exist.")

    else:
        break


    # with open("q5_query2_runtimes.txt","a") as f:
    #     f.write("%s\n" % (time.time() - start_time))


