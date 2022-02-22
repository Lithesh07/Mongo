from pymongo import MongoClient
 #Creating a pymongo client
client = MongoClient('localhost', 27017) #Getting the database instance
db = client['mydb']
print("Database created........")
#Verification
print("List of databases after creating new one")
print(client.list_database_names())
#Creating a collection
coll = db['Basics']
#Inserting document into a collection
doc1 = [{"name": "Lithesh", "age": "19", "city": "Kadapa"},{"name": "Nithin", "age": "19", "city": "Rajahmundry"},
        {"name": "Dinesh", "age": "20", "city": "TadepalliGudam"},{"name": "Sainadh", "age": "20", "city": "Tenali"},
        {"name": "Ayyappa", "age": "20", "city": "Guntur"}, {"name": "Rama Krishna", "age": "22", "city": "Rajahmundry"},
        {"name": "Bhargav", "age": "21", "city": "Vizag"}, {"name": "Vishnu", "age": "22", "city": "Ongole"}
        ]
res = coll.insert_many(doc1)
print("Data inserted ......")
print(res.inserted_ids)
 #Retrieving the first record using the find_one() method
print("First record of the collection: ")
print(coll.find())
 #Retrieving data of age 21 using the find_one() method
print("Record whose age is 21: ")
print(coll.find_one({"age": "21"}))
# Retrieving records with age greater than 21 using the find() method
print("Record whose age is more than 21: ")
for doc2 in coll.find({"age": {"$gt": "21"}}):
 print(doc2)
print("Documents in the collection: ")
for doc1 in coll.find({"name":"Lithesh"}):
 print(doc1)
 # Deleting one document
 coll.delete_one({"name": "Nithin"})
 print("Documents in the collection after update operation: ")
 for doc2 in coll.find():
  print(doc2)


