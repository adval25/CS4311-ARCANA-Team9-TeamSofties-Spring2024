import projectManager
from eventGraph import EventGraph
import nodeCreator

def createGraphGUIElements(dictOfNodes):
    graphElementList = []
    for nodeId in dictOfNodes:
        node = dictOfNodes[nodeId]
        graphElement = {'data': {'id': node.getNodeId(), 'label': node.getNodeLabel()}, 'position': {'x': node.getNodeXPosition(), 'y': node.getNodeYPosition()}}
        graphElementList.append(graphElement)
    for connection in dictOfNodes.values():
        connections = connection.getNodeConnections()
        if connections:  # Check if connections list is not empty
            graphElementList.extend(connections)
    return graphElementList

def createGraph(selectedProject):
    vectorIdPositions = nodeCreator.unconnectedNodePositions(nodeCreator.getUniuqeVectorIds(selectedProject))
    dictOfNodes = nodeCreator.eventsToNodes(selectedProject,vectorIdPositions)
    nodeCreator.edgeCreator(dictOfNodes)
    return EventGraph(dictOfNodes = dictOfNodes, vectorIdPositions = vectorIdPositions)

def getNode(nodeId,projectId):
    project = projectManager.getProject(projectId)
    nodeGraph = project.getEventGraph()
    return nodeGraph.getNode(nodeId)

def getGraph(projectId):
    project = projectManager.getProject(projectId)
    return project.getEventGraph()

def addNodeToGraph(node,projectId):
    project = projectManager.getProject(projectId)
    graph = project.getEventGraph()
    graph.addNode(node)
    project.save()

def saveNodePositions(elements,projectId):
    project = projectManager.getProject(projectId)
    dictOfNodes = project.getEventGraph().getDictOfNodes()
    for element in elements:
        if len(element) == 2:
            node = dictOfNodes.get(element["data"]["id"])
            node.changeNodeXPosition(element["position"]["x"])
            node.changeNodeYPosition(element["position"]["y"])
    project.save()