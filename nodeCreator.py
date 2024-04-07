from node import Node
from datetime import datetime

def getUniuqeVectorIds(project): #gets all unique vectorsIds in eventCollection to group nodes properly
    listOfevents = project.getEventCollection()
    uniqueVectorId = set()
    for eventId in listOfevents:
        eventVectoriD = listOfevents[eventId].getVectorId()
        if eventVectoriD != None and not eventVectoriD.isspace() and eventVectoriD != "": #filtering out invalidVectorIds
            uniqueVectorId.add(eventVectoriD)
    print(uniqueVectorId)
    return uniqueVectorId

def unconnectedNodePositions(uniqueVectorIds): #if nodes have no positions this is where they will be placed
    vectorIdPositionDic = {}
    positionY = 50
    for vectorId in uniqueVectorIds:
        vectorIdPositionDic[vectorId] = positionY
        positionY = positionY + 200
    return vectorIdPositionDic

def eventsToNodes(project,vectorIdPositionDic): #turns all events into nodes and assignes them positions
    dictOfNodes = {}
    listOfevents = project.getEventCollection()
    for eventId in listOfevents:
        event = listOfevents[eventId]
        node = Node(
             nodeXPosition = vectorIdPositionDic.get(event.getVectorId(), 0), #no vectorid Id found put 0
             nodeYPosition = 0,
             nodeId = eventId, #makes node and associated event Id the same
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
        dictOfNodes[eventId] = node
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
                     parentNode.addConnection(childNode.getNodeId())
    return dictOfNodes