from pymongo import MongoClient

def fetchTasks():
    client=MongoClient('localhost',27017)
    db=client['userdb']
    table=db['tasks']
    result=list(table.find({},{'task':1,'_id':1}))
    return result


#print(fetchTasks())