import mongoengine
from event import Event
from eventGraph import EventGraph
from bson.objectid import ObjectId
class Project(mongoengine.Document):
    projectName = mongoengine.StringField()
    analystInitals = mongoengine.StringField()
    eventCollection = mongoengine.DictField(mongoengine.EmbeddedDocumentField(Event))
    eventGraph = mongoengine.EmbeddedDocumentField(EventGraph)
    #nodeIconList = mongoengine.ListField(mongoengine.DictField())

    def addEventDict(self,eventDic):
        self.eventCollection = eventDic#has to be extend it will break otherwhise
    
    def addNodeGraph(self,nodeGraph):
        self.eventGraph = nodeGraph
    
    def addEvent(self,event):
         self.eventCollection[event.getId()] = event
    
    def getEventCollection(self):
        return self.eventCollection

    def getEvent(self,eventId):
        return self.eventCollection[eventId]
    
    def getEventGraph(self):
        return self.eventGraph
    
    def getProjectName(self):
        return self.projectName
    
    def getAnalystInitals(self):
        return self.analystInitals

    # def getNodeIconList(self):
    #     return self.nodeIconList
    
    # def appendIconList(self,imageName,ImageData):
    #     image_entry = {"name": imageName, "data": ImageData}
    #     self.nodeIconList.append(image_entry)