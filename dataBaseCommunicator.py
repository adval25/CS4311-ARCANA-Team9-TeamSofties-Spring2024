import mongoengine
import pymongo
from project import Project
from event import Event

def createProject(projectName,analystInitals):
    newProject = Project(projectName = projectName,analystInitals =analystInitals,eventCollection = [])
    newProject.save() #sends project to the database
    return newProject

#TODO
def addEventToProject(project,event):
    project.addEvent(event)
    project.save()
    return project

def getProjectFromDb(projectId):
    return 0
    
def updateProjectEvent(projectId, eventId):
    return 0

def deleteProjectEvent(projectId, eventId):
    return 0

def getEmbeddedDocFromDb(projectId):
    return 0

def getAllProjectsFromDb(client):
     projectDataBase = client["projectsDb"]
     projectCollection = projectDataBase["project"]
     return list(projectCollection.find())
