import mongoengine
from event import Event
class Project(mongoengine.Document):
    projectName = mongoengine.StringField()
    analystInitals = mongoengine.StringField(max_length=5)
    eventCollection = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Event))


    def addEvent(self,event):
        self.eventCollection.extend(event) #has to be extend it will break otherwhise

    def getCollection(self):
        for event in self.eventCollection:
            print(event.getEventDescription())

