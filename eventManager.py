import projectManager
from bson.objectid import ObjectId
from event import Event
import loggerManager

def createEvent(eventTimeStamp, malformedInputs,intialsInput,vectorIdInput,sourceHostInput,targetHostInput,teamInput,descriptionInput,eventLocation,eventDataSource,eventIcon,eventId=None):
    if eventId is None:
        eventId = str(ObjectId())
    print("EVENTID" +eventId)
    event = Event(eventTimeStamp = str(eventTimeStamp),
                analystInitals = str(intialsInput),
                malformed = bool(malformedInputs),
                eventTeam = str(teamInput),
                eventDescription =str(descriptionInput), 
                eventLocation = str(eventLocation),
                eventSourceHost = str(sourceHostInput),
                eventTargetHost = str(targetHostInput),
                eventVectorId = str(vectorIdInput),
                eventDataSource = str(eventDataSource),
                eventId = str(eventId),
                eventIcon = str(eventIcon)
                )
    return event


def addEventToProject(projectId,event):
    project = projectManager.getProject(projectId)
    project.addEvent(event)
    project.save()
    loggerManager.addUserActivity("User has created an Event and added it to " + project.getProjectName())
    return project

def deleteEvent(eventId,projectId):
    project = projectManager.getProject(projectId)
    del project.getEventCollection()[eventId]
    project.save()
    loggerManager.addUserActivity("User has deleted an Event and it was removed from " + project.getProjectName())
    return project

def editEvent(eventId,projectId,newEventData):
    project = projectManager.getProject(projectId)
    project.getEventCollection()[eventId] = newEventData
    project.save()
    loggerManager.addUserActivity("User has edited an Event and changes where saved to " + project.getProjectName())
    return project

def getEventFromProject(eventId,projectId):
    project = projectManager.getProject(projectId)
    return project.getEvent(eventId)

def eventListToDictionary(projectEvents): #used in the GUI to display the event Table
    eventList = []
    for event in projectEvents:
        eventList.append(projectEvents[event].eventToDictionary())
    return eventList

