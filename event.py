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
    eventPosture = mongoengine.StringField(default = "")
    eventId = mongoengine.StringField()

    def getEventDescription(self):
        return self.eventDescription
    
    def getEventLocation(self):
        return self.eventLocation
    
    def getEventTimeStamp(self):
        return self.eventTimeStamp
    
    def getEventPosture(self):
        return self.eventPosture
    
    def getId(self):
        return self.eventId
    
    def getVectorId(self):
        return self.eventVectorId
    
    def geteventTeam(self):
        return self.eventTeam
    
    def setMalformed(self,malformedInput):
        self.malformed = malformedInput
    
    def getDataSource(self):
        return self.eventDataSource
    
    def getSourceHost(self):
        return self.eventSourceHost
        
    def getTargetHost(self):
        return self.eventTargetHost
    
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
  


