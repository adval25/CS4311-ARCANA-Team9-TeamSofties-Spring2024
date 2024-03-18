import mongoengine
from bson.objectid import ObjectId
class Event(mongoengine.EmbeddedDocument):
    malformed = mongoengine.BooleanField(default=False)
    eventTimeStamp = mongoengine.StringField()
    analystInitals = mongoengine.StringField(max_length=5)
    eventTeam = mongoengine.StringField()
    eventDescription = mongoengine.StringField()
    eventLocation = mongoengine.StringField()
    eventSourceHost = mongoengine.StringField()
    eventTargetHost = mongoengine.StringField()
    eventVectorId = mongoengine.StringField()
    eventDataSource = mongoengine.StringField()
    eventId = mongoengine.StringField()

    def getEventDescription(self):
        return self.eventDataSource
    
    def getId(self):
        return self.eventId
    
    def eventToDictionary(self):
        return {
        'malformed': self.malformed,
        'eventTimeStamp': self.eventTimeStamp,
        'analystInitals': self.analystInitals,
        'eventTeam': self.eventTeam,
        'eventDescription': self.eventDescription,
        'eventLocation': self.eventLocation,
        'eventSourceHost': self.eventSourceHost,
        'eventTargetHost': self.eventTargetHost,
        'eventVectorId': self.eventVectorId,
        'eventDataSource': self.eventDataSource,
        '_id': self.eventId  # Convert ObjectId to string
    }
  


