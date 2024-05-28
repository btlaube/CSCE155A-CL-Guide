# How to be a Course Leader for CSCE 155A


## A somewhat comprehensive guide compiled and written by Ben Laube

May 29, 2024


# MOSS

Moss (for a Measure Of Software Similarity) is an automatic system for determining the similarity of programs. To date, the main application of Moss has been in detecting plagiarism in programming classes.

As CL you will be asked to use Moss to detect plagiarism in student submissions. You will need to understand Moss well enough to use it as well as to explain what it is, how it works, and why we use it to the 155A students. You will be asked to present this information to the class around week 5. A past CL, Jacob Harvey, provided a GitHub repository with notes on what to cover during this presentation including how Moss works, what counts as cheating, and what students should do if they have been flagged for academic dishonesty (Harvey, 2022). Additionally, you can find a link to a Google Slides presentation based on Harvey’s notes below, that can be used as a visual aid during your Moss presentation. 


## Setup

For the setup of Moss, find the “Registering For Moss” section at the following link: [https://theory.stanford.edu/~aiken/moss/](https://theory.stanford.edu/~aiken/moss/)  

From the above link, to register an account:



1. Send an email to "[moss@moss.stanford.edu](mailto:moss@moss.stanford.edu)"
2. The body of the email must following the following format:

       registeruser
       mail _username@domain_

4. Replace the end portion with your email address.
5. Once you have an account, download the moss script at the following link: [http://moss.stanford.edu/general/scripts.html](http://moss.stanford.edu/general/scripts.html) 


## Using Moss

Once you have registered a Moss account, you will need to prepare student code to be submitted to the Moss system. To do this, you can download all student submissions from the particular assignment’s Canvas page. Find the “Download Submissions” button to download a .zip file with all student submissions that you will extract.

Downloading assignment submissions from Canvas will rename all files with the students’ names; however, further formatting can be done to make Moss easier to use. 

You will find a script, cleaner.sh, that will restructure a folder of files, on the GitHub repository at this link: [https://github.com/btlaube/CSCE155A-CL-Guide/tree/main/MOSS](https://github.com/btlaube/CSCE155A-CL-Guide/tree/main/MOSS) 

To use it, download all the submissions and unzip them, then run:

    ./cleaner.sh [dir of student files]​	 

**CAUTION**: This script has no save guards and moves files around, so do not use it on the wrong directory. 

For safety, before running the shell script, run: 

    chmod +x cleaner.sh​

And after run: 

    chmod -x cleaner.sh

Also, it may print a lot of error messages to the terminal, but it still works, the original issues were never ironed out.

Finally, you will run Moss using:

    moss -l python -d [cleaned dir of student files]/*/*


## Presentation

As Course Leader, you may be asked to present a Moss lecture to the class. You should meet with the instructor(s) to select a lecture period (likely around week 5) during which you will present. 

Below are a few resources for this presentation, provided by past and current CSCE 155A Course Leaders.



* This GitHub repo provides a brief outline of the Moss system as well as a rundown of the UNL SoC academic dishonesty policy: [https://github.com/jharvey25/Moss-Overview](https://github.com/jharvey25/Moss-Overview) 
* Need a visual aid? Use this Google Slides presentation based on information from the repository above: [https://docs.google.com/presentation/d/1g5CqBktnBTmgtoj7Ogii5BYBJvKvWCXqhAX-9kIosrA/edit?usp=sharing](https://docs.google.com/presentation/d/1g5CqBktnBTmgtoj7Ogii5BYBJvKvWCXqhAX-9kIosrA/edit?usp=sharing) 


## Template Cheating Message

After discussing the Moss results with the instructor(s), the CL must notify each student that has been flagged for academic dishonesty. This can be done via Canvas by setting the student’s grade to 0 for the assignment and leaving a modified version of the following boilerplate comment:

“This submission has been flagged for violating the Academic Integrity Policy of the School of Computing due to its resemblance to one or more student submissions or code available online.

A grade of 0/XX has been assigned to this submission. If you feel that this decision was made in error, please contact an instructor before DATE (XX/XX) @ 11:59 PM to discuss your concerns.”


# Grading

You will be responsible for determining how to distribute the grading amongst the Learning Assistants. Additionally, you must decide whether or not to include yourself in the distribution. Ideally you will have time to grade and hold office hours; however, you may need to choose one or the other. For Course Leaders, I personally recommend prioritizing grading, and forgoing office hours if you must.

You should make a grading distribution roughly once a week covering all assignments that were due that week. Code to automatically generate a distribution of graders and students can be found below. Additionally, you will notify the 155A Learning Assistant via Slack which students they should grade for which assignments. A template message to send with a grading distribution can be found below.


## Distribution

The code I used to generate grading distributions is hosted on a GitHub at this link: [https://github.com/btlaube/CSCE155A-CL-Guide/tree/main/Grading](https://github.com/btlaube/CSCE155A-CL-Guide/tree/main/Grading) 


## Template Grading Message

This template message informs LAs which assignment(s) will be graded and when they should have their grading completed. It includes an example of how the assignment should be graded, instructing students to use the rubric on the assignment page. Note that this may need to be modified as not all assignments have rubrics at the time of writing. Finally, LAs are informed to leave a comment for each student with information about the grading. 

The message is as follows: 
"Hey @channel we are grading ASSIGNMENT. Everyone should finish their portion of the grading by Tuesday (DATE) at 11:59pm. If you cannot make this deadline, then please reach out. And if someone else reaches out, then feel free to help!

We will all use the rubric on the assignment page to grade. Follow it as closely as you can, and if anything seems ambiguous (or if you have any other questions), then reach out.

For each student, leave a comment with your name, an email for students to send questions about their grade, and a short explanation of any points you may have deducted. Also, be sure to give positive feedback for the student’s good work!"


## Quality Check

Before posting grades, you will need to QC. Once the LAs have completed the grading you assigned, you will run Moss (see the section of Moss above), make sure the LAs left good comments, and correct any mistakes you notice. After you have finished QC, you will post grades for students to see.
