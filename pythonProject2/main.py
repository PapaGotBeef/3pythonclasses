import Student
import Quiz
import score



def main():
    print("Welcome to the simple quiz!")
    answer = input("Would you like to take the quiz?")
    if answer.lower() != "y":
        print("Thanks for your time!")
    else:
        student = make_student()
        grade = Quiz.run_test(Quiz.questions)
        studentScore = score.score(grade, score.calc_percent(grade))
        print("Congrats, " + student.fname + " you got " + str(studentScore.points) + "/" + str(len(Quiz.questions)) + " correct!\nThat's " + str(studentScore.percentcorrect) + "%!" )

def make_student():
    value = input("Enter your first name: ")
    value2 = input("Enter your last name: ")
    student = Student.Student(value, value2)
    print("Hello " + student.fname + " " + student.lname + "!")

    return student


main()

