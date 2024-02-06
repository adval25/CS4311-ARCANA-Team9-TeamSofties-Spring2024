#https://www.mongodb.com/try/download/community
#pip install pymongo
#pip install mongoengine
import mongoengine
from mongoengine import connect

connect("animals")
#mongoengine.EmbeddedDocument) if the document is embedded
class Animal(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    age = mongoengine.IntField()
    employeeid = mongoengine.StringField(max_length=50)
    meta = {"collection" : "employess"} #db_alias : databaseName sets what database this goes too
    #without meta the collection in the db will be named after the classn 

tofu = Animal(name = "Greg", age = 10, employeeid = "864").save()

    