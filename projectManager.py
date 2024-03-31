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


def deleteProject():
    return

def createProject(projectName,analystInitals,logPath):
    newProject = dataBaseCommunicator.createProjectDb(projectName,analystInitals) #creates the project object
    logData = logIngestor.csvsToEventDataList(logIngestor.getCsvPaths(logIngestor.combineLogLists())) #grabs all the docs
    newEventDic = logIngestor.eventDataListToEventDictionary(logData) #creates event dictionary from docs
    newProject = dataBaseCommunicator.addEventDictionaryToProject(newProject,newEventDic) 
    nodeGraph = graphManager.createGraph(newProject) 
    newProject = dataBaseCommunicator.addnodeGraphToProject(newProject,nodeGraph) #adds the graph to the project
    return newProject
    
