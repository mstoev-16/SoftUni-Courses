def grades(grade_input):
    if 2 <= grade_input <= 2.99:
        return 'Fail'
    elif 3 <= grade_input <= 3.99:
        return 'Poor'
    elif 3.50 <= grade_input <= 4.49:
        return 'Good'
    elif 4.50 <= grade_input <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade_input <= 6:
        return 'Excellent'


print(grades(float(input())))
