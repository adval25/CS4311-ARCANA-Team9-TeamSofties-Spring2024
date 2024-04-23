import mongoengine
import pymongo
from pymongo import MongoClient
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

def getAllProjectsFromDb():
    try:
        projectList = Project.objects.all()
        print(projectList)
        return projectList
    except Exception as e:
        print("An error occurred while retrieving projects:", str(e))
        return None

def getAllProjectsFromSeprateDb(dataBaseName,host):
    client = MongoClient(host, 27017)
    mongoengine.connect(dataBaseName, alias="syncedProject")
    database = mongoengine.get_connection("syncedProject")
    # Access database and collection
    db = client.mydatabase
    allProjects = db.mycollection
    # allProjects = Project.objects.using("syncedProject")[:]
    mongoengine.disconnect(alias="syncedProject")
    return allProjects

def getProjectByIDFromSeprateDb(dataBaseName, host, projectId):
    mongoengine.connect(dataBaseName,alias="syncedProject")
    
    try:
        project = Project.objects.using("syncedProject").get(id=projectId)
        return project
    except Project.DoesNotExist:
        return None
    finally:
        mongoengine.disconnect(alias="syncedProject")

def deleteProjectFromDb(projectId):
    project = getProjectFromDb(projectId)
    project.delete()

def addProjectFromSerpateDb(project):
    project = Project(projectName = project.getProjectName(), analystInitals = project.getAnalystInitals(),
             eventCollection = project.getEventCollection(), eventGraph = project.getEventGraph())
    project.save()

    


