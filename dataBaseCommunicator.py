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
    try:
        project = Project.objects.get(id=projectId)
        return project
    except Project.DoesNotExist:
        print('No project found with ID:', projectId)
        return None
    except Exception as e:
        print('An error occurred:', e)
        return None

    
def updateProjectEvent(projectId, eventId, updatedEventDescription):
    try:
        project = Project.objects.get(id=projectId)
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
