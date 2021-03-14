student = {}
student[0] = {}
student2 = []
import time


def student_info():
    # To get student information from the user
    for i in range(0, 5):
        student[i] = {}
        student[i]['Name'] = input("Please enter {}. student name:".format(i+1))
        student[i]['Surname'] = input("Please enter {}. student Surname:".format(i+1))
        student[i]['Midterm'] = float(input("Please enter {}.student Midterm :".format(i+1)))
        student[i]['Project'] = float(input("Please enter {}. student Project:".format(i+1)))
        student[i]['Final'] = float(input("Please enter {}. student Final:".format(i+1)))
        print("")
    return ()


def student_passing_grade():
    # To calculate students passing grades
    for i in range(0,5):
        midterm = student[i]['Midterm']
        project = student[i]['Project']
        final = student[i]['Final']
        student[i]['Passing Grade'] = midterm*0.3+project*0.3+final*0.4

    return ()


def myFunc(e):
    # The function required to take passing grades will be useful in the ranking.
  return e['Passing Grade']


def iterate_list ():
    # Function for getting student information as output
    for person in student2:
        for k, v in person.items():
            print('{}: {}'.format(k, v))
        print("")
    return

def waiting():
    # just to add fun to the visual and environment :)
    print("")
    print("Please wait during calculations..")
    time.sleep(2)
    print("")
    print("***Student success ranking***")
    print("")
    return

print("*****Welcome to Student Information System*****\n")
student_info()
student_passing_grade()
waiting()

student2 = list(student.values())  # To turn the information I have saved in the dictionary into a list

student2.sort(reverse=True , key=myFunc)  # To rank students according to their scores

iterate_list()










