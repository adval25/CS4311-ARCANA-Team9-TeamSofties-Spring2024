import mongoengine
from node import Node
class EventGraph(mongoengine.EmbeddedDocument):
    dictOfNodes = mongoengine.DictField(mongoengine.EmbeddedDocumentField(Node))
    vectorIdPositions = mongoengine.DictField()

    def getDictOfNodes(self):
        return self.dictOfNodes
    
    def getNode(self,nodeId):
        return self.dictOfNodes.get(nodeId)
    
    def addNode(self,node):
        self.dictOfNodes[node.getNodeId()] = node
    
    def getVectorIdPositions(self):
        return self.vectorIdPositions
    
    def addVectorIds(self,newVectorId):
        maxVectorPosition = max(self.vectorIdPositions.values())
        print(maxVectorPosition)
        if newVectorId not in self.vectorIdPositions:
            self.vectorIdPositions[newVectorId] = maxVectorPosition + 200

