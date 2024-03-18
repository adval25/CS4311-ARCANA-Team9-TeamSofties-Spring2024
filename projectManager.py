import logIngestor
from project import Project
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
    newProject = dataBaseCommunicator.createProjectDb(projectName,analystInitals)
    logData = logIngestor.csvsToEventDataList(logIngestor.getCsvPaths(logIngestor.combineLogLists()))
    newEventDic = logIngestor.eventDataListToEventDictionary(logData)
    newProject = dataBaseCommunicator.addEventDictionaryToProject(newProject,newEventDic)
    return newProject
    
