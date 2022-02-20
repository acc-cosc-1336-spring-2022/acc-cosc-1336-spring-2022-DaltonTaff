def get_options_ratio(option, total):
    return (option // total)

def get_letter_grade(grade):
    if grade >= 90 and grade <= 100:
        return 'A'
    elif grade >= 80 and grade < 90:
        return 'B'
    elif grade >= 70 and grade < 80:
        return 'C'
    elif grade >= 60 and grade < 70:
        return 'D'
    elif grade > 0 and grade < 60:
        return 'F'
    else:
        return 'Invalid Number'

def get_faculty_rating(rating):