from pymongo import MongoClient 

def output_student(student):
    print("Student ID: " + str(student['student_id']))
    print("First Name: " + student['first_name'])
    print("Last Name: " + student['last_name'])
    print("")
    

url="mongodb+srv://admin:admin@cluster0.vkti0bu.mongodb.net/?retryWrites=true&w=majority"
client= MongoClient(url)
db=client.pytech 
students= db.students


all_students= db.students.find()
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
for student in all_students:
    output_student(student)

students.update_one({'student_id':1007}, {"$set":{"last_name":"Looper"}})
find_student= students.find_one({"student_id":1007})
print(" -- DISPLAYING STUDENT DOCUMENT 1007 -- ")
output_student(find_student)

input('End of program, press any key to exit...')