student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}



for item in student_scores:
    if student_scores[item] > 90:
        student_scores[item] = "Outstanding"
        student_grades[item] = student_scores[item]
    elif student_scores[item]  > 80:
        student_scores[item] = "Exceeds Expectations"
        student_grades[item] = student_scores[item]
    elif student_scores[item] > 70:
        student_scores[item] = "Acceptable"
        student_grades[item] = student_scores[item]
    else:
        student_scores[item] = "Fail"
        student_grades[item] = student_scores[item]


print(student_grades)
print(student_scores)