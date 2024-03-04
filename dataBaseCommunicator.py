import mongoengine
import pymongo
from project import Project
from event import Event
from bson.objectid import ObjectId

def createProject(projectName,analystInitals):
    newProject = Project(projectName = projectName,analystInitals =analystInitals,eventCollection = [])
    return newProject

#TODO
def addEventToProject(project,event):
    project.addEvent(event)
    project.save()
    return project

def addEventListToProject(project,event):
    project.addEventList(event)
    project.save()
    return project

def getProjectFromDb(projectId):
    try:
        project = Project.objects.get(_id=projectId)
        return project
    except Project.DoesNotExist:
        print('No project found with ID:', projectId)
        return None
    except Exception as e:
        print('An error occurred:', e)
        return None

    
def updateProjectEvent(projectId, eventId, updatedEventDescription):
    try:
        project = Project.objects.get(_id=projectId)
        for event in project.eventCollection:         # Find the event by its ID and update its description
            if str(event.id) == eventId:
                event.eventDescription = updatedEventDescription
                break
        project.save()
        return project
    except Project.DoesNotExist:
        print('No project found with ID:', projectId)
        return None
    except Exception as e:
        print('An error occurred:', e)
        return None


def deleteProjectEvent(projectId, eventId):
    try:
        project = Project.objects.get(id=projectId)  # Filter out the event to be deleted
        project.eventCollection = [event for event in project.eventCollection if str(event.id) != eventId]
        project.save()
        return project
    except Project.DoesNotExist:
        print('No project found with ID:', projectId)
        return None
    except Exception as e:
        print('An error occurred:', e)
        return None

def getEventDictionaryFromDb(projectId,client):
    projectId = ObjectId(projectId)
    projectDataBase = client["projectsDb"]
    projectCollection = projectDataBase["project"]
    foundProject = projectCollection.find({"_id": projectId})
    projectInformation = list(foundProject)
    if projectInformation and len(projectInformation) == 1: #there should only ever be one result objectID are unique
        return projectInformation[0]["eventCollection"] #returbns just the events of the fist project found
    else:
        print("ERROR PROJECTID NOT IN DB")


def getEmbeddedDocFromDb(projectId):
    retrivedProject = getProjectFromDb(projectId)
    return retrivedProject.getEventCollection()

def getAllProjectsFromDb(client):
     projectDataBase = client["projectsDb"]
     projectCollection = projectDataBase["project"]
     return list(projectCollection.find())


dataBaseCleint = mongoengine.connect("projectsDb")