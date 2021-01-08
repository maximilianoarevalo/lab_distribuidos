from pymongo import MongoClient
try: 
    conn = MongoClient(
        host=['35.232.177.132:27017'],
        document_class=dict,
        username="admin",
        password="retro123",
        connect=True
    ) 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

db = conn.ejemplo
collection = db.ejemplo