from mongoengine import StringField, ListField,EmbeddedDocument,IntField
from bson.objectid import ObjectId
class Node(EmbeddedDocument):
    nodeXPosition = IntField()
    nodeYPosition = IntField()
    nodeId = StringField()
    eventId = StringField()
    nodeLabel = StringField()
    nodeIcon = StringField()
    nodeConnections = ListField(StringField())
    nodeLocation = StringField()
    nodeTimeStamp = StringField()
    nodeDataSource = StringField()
    nodePosture = StringField()
    nodeDescription = StringField()
    nodeVectorId = StringField()

    
    def addConnection(self,connectingNodeId):
        self.nodeConnections.append({'data': {'source': self.nodeId, 'target':connectingNodeId}})

    def getNodeConnections(self):
        return self.nodeConnections
    
    def getNodeDescription(self):
        return self.nodeDescription
    
    def getNodeXPosition(self):
        return self.nodeXPosition
    
    def getNodeId(self):
        return self.nodeId
    
    def getNodeLabel(self):
        return self.nodeLabel

    def getNodeYPosition(self):
        return self.nodeYPosition

    def changeNodeXPosition(self,newX):
        self.nodeXPosition = newX

    def changeNodeYPosition(self,newy):
        self.nodeYPosition = newy

    def getNodeVectorId(self):
        return self.nodeVectorId