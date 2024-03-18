import mongoengine
from event import Event
from bson.objectid import ObjectId
class Project(mongoengine.Document):
    projectName = mongoengine.StringField()
    analystInitals = mongoengine.StringField(max_length=5)
    eventCollection = mongoengine.DictField(mongoengine.EmbeddedDocumentField(Event))

    def addEventDict(self,eventDic):
        self.eventCollection = eventDic#has to be extend it will break otherwhise
    
    def addEvent(self,event):
         self.eventCollection[event.getId()] = event
    
    def getEventCollection(self):
        return self.eventCollection