import mongoengine
import pymongo
from project import Project
from event import Event
from bson.objectid import ObjectId

def createProjectDb(projectName,analystInitals):
    newProject = Project(projectName = projectName,analystInitals =analystInitals,eventCollection = [])
    return newProject

def addEventDictionaryToProject(project,event):
    project.addEventDict(event)
    project.save()
    return project

def getProjectFromDb(projectId):
    try:
        project = Project.objects.get(id=projectId)
        return project
    except Project.DoesNotExist:
        print('No project found with ID:', projectId)
        return None
    except Exception as e:
        print('An error occurred:', e)
        return None

def getEmbeddedDocFromDb(projectId):
    retrivedProject = getProjectFromDb(projectId)
    return retrivedProject.getEventCollection()

def getAllProjectsFromDb(client):
     projectDataBase = client["projectsDb"]
     projectCollection = projectDataBase["project"]
     return list(projectCollection.find())


dataBaseCleint = mongoengine.connect("projectsDb")