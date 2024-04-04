from mongoengine import StringField, ListField,EmbeddedDocument,IntField
from bson.objectid import ObjectId
class Node(EmbeddedDocument):
    nodeXPosition = IntField()
    nodeYPosition = IntField()
    nodeId = StringField()
    nodeLabel = StringField()
    nodeIcon = StringField()
    nodeConnections = ListField(default=[])
    nodeLocation = StringField()
    nodeTimeStamp = StringField()
    nodeDataSource = StringField()
    nodePosture = StringField()
    nodeDescription = StringField()
    nodeVectorId = StringField()
    nodeSourceHost = StringField()
    nodeTargetHost = StringField()

    
    def addConnection(self,targetNodeId): #formats the connection to easily display in the gui
        if self.nodeConnections == []: #weird bug with listFields this fixes it
            self.nodeConnections = []
        self.nodeConnections.append({'data': {'source': self.nodeId, 'target':targetNodeId}})
    
    def deleteOneConnection(self, targetNodeId):
        for connection in self.nodeConnections:
            if connection['data']['target'] == targetNodeId:
                self.nodeConnections.remove(connection)
                return True
        return False  
    
    def deleteAllTargetConnections(self,targetNodeId):
         self.nodeConnections = [connection for connection in self.nodeConnections if connection.get('data', {}).get('target') != targetNodeId]

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
    
    def getNodeLocation(self):
        return self.nodeLocation
    
    def getNodeTimeStamp(self):
        return self.nodeTimeStamp
    
    def getSourceHost(self):
        return self.nodeSourceHost
    
    def getTargerHost(self):
        return self.nodeTargetHost