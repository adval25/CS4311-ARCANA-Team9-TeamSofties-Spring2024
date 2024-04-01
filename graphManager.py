import projectManager
from node import Node
from eventGraph import EventGraph
from bson.objectid import ObjectId
from datetime import datetime

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

def parseTimestamp(timestamp_str): #time stamps have two 
    formats_to_try = ['%m/%d/%Y %H:%M', '%m/%d/%Y %H:%M:%S']
    for format_str in formats_to_try:
        try:
            return datetime.strptime(timestamp_str, format_str)
        except ValueError:
            pass
    return datetime.max #if there is no timeStamp place it at the end of the list

def edgeCreator(dictOfNodes):
    sortedNodes = sorted(dictOfNodes.values(), key=lambda x: parseTimestamp(x.getNodeTimeStamp()))
    for count,parentNode in enumerate(sortedNodes):
         for childNode in sortedNodes[count+1:]:
             if (parentNode.getNodeVectorId() == childNode.getNodeVectorId() and (parentNode.getNodeVectorId() != "" or parentNode.getNodeVectorId() != " ")) and (parentNode.getNodeLocation() == childNode.getNodeLocation()):
                 if parentNode.getTargerHost() == childNode.getSourceHost():
                     parentNode.addConnection(childNode)
    for nodes in dictOfNodes:
        print(dictOfNodes[nodes].getNodeConnections())
             
    return dictOfNodes

def createGraphElements(dictOfNodes,nodeDictConnections):
    graphElementList = []
    for nodeId in dictOfNodes:
        node = dictOfNodes[nodeId]
        graphElement = {'data': {'id': node.getNodeId(), 'label': node.getNodeLabel()}, 'position': {'x': node.getNodeXPosition(), 'y': node.getNodeYPosition()}}
        graphElementList.append(graphElement)
    for connection in nodeDictConnections.values():
        connections = connection.getNodeConnections()
        if connections:  # Check if connections list is not empty
            graphElementList.extend(connections)
    return graphElementList

def createGraph(selectedProject):
    dictOfNodes = eventsToNodes(selectedProject)
    return EventGraph(dictOfNodes = dictOfNodes)

def getNode(nodeId,projectId):
    project = projectManager.getProject(projectId)
    nodeGraph = project.getEventGraph()
    return nodeGraph.getNode(nodeId)