from random import randint as rand
import os
import datetime
def fileExists(file):
    if(os.path.isfile(file)):
        return True
    else:
        return False

def intCheck(value):
    if(value != '0' and value != 0):
        try:
            value = int(value)
            return value
        except:
            return False
    else:
        return int(value)

def organise(file):
    fi = open(file,"r")
    alldata = []
    i = 0
    for line in fi:
        if(i > 0):
            exam = {}
            row = line.split(",")
            exam["subject"] = row[0]
            exam["paper"] = row[1]
            exam["date"] = row[2]
            exam["priority"] = row[3]
            exam["topics"] = row[4].replace("\n","").split("/")
            alldata.append(exam)
        i += 1
    fi.close()
    return alldata

def subcollector(exams):
    subjects = []
    for exam in exams:
        if(exam["subject"] not in subjects):
            subjects.append(exam["subject"])
    return subjects
def timetabler(exams,th,totalhours,firstday,lastexam):                 # 'th' is topics/hours
    i = datetime.datetime.strptime(firstday,"%Y-%m-%d").toordinal()         # Ordinal number of the first day of hardcore revision
    lastexam = datetime.datetime.strptime(lastexam,"%Y-%m-%d").toordinal()      # Ordinal number of the last day of hardcore revision
    while (i < lastexam):
        day = datetime.datetime.strftime(datetime.date.fromordinal(i),"%d/%m/%Y")   # Set day to the date of the current iteration
        todelete = []                                                               # Remove exams where the date is already set
        for exam in exams:
            if(i >= datetime.datetime.strptime(exam["date"],"%d/%m/%Y").toordinal()):
                todelete.append(exam)
        for exam in todelete:
            exams.remove(exam)

        subjects = subcollector(exams)
        
        prioritotal = [0]
        total = 0
        for exam in exams:
            total += int(exam["priority"])
            prioritotal.append(total)
            
        j = 1
        revision = []
        if(th == "topics"):
            revisionsubs = []
            revisiontops = []
            while j <= totalhours:
                randnum = rand(0,prioritotal[-1])
                for k in range(len(prioritotal)-1):
                    if(prioritotal[k] < randnum and randnum <= prioritotal[k+1]):
                        exam = exams[k]
                        if((exam["subject"] not in revisionsubs and j <= len(subjects)) or (exam["subject"] in revisionsubs and j > len(subjects))):
                            topic = exam["topics"][rand(0,len(exam["topics"])-1)]
                            revisionsubs.append(exam["subject"])
                            revisiontops.append(topic)
                            revision.append(exam["subject"]+": "+topic)
                            j += 1
        if(th == "hours"):
            while j <= totalhours:
                randnum = rand(0,prioritotal[-1])
                for k in range(len(prioritotal)-1):
                    if(prioritotal[k] < randnum and randnum <= prioritotal[k+1]):
                        exam = exams[k]
                        if((exam["subject"] not in revision and j <= len(subjects)) or (exam["subject"] in revision and j > len(subjects))):
                            revision.append(exam["subject"])
                            j += 1
        day = datetime.datetime.strftime(datetime.date.fromordinal(i),"%a %d/%m/%y")
        string = (day+","+",".join(revision))
        f = open("TIMETABLE.csv","a")
        f.write(string+"\n")
        f.close()
        i += 1
    print(exams)

while True:
    f = input("Enter the file to read from\n>> ")
    while(fileExists(f) == False):
        f = input("Please enter a valid file\n>> ")
    
    choice = input("Would you rather do set topics or set hours every day?\n>> ")
    choices = ["topics","hours"]
    while choice not in choices:
        choice = input("Please only enter 'topics' or 'hours'")

    hours = intCheck(input("Enter how many "+choice+" you want to do every day\n>> "))
    while intCheck(hours) == False:
        hours = intCheck(input("Please enter an integer value\n>> "))
    firstday = input("Enter the date of the first day you plan to revise in the form of yyyy-mm-dd\n")
    lastexam = input("Enter the last day of your exams in the form of yyyy-mm-dd\n")
    timetabler(organise("EXAMS.csv"),choice,hours,firstday,lastexam)
