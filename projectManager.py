import logIngestor
from project import Project
import graphManager
import dataBaseCommunicator

def getProjectDict(client):
    projectDataBase = client["projectsDb"]
    projectCollection = projectDataBase["project"]
    return list(projectCollection.find())

def getProject(projectId):
    return dataBaseCommunicator.getProjectFromDb(projectId)

def getAllProjectNames(projectDict): #grabbing the project name and associating each one with an id
    projectList =  [{"_id": str(project["_id"]), "projectName": project["projectName"]} for project in projectDict]
    return projectList

def projectObjectListToName(projectList):
     projectList =  [{"_id": str(project.id), "projectName": str(project.getProjectName())} for project in projectList]
     return projectList

def deleteProject(projectId):
    dataBaseCommunicator.deleteProjectFromDb(projectId)
    return

def checkIfProjectExists(projectId):
    if projectId == {}:
        return False
    return not (Project.objects.with_id(object_id=projectId) == None)


def getProjectName(projectId):
    project = dataBaseCommunicator.getProjectFromDb(projectId)
    return project.getProjectName()

def createProject(projectName,analystInitals,logPath):
    newProject = dataBaseCommunicator.createProjectDb(projectName,analystInitals) #creates the project object
    logData = logIngestor.csvsToEventDataList(logIngestor.getCsvPaths(logIngestor.combineLogLists())) #grabs all the docs
    newEventDic = logIngestor.eventDataListToEventDictionary(logData) #creates event dictionary from docs
    newProject = dataBaseCommunicator.addEventDictionaryToProject(newProject,newEventDic) 
    nodeGraph = graphManager.createGraph(newProject) 
    newProject = dataBaseCommunicator.addnodeGraphToProject(newProject,nodeGraph) #adds the graph to the project
    return newProject
    
