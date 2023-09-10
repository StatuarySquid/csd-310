from pymongo import MongoClient

def output_student(student):
    print("Student ID: " + str(student['student_id'])) 
    print("First Name: " + student ['first_name'])
    print("Last Name: " + student ['last_name'])
    print('')

url= "mongodb+srv://admin:admin@cluster0.vkti0bu.mongodb.net/?retryWrites=true&w=majority"
client= MongoClient(url)
db=client.pytech
students=db.students


'''find() method to display database '''
all_students= db.students.find()
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
for student in all_students:
    output_student(student)

'''insert_one() method to put student_id 1010'''

jack ={
   'student_id': 1010,
   'first_name': 'Jack',
   'last_name' : 'Delete'
}

new_jack_id= students.insert_one(jack).inserted_id


'''find_one() method to display database '''
find_student= students.find_one({"student_id":1010})

print(" -- DISPLAYING STUDENT TEST DOC -- ")
output_student(find_student)

'''delete_one( )  method'''
delete_student= students.delete_one({"student_id":1010})

all_students= db.students.find()
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
for student in all_students:
    output_student(student)