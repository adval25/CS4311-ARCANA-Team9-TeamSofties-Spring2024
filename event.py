import mongoengine
from bson.objectid import ObjectId
from datetime import datetime
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
    eventIcon = mongoengine.StringField()

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
    
    def getInitals(self):
        return self.analystInitals
    
    def getEventIcon(self):
        return self.eventIcon
    
    def geteventTeam(self):
        return self.eventTeam
    
    def setMalformed(self,malformedInput):
        self.malformed = malformedInput
    
    def getMalformed(self):
        return self.malformed
    
    def getDataSource(self):
        return self.eventDataSource
    
    def getSourceHost(self):
        return self.eventSourceHost
        
    def getTargetHost(self):
        return self.eventTargetHost
    
    def converTimeStampToDateTime(self):
            if self.eventTimeStamp.isspace() or self.eventTimeStamp == "":
                return None
            temporaryTimeStamp = self.eventTimeStamp
            if len(self.eventTimeStamp) <= 15:  # Check if the string has no seconds
                temporaryTimeStamp += ":00"  # Add seconds
            return datetime.strptime(temporaryTimeStamp,'%m/%d/%Y %H:%M:%S')
    
    def eventToDictionary(self): #creates events to a dictionary to display in the gui
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
  


