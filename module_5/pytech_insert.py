from pymongo import MongoClient 

def output_student(student,inserted_id):
    print("Inserted student record "+ student['first_name'] + " " + student['last_name'] + " into the student collection with document_id " + str(inserted_id))
    


url="mongodb+srv://admin:admin@cluster0.vkti0bu.mongodb.net/?retryWrites=true&w=majority"
client= MongoClient(url)
db=client.pytech

students= db.students

fred = {
 "first_name": "Fred",
 "last_name": "Tucker",
 "student_id": 1007
}

todd = {
 "first_name": "Todd",
 "last_name": "Perez",
 "student_id": 1008
}
john = {
 "first_name": "John",
 "last_name": "Bauer",
 "student_id": 1009
}

new_fred_id=students.insert_one(fred).inserted_id
new_todd_id=students.insert_one(todd).inserted_id
new_john_id=students.insert_one(john).inserted_id


print('-- INSERT STATEMENTS --')
output_student(fred,new_fred_id)
output_student(todd, new_todd_id)
output_student(john, new_john_id)
input('End of program, press any key to exit...')





 
