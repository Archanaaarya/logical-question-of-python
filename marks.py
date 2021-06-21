i = 1
while  i <= 1:
    
    name = input("enter the any name")

    marks_of_accounts = int(input("enter the any marks of accounts subect"))

    marks_of_business_studies = int(input("enter the any marks of the business studies"))

    marks_of_economics = int(input("enter the any marks of the economics subject"))

    marks_of_hindi = int(input("enter the any marks of the hindi subject"))

    marks_of_english = int(input("enter the any number of the english subject"))

    marks_of_music = int(input("enter the any number of the music subjet"))

    total_marks_of_the_student = marks_of_accounts + marks_of_business_studies + marks_of_economics + marks_of_english + marks_of_hindi + marks_of_music

    total_percentage_of_student = (total_marks_of_the_student / 600) * 100

    print(name , "your total marks is ", total_marks_of_the_student , " your total percentage is " , total_percentage_of_student )

