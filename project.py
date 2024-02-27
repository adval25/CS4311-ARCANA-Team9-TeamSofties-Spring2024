import mongoengine
from event import Event
class Project(mongoengine.Document):
    projectName = mongoengine.StringField()
    analystInitals = mongoengine.StringField(max_length=5)
    eventCollection = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Event))
    _id = mongoengine.ObjectIdField()

    def addEvent(self,event):
        self.eventCollection.extend(event) #has to be extend it will break otherwhise
    
    def getEventCollection(self):
        return self.eventCollection

