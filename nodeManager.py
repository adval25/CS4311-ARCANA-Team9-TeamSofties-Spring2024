import projectManager
from node import Node

def createNode(projectId,event):
    project = projectManager.getProject(projectId)
    nodeGraph = project.getEventGraph()
    vectorIds =nodeGraph.getVectorIdPositions()
    node = Node(
        nodeXPosition = vectorIds.get(event.getVectorId(), 0), #no vectorid Id found put 0
        nodeYPosition = 0,
        nodeId = event.getId(), #makes node and associated event Id the same
        nodeLabel = event.geteventTeam(),
        nodeIcon = event.getEventIcon(),
        nodeLocation = event.getEventLocation(),
        nodeTimeStamp = event.getEventTimeStamp(),
        nodeDataSource = event.getDataSource(),
        nodePosture = event.getEventPosture(),
        nodeDescription = event.getEventDescription(),
        nodeVectorId = event.getVectorId(),
        nodeSourceHost = event.getSourceHost(),
        nodeTargetHost = event.getTargetHost(),
        nodeInitals = event.getInitals(),
        nodeMalformed = event.getMalformed()

    )
    return node

def addEdgeToGui(node1_id,node2_id):
    return {"data": {"source": node1_id, "target": node2_id}}

def deleteNodeFromGui(elements,nodeId):
    elements = [e for e in elements if "source" not in e["data"] or e["data"]["source"] != nodeId]
    elements = [e for e in elements if "target" not in e["data"] or e["data"]["target"] != nodeId]
    elements = [e for e in elements if e.get("data", {}).get("id") != nodeId]
    return elements

def addEdgeToNode(projectId,eventId,targetId):
    project = projectManager.getProject(projectId)
    nodeDictionary = project.getEventGraph().getDictOfNodes()
    node = nodeDictionary[eventId]
    targetId = targetId
    node.addConnection(targetId)
    project.save()

def deleteEdge(projectId,eventId,targetId):
    project = projectManager.getProject(projectId)
    nodeDictionary = project.getEventGraph().getDictOfNodes()
    nodeDictionary[eventId].deleteOneConnection(targetId)
    project.save()

def deleteNode(projectId,eventId):
    project = projectManager.getProject(projectId)
    nodeDictionary = project.getEventGraph().getDictOfNodes() 
    for nodeId in nodeDictionary:
        nodeDictionary[nodeId].deleteAllTargetConnections(eventId)
    del nodeDictionary[eventId]
    project.save()

    