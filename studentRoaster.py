# A list of student records (dictionaries)
student_records = [
    {
        "student_id": "S1001",
        "name": "Alice Johnson",
        # Tuple of grades: (Math, Science, History)
        "grades": (92, 88, 95),
        # Set of courses enrolled
        "courses": {"Calculus", "Physics", "English Lit"}
    },
    {
        "student_id": "S1002",
        "name": "Bob Smith",
        "grades": (78, 85, 80),
        "courses": {"Physics", "Intro to CS", "Economics"}
    },
    {
        "student_id": "S1003",
        "name": "Charlie Brown",
        "grades": (99, 92, 100),
        "courses": {"Calculus", "Physics", "English Lit", "Art History"}
    }
]

def analyze_roster(roster_list):
    """
    Processes the student roster to calculate averages and find unique courses.

    :param roster_list: A list of student dictionary records.
    :return: A tuple containing (dict_of_averages, set_of_unique_courses).
    """

    # 1. Dictionary to store student averages: {'name': average_grade}
    student_averages = {}

    # 2. Set to store all unique courses
    all_unique_courses = set()

    # Iterate through the list of student dictionaries
    for student in roster_list:
        # **Accessing Dictionary and Tuple:**
        grades_tuple = student["grades"]

        # Calculate average grade: sum of grades / number of grades
        # sum() and len() work directly on the tuple
        avg_grade = sum(grades_tuple) / len(grades_tuple)

        # Store in the new dictionary
        student_averages[student["name"]] = round(avg_grade, 2)

        # **Combining Sets:**
        # Use the union or update method to add courses to the unique set
        all_unique_courses.update(student["courses"])

    # Return the results as a tuple
    return student_averages, all_unique_courses


# Call the function and unpack the results
(averages, unique_courses) = analyze_roster(student_records)

# Print the results
print("--- Student Grade Analysis ---")
print(f"**Student Averages (Dictionary):** {averages}")
print("\n**All Unique Courses Offered (Set):**")
# Iterating through the set
for course in sorted(list(unique_courses)):
    print(f"- {course}")

# Example: Finding the student with the highest average
best_student = max(averages, key=averages.get)
print(f"\n**Top Performer:** {best_student} with an average of {averages[best_student]}")