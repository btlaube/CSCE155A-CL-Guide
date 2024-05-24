import studentListGen

studentListGen.createstudentlist()

studentsFilePath = 'students.txt'
students = []
gradersFilePath = 'graders.txt'
graders = []
outputFilePath = 'gradingDist.txt'

# Read students file and remove newline characters
with open(studentsFilePath, 'r') as students_file:
    students = [line.strip() for line in students_file]

# Read graders file and remove newline characters
with open(gradersFilePath, 'r') as graders_file:
    graders = [line.strip() for line in graders_file]

num_graders = len(graders)
num_students = len(students)

print(f"{num_graders} graders, {num_students} students")
with open(outputFilePath, 'w') as output_file:
    output_file.write(f"{num_graders} graders, {num_students} students" + '\n')

    base_size = num_students // num_graders
    remainder = num_students % num_graders

    if remainder > 0:
        print(f"{base_size} or {base_size + 1} per grader")
        output_file.write(f"{base_size} or {base_size + 1} per grader" + '\n')
    else:
        print(f"{base_size} per grader")
        output_file.write(f"{base_size} per grader" + '\n')

    remainder_remaining = remainder
    student_index = 0
    for i in range(num_graders):
        num_grade = base_size
        if remainder_remaining > 0:
            num_grade += 1
            remainder_remaining -= 1

        print(f"===============================\n {graders[i]} ({num_grade} students) \n===============================")
        output_file.write(f"===============================\n {graders[i]} ({num_grade} students) \n===============================" + '\n')
        for j in range(num_grade):
            print(f"{j+1:<3} {students[student_index+j]}")
            output_file.write(f"{j+1:<3} {students[student_index+j]}" + '\n')

        student_index += num_grade


# Update grader order by shifting each grader, so each grader is assigned to grade every student eventually.
with open(gradersFilePath, 'w') as txt_file:
    txt_file.write(graders[len(graders)-1] + '\n')
    for i in graders[:len(graders)-1]:
        txt_file.write(i + '\n')