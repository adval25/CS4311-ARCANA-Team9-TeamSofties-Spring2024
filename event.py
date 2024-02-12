import mongoengine
class Event(mongoengine.EmbeddedDocument):
    malformed = mongoengine.BooleanField
    eventTimeStamp = mongoengine.StringField()
    analystInitals = mongoengine.StringField(max_length=5)
    eventTeam = mongoengine.StringField()
    eventDescription = mongoengine.StringField()
    eventLocation = mongoengine.StringField()
    eventSourceHost = mongoengine.StringField()
    eventTargetHost = mongoengine.StringField()
    eventVectorId = mongoengine.StringField()
    eventDataSource = mongoengine.StringField()

