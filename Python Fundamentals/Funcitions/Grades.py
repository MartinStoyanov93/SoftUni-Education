def grade_function(grade):
    if 2 <= grade <= 2.99:
        print("Fail")
    elif grade <= 3.49:
        print("Poor")
    elif grade <= 4.49:
        print("Good")
    elif grade <= 5.49:
        print("Very Good")
    else:
        print("Excellent")


grade_function(float(input()))