import projectManager
from node import Node
from eventGraph import EventGraph
from bson.objectid import ObjectId

def getUniuqeVectorIds(project): #gets all unique vectorsIds in eventCollection to group nodes properly
    listOfevents = project.getEventCollection()
    uniqueVectorId = set()
    for eventId in listOfevents:
        event = listOfevents[eventId]
        uniqueVectorId.add(event.getVectorId())
    uniqueVectorId.discard("None")
    uniqueVectorId.discard('')
    uniqueVectorId.discard(' ')
    print(uniqueVectorId)
    return uniqueVectorId

def unconnectedNodePositions(uniqueVectorIds): #if nodes have no positions this is where they will be placed
    vectorIdPositionDic = {}
    positionY = 50
    for vectorId in uniqueVectorIds:
        vectorIdPositionDic[vectorId] = positionY
        positionY = positionY + 200
    print(vectorIdPositionDic)
    return vectorIdPositionDic

def eventsToNodes(project): #turns all events into nodes and assignes them positions
    dictOfNodes = {}
    listOfevents = project.getEventCollection()
    vectorIdPositionDic = unconnectedNodePositions(getUniuqeVectorIds(project))
    for eventId in listOfevents:
        event = listOfevents[eventId]
        node = Node(
             nodeXPosition = vectorIdPositionDic.get(event.getVectorId(), 0), #no vectorid Id found put 0
             nodeYPosition = 0,
             nodeId =  str(ObjectId()), #gives all node a unique id
             eventId = event.getId(),
             nodeLabel = event.geteventTeam(),
             nodeIcon = "",
             nodeLocation = event.getEventLocation(),
             nodeTimeStamp = event.getEventTimeStamp(),
             nodeDataSource = event.getDataSource(),
             nodePosture = event.getEventPosture(),
             nodeDescription = event.getEventDescription(),
             nodeVectorId = event.getVectorId(),
             nodeSourceHost = event.getSourceHost(),
             nodeTargetHost = event.getTargetHost()
             )
        dictOfNodes[node.getNodeId()] = node
    return dictOfNodes

def createGraph(selectedProject):
    dictOfNodes = eventsToNodes(selectedProject)
    return EventGraph(dictOfNodes = dictOfNodes)

def getNode(nodeId,projectId):
    project = projectManager.getProject(projectId)
    nodeGraph = project.getEventGraph()
    return nodeGraph.getNode(nodeId)