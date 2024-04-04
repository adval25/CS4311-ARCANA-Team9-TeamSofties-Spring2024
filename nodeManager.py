import projectManager
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

    