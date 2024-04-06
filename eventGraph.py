import mongoengine
from node import Node
from bson.objectid import ObjectId
class EventGraph(mongoengine.EmbeddedDocument):
    dictOfNodes = mongoengine.DictField(mongoengine.EmbeddedDocumentField(Node))
    vectorIdPositions = mongoengine.DictField()


    def getDictOfNodes(self):
        return self.dictOfNodes
    
    def getNode(self,nodeId):
        return self.dictOfNodes.get(nodeId)
    
    def addEvent(self,node):
        self.dictOfNodes[node.getId()] = node
    
    def getVectorIdPositions(self):
        return self.vectorIdPositions