This Project is to make the Examinations better by allotting the student in a way that no students 
of the same class sit next to each other

**Requirements to run the program:**
1. python3 pre-installed 
2. pyQt5 pre-installed - if not installed, open the terminal/cmd and run  

   `pip install pyQt5`

3. Can be run only in linux and Windows environment


**Resource requirements are :**

1. Database of all the students in sqlite database
   
   The **create** statement of the table should be like

    ` 
   CREATE TABLE "student" (
    "rollno"	text,
    "name"	text,
    "class"	text,
    PRIMARY KEY("rollno")
)`
2. list of all the exam Halls - sorted by the order it needs to be you need the output
3. list of classes - sorted by the subjects, having the largest group on top of the list.

**To execute the program, run**

    python3 main.py

    