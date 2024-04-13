import mongoengine
import pymongo
from project import Project
from event import Event
from bson.objectid import ObjectId
from mongoengine.context_managers import switch_db


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

def getAllProjectsFromSeprateDb(dataBaseName,host):
    mongoengine.connect(dataBaseName, alias="syncedProject")
    database = mongoengine.get_connection("syncedProject")
    allProjects = Project.objects.using("syncedProject")[:]
    mongoengine.disconnect(alias="syncedProject")
    return allProjects

def deleteProjectFromDb(projectId):
    project = getProjectFromDb(projectId)
    project.delete()

def addProjectFromSerpateDb(projectName,analystInitals,eventCollection,eventGraph):
    project = Project(projectName = projectName, analystInitals = analystInitals,
             eventCollection = eventCollection, eventGraph = eventGraph)
    project.save()
    


dataBaseCleint = mongoengine.connect("projectsDb", alias="default") #connects the user to the database