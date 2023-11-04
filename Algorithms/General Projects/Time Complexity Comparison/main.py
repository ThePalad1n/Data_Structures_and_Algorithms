import time

# Read data from the text file
def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    students = []
    for line in lines:
        student = line.strip().split(',')
        students.append({
            'Student ID': int(student[0]),
            'First Name': student[1],
            'Last Name': student[2],
            'Email ID': student[3],
            'Major': student[4]
        })
    return students

# Linear Search
def linear_search(students, key, value):
    for student in students:
        if student[key] == value:
            return student
    return None

# Selection Sort
def selection_sort(students, key):
    start_time = time.time()
    for i in range(len(students)):
        min_idx = i
        for j in range(i+1, len(students)):
            if students[j][key] < students[min_idx][key]:
                min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i] 
    print(f"Selection Sort Time: {time.time() - start_time}")

# Insertion Sort
def insertion_sort(students, key):
    start_time = time.time()
    for i in range(1, len(students)):
        j = i-1
        next_elem = students[i]
        while (students[j][key] > next_elem[key]) and (j >= 0):
            students[j+1] = students[j]
            j=j-1
        students[j+1] = next_elem
    print(f"Insertion Sort Time: {time.time() - start_time}")

# Bubble Sort
def bubble_sort(students, key):
    start_time = time.time()
    for i in range(len(students)):
        for j in range(0, len(students)-i-1):
            if students[j][key] > students[j+1][key]:
                students[j], students[j+1] = students[j+1], students[j]
    print(f"Bubble Sort Time: {time.time() - start_time}")

# Main Program
students = read_data('students.txt')
print("Original Data:")
print(students)

# Linear Search Example
start_time = time.time()
print("Linear Search Result:", linear_search(students, 'Student ID', 5))
print(f"Linear Search Time: {time.time() - start_time}")

# Sorting
selection_sort(students, 'Student ID')
print("Sorted by Selection Sort:")
print(students)

insertion_sort(students, 'First Name')
print("Sorted by Insertion Sort:")
print(students)

bubble_sort(students, 'Last Name')
print("Sorted by Bubble Sort:")
print(students)




# Function to print and record time
def print_and_record_time(sort_function, students, key, table):
    start_time = time.time()
    sort_function(students, key)
    elapsed_time = time.time() - start_time
    print(f"{sort_function.__name__} Time: {elapsed_time}")
    table[sort_function.__name__] = elapsed_time

# Main Program
students = read_data('students.txt')

# Sort by Student ID and record time
print("\nSorting by Student ID on already sorted data:")
table_3_id = {}
print_and_record_time(selection_sort, students, 'Student ID', table_3_id)
print_and_record_time(insertion_sort, students, 'Student ID', table_3_id)
print_and_record_time(bubble_sort, students, 'Student ID', table_3_id)

# Sort by First Name and record time
print("\nSorting by First Name on already sorted data:")
table_3_first_name = {}
insertion_sort(students, 'First Name')  # Sorting by First Name first
print_and_record_time(selection_sort, students, 'First Name', table_3_first_name)
print_and_record_time(insertion_sort, students, 'First Name', table_3_first_name)
print_and_record_time(bubble_sort, students, 'First Name', table_3_first_name)

# Sort by Last Name and record time
print("\nSorting by Last Name on already sorted data:")
table_3_last_name = {}
insertion_sort(students, 'Last Name')  # Sorting by Last Name first
print_and_record_time(selection_sort, students, 'Last Name', table_3_last_name)
print_and_record_time(insertion_sort, students, 'Last Name', table_3_last_name)
print_and_record_time(bubble_sort, students, 'Last Name', table_3_last_name)

# Table-3: Time on Already Sorted Data
print("\nTable-3: Time on Already Sorted Data")
print("Sorting by Student ID:", table_3_id)
print("Sorting by First Name:", table_3_first_name)
print("Sorting by Last Name:", table_3_last_name)



# Main Program
students_identical = read_data('students_identical.txt')

# Function to print and record time
def print_and_record_time_identical(sort_function, students, key, table):
    start_time = time.time()
    sort_function(students, key)
    elapsed_time = time.time() - start_time
    print(f"{sort_function.__name__} Time: {elapsed_time}")
    table[sort_function.__name__] = elapsed_time

# Sort by Student ID and record time for identical data
print("\nSorting by Student ID on identical data:")
table_4_id = {}
print_and_record_time_identical(selection_sort, students_identical, 'Student ID', table_4_id)
print_and_record_time_identical(insertion_sort, students_identical, 'Student ID', table_4_id)
print_and_record_time_identical(bubble_sort, students_identical, 'Student ID', table_4_id)

# Table-4: Time on Identical Data
print("\nTable-4: Time on Identical Data")
print("Sorting by Student ID:", table_4_id)