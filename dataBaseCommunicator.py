import mongoengine
import pymongo
from project import Project
from event import Event
from bson.objectid import ObjectId

def createProjectDb(projectName,analystInitals): #makes the project object
    newProject = Project(projectName = projectName,analystInitals =analystInitals,eventCollection = [],eventGraph = None)
    return newProject

def addEventDictionaryToProject(project,eventDic): 
    project.addEventDict(eventDic)
    project.save()
    return project

def addnodeGraphToProject(project,nodeGraph):
    project.addNodeGraph(nodeGraph)
    project.save()
    return project

def getProjectFromDb(projectId): #grabs the project using project ID
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


dataBaseCleint = mongoengine.connect("projectsDb") #connects the user to the database