def read_student(file):
    """Reads a student record from the file."""
    line = file.readline()
    if line:
        student_id, gpa = line.strip().split()
        return student_id, gpa
    return None, None

def merge_files(file1_name, file2_name):
    """Merges two student files and prints the sorted result."""
    with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2:
        student1_id, student1_gpa = read_student(file1)
        student2_id, student2_gpa = read_student(file2)

        while student1_id is not None or student2_id is not None:
            if student1_id is None:
                print(student2_id, student2_gpa)
                student2_id, student2_gpa = read_student(file2)
            elif student2_id is None:
                print(student1_id, student1_gpa)
                student1_id, student1_gpa = read_student(file1)
            else:
                # Compare the last two digits of the student IDs (faculty code)
                faculty1 = student1_id[-2:]
                faculty2 = student2_id[-2:]

                if faculty1 < faculty2:
                    print(student1_id, student1_gpa)
                    student1_id, student1_gpa = read_student(file1)
                elif faculty1 > faculty2:
                    print(student2_id, student2_gpa)
                    student2_id, student2_gpa = read_student(file2)
                else:
                    # If faculty codes are equal, compare the full student IDs
                    if student1_id < student2_id:
                        print(student1_id, student1_gpa)
                        student1_id, student1_gpa = read_student(file1)
                    else:
                        print(student2_id, student2_gpa)
                        student2_id, student2_gpa = read_student(file2)

# Input file names
file1_name, file2_name = input().split()

# Merge and print the sorted result
merge_files(file1_name, file2_name)