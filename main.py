is_male = True
is_adult = True
is_check = True

if is_male and is_adult and is_check:
    print("Congratulation, you can get in the club")
elif is_male and is_adult and not is_check:
    print("Please accept term of agreement before log in to the club")
else:
    print("you are not qualify for the club.")
