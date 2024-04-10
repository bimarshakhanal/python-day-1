'''
[dictionary comprehension] Given a dictionary with students'
names as keys and their respective scores as values, create a new
dictionary that contains only the students who scored more than 80
using dictionary comprehension.
'''

def filter_students(students):
    '''Function to filter students using their scores'''

    return {k:v for k,v in students.items() if v > 80}

if __name__=="__main__":
    #define dictionary for student records
    students = {'Ram':40,'Shyam':90,'Sita':81,'Gita':80}
    
    print("Passed students: ",filter_students(students))
