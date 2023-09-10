from pymongo import MongoClient

def output_student(student):
    print("Student ID: " + str(student))
    print("First Name: " + student ['first_name'])
    print("Last Name: " + student ['last_name'])

url= "mongodb+srv://admin:admin@cluster0.vkti0bu.mongodb.net/?retryWrites=true&w=majority"
client= MongoClient(url)
db=client.pytech
students=db.students



all_students= db.student.find()
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
for student in all_students:
    output_student(student)



    