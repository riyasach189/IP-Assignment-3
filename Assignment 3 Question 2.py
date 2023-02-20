#COMPLETED

"""
For IIIT-D students living off-campus (we have used IP TA names for this), suppose records of 
whenever a student enters or exits the campus are maintained in a data file. A typical data entry will 
look like this: "Student_Name, Crossing (can be ENTER or EXIT), Gate-number, Time (in 24 hr format)”

If in the record, a student is shown to enter even if he had previously entered the campus, i.e., 
two ENTER entries before EXIT, take the first one. Similarly, there can be two consecutive EXIT 
entries from the campus for a student - if so, take the last one. You are given the data for one day 
(A sample data file can be downloaded from File). If for a student there is EXIT but there is no ENTRY -
it means he/she came the day before; similarly if ENTRY but no EXIT, it means that the student will 
leave next day. To avoid special situations, it is best if you first sort this data w.r.t time.

Convert this data into a nested dictionary. The keys should be the name and value should be another 
dictionary containing a list of gate no, crossing type, time. Use this dictionary to answer the 
following queries (for querying, you can write a small loop and ask for a number between 1 and 3 - 
nothing given can be the end).

1) Given a student name (as input), show the record of student moving in/out of campus (as a list of tuples)
in the day (in a output text file), and whether currently present in campus or not. Take another input 
for current time as well.

2) Given the start time and the end time (in 24hr format, both inclusive) as input, determine all
the students who entered the campus during this, and all students who exited the campus during this time.
Save the result into an output text file, with the format similar as the input data file.

3) Given the gate number (as input), determine the number of times students have entered the campus 
through that gate, and the number of times students have exited the campus from that gate. 
"""

#This code only works if name of student is in the record.

records = dict()

with open("sorted_data.txt", "r") as data:
    temp = data.readlines()

for i in range(1,len(temp)):
    temp[i] = temp[i].replace("\n","")
    temp[i] = temp[i].split(", ")
    details = {"crossing": temp[i][1], "gate_no": int(temp[i][2]), "time_as_list":[int(num) for num in temp[i][3].split(":")], "time": temp[i][3]}
    records[temp[i][0]] = records.get(temp[i][0], []) + [details]

while(True):
    try:
        query = int(input("1 to print student record\n2 to print record of time duration\n3 to print gate record\nAnything else to exit\n"))

    except:
        break

    if query==1:
        student = input("Enter name: ")
        current_time = list(map(int,input("Current time: ").split(":")))
        time_in_sec = current_time[0]*3600 + current_time[1]*60 + current_time[2]
        status = ""
        output = []

        for i in records:
            if i==student:
                for j in records[i]:
                
                    output.append((j["crossing"], j["gate_no"], j["time"]))

                    temp = j["time_as_list"][0]*3600 + j["time_as_list"][1]*60 + j["time_as_list"][2]

                    if temp<=time_in_sec:
                        status = j["crossing"]

        if status=="ENTER":
            status = ("\nStudent is inside the campus.")

        elif status=="EXIT":
            status = ("\nStudent is not inside the campus.")
        
        elif status=="":
            for i in records:
                if i==student:
                    status = records[i][0]["crossing"]

            if status=="ENTER":
                status = ("\nStudent is not inside the campus.")
            else:
                status = ("\nStudent is inside the campus.")

        with open("q2_query1.txt","w") as file:
            for i in output:
                file.write(f"{i}\n")

            file.write(status)

    elif query==2:
        start_time = list(map(int,input("Start time: ").split(":")))
        end_time = list(map(int,input("End time: ").split(":")))

        start_time = start_time[0]*3600 + start_time[1]*60 + start_time[2]
        end_time = end_time[0]*3600 + end_time[1]*60 + end_time[2]

        output = ["TA, Crossing, Gate number, Time"]

        for i in records:
                for j in records[i]:

                    temp = j["time_as_list"][0]*3600 + j["time_as_list"][1]*60 + j["time_as_list"][2]

                    if start_time<=temp<=end_time:
                    
                        output.append(f"\n{i}, {j['crossing']}, {j['gate_no']}, {j['time']}")

        with open("q2_query2.txt","w") as file:
            for m in output:
                file.write(f"{m}")

    elif query==3:
        enter = 0
        exit = 0
        gate_no = int(input("Gate No.: "))
        for i in records:
            for j in records[i]:
                if j["gate_no"]==gate_no:
                    if j["crossing"]=="ENTER":
                        enter+=1
                    else:
                        exit+=1

        print(f"Entry: {enter}")
        print(f"Exit: {exit}")        

    else:
        break