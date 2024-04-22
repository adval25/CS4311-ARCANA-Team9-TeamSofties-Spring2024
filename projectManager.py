import logIngestor
from project import Project
import graphManager
import dataBaseCommunicator
import loggerManager

def getProjectDict():
    projectList = dataBaseCommunicator.getAllProjectsFromDb()
    return projectList



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
    logData = logIngestor.csvsToEventDataList(logIngestor.getCsvPaths(logIngestor.combineLogLists(logPath))) #grabs all the docs
    newEventDic = logIngestor.eventDataListToEventDictionary(logData) #creates event dictionary from docs
    newProject = dataBaseCommunicator.addEventDictionaryToProject(newProject,newEventDic) 
    nodeGraph = graphManager.createGraph(newProject) 
    newProject = dataBaseCommunicator.addnodeGraphToProject(newProject,nodeGraph) #adds the graph to the project
    loggerManager.addUserActivity("User has created " + projectName + "its logs are from the " + logPath + "its intials are set as" + analystInitals)
    return newProject
    
