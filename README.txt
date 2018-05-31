Welcome to the timetabler script!
==============
 REQUIREMENTS
==============

- Python 3.6 (or later)
- Recommended: Microsoft Excel
- 4 minutes to read through this file to make sure you do everything right.

==============
 INSTRUCTIONS
==============
------------------------------
 WHERE FILES SHOULD BE PLACED
------------------------------

The CSV file (see DATA FORMATTING) should be in the same folder/directory as
the Python script.

------------------
 DATA FORMATTING:
------------------

For this program to work, you should enter your exams in a CSV file.

If you don't know how to do this, you can either: 

Enter everything seperated
by commas in a notepad document, and then click File>Save As...>[File Name].csv (you'd
need to enable "Save as type: All files" first.

OR

You can open Microsoft Excel, enter all your data there, and save it as a CSV
(Comma Seperated Value) file.

Your exams in the format: subject, paper, data, priority, topics.
subject: Just the title of your chosen subject, e.g. English Literature, Physics, etc.
paper: The paper of the exam, e.g. in the subject French, a paper could be speaking, writing, reading, or listening
date: The date of the exam, written in the format dd/mm/yyyy
priority: You can write the priority of your exams, like this:
		3 - low priority
		6 - medium priority
		9 - high priority
	  No, I don't know why I chose 3,6,9, I genuinely forgot. But it works. So there.
topics: The topics that the exam (paper) assesses. For example, in Edexcel History Paper 2, the topics would be
	Anglo-Saxons/Superpower Relations.
	YOU MUST SEPERATE EACH TOPIC USING '/' WHEN WRITING THE FILE. THE PROGRAM
	CANNOT UNDERSTAND IT OTHERWISE
------------------------------------------------------------------------------------------------------------------------
**IMPORTANT**: The FIRST row should be the headers, as such: 'subject,paper,date,priority,topics'. It doesn't matter
what the names of each header are, as long as there are 5, they don't confuse you, and they are in the FIRST row.
If they aren't, then the first paper you have will be removed (the program removes the first line as it should normally
be the headers, which isn't an exam!). I accidentally made a typo in my exam headers, still works fine. Their only
importance is that they are there.
------------------------------------------------------------------------------------------------------------------------
For further guidance, please refer to the EXAMS.csv file in the 'EXAMPLE DATA' file to see how it should be laid out.
I recommend opening it with notepad.

What topics you separate into, and what subjects you put in, with whatever paper you put in, is
up to you, depending on your exam dates.

----------------------
 RUNNING THE PROGRAM:
----------------------

You need Python 3.6 or later installed to run this.
---
 1
---
'Enter the file to read from'. 
This is the name of the file you've stored all of your exams in.

For example, if your file is called 'EXAMS', you enter, 'EXAMS.csv' (the file extension, '.csv', must be entered).
If your file is called 'TheReasonForMySuffering', you enter, 'TheReasonForMySuffering.csv'.

---
 2
---
'Would you rather do set topics or set hours every day?'.
Enter 'topics' or 'hours'.
- Doing a set topic just means you have a goal of completing a particular unit in your course.
- Doing a set hour just means you have a fixed 1 hour period to complete revision on a subject. It's completely
  up to you what you do in this hour, but let it be related to the subject specified.

---
 3
---
'Enter how many [topics/hours] you want to do every day'
Depends how tough you are, really. This speaks for itself really, but just
do what works for YOU. I'd advise against doing 24 subjects a day because there's a high risk of death by fatigue.
Recommended: 5.
If you're REALLY feeling tough: 8.
Do what you like though.
---
 4
---
'Enter the date of the first day you plan to revise in the form of yyyy-mm-dd'
Don't really need to explain this. If you're starting on the 31st of May 2018, you type 2018-05-31.
If you're starting on the 5th of June 1943 (which, I HIGHLY doubt you are), you type 1943-06-05.
I'd speak against setting the year to be like 1943, because you will take up a LOT of space on your computer.
Additionally, you may break the script if you go earlier than 1901.
---
 5
---
'Enter the last day of your exams in the form of yyyy-mm-dd'
Over the summer I'm gonna remove this because this can be determined automatically, I was just lazy.
For now, do the same as above but for the last date of your exam.


It'll create a file called "TIMETABLE.csv", containing your timetable.
Do what you like with this, your life, I'm not controlling it.
====================================================================================================
Raphael Nash © 2018