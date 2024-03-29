import mongoengine
from node import Node
from bson.objectid import ObjectId
class EventGraph(mongoengine.EmbeddedDocument):
    dictOfNodes = mongoengine.DictField(mongoengine.EmbeddedDocumentField(Node))

    def getDictOfNodes(self):
        return self.dictOfNodes