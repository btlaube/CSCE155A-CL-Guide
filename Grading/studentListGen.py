
def createstudentlist():
    # Specify the CSV file path
    csv_file_path = 'students.csv'

    # Specify the text file path to save the output
    txt_file_path = 'students.txt'

    lines = []
    # Open the CSV file in 'read' mode
    with open(csv_file_path, 'r') as csv_file:
        #iterate through the csv file
        for line_number, line in enumerate(csv_file):
            # Skip the first line (line_number == 0)
            if line_number == 0:
                continue
            # Process each line as needed and add to the list
            lines.append(line.split("\"")[1] + '\n')

    # Sort the list of lines alphabetically
    # lines.sort()
    lines = sorted(lines, key=lambda x: x.split()[0])

    # Restructure list elements from (Lastname, Firstname) to (firstname Lastname)
    new_lines = []
    for line in lines:
        split_line = line.strip().split(',')
        line = split_line[1] + ' ' + split_line[0] + '\n'
        new_lines.append(line)

    # Write the sorted and restructureed names to the text file
    with open(txt_file_path, 'w') as txt_file:
        txt_file.writelines(new_lines)


def main():
    createstudentlist()

if __name__ == '__main__':
    main()