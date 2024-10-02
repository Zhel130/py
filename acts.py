students = {'John', 'Maria', 'David', 'Samantha'}

index = int(input("Enter the index of the student: "))

count = 0
selected_student = None

for student in students:
    if count == index:
        selected_student = student
        break
    count += 1

if selected_student is not None:
    print(f"The student at index {index} is: {selected_student}")
else:
    print(f"Index {index} is out of range.")



numbers = (1, 4, 7, 10, 13, 16)

odd_sum = 0
odd_count = 0

for num in numbers:
    if num % 2 != 0: 
        odd_sum += num
        odd_count += 1

if odd_count > 0:
    average = odd_sum / odd_count
    print(f"The average of the odd numbers is: {average}")
else:
    print("There are no odd numbers in the tuple.")


people = {'profile': {'John': 19, 'Emily': 21, 'Sarah': 25, 'Tom': 18}}

profiles = people['profile']

for name in profiles:
    if profiles[name] > 19:
        print(f"{name} is older than 19.")


numbers = [1, 3, 2, 4, 3, 1, 2, 5, 10]

duplicates = []

for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count > 1 and numbers[i] not in duplicates:
        duplicates.append(numbers[i])

print("Numbers that appear more than once:", duplicates)


students_scores = [[('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]]

students = students_scores[0]

max_score = 0
top_student = ""

for student in students:
    name, score = student
    if score > max_score:
        max_score = score
        top_student = name

print(f"The student with the highest score is {top_student} with a score of {max_score}.")
