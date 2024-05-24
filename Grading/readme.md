To use this grading distrubution generator, you will need a few things
1. graders.txt: a text file with the names of each grader you wish to include in the distrubiution (one name per line, no punctuation).
    a. The order graders appear in this fill will match the order in the generated output.
2. students.csv: a csv file with information on all students in the course.
    a. This file can be downloaded from Canvas on the "New Analytics" page.

Once you have created graders.txt and downloaded students.csv, simply executing gradingDistGen.py will generate a formated text file, gradingDist.txt, with an even distribution that accounts for an uneven ratio of students to graders, while maintaining a rotating order of graders. 
The program starts by importing studentListGen.py, and exectuing its createstudentlist() function that generates a formated text file of student names based on the downloaded file, students.csv.
Next the number of students per grader is calculated from the number of students and graders, accounting for an uneven ratio.
The distrubution is formatted and printed to the output file, gradingDist.txt
Finally, the program updates graders.txt with the grading order that will be used for the next generated distribution.