import projectManager

def addEventToProject(project,event):
    project.addEvent(event)
    project.save()
    return project

def deleteEvent(eventId,projectId):
    project = projectManager.getProject(projectId)
    del project.getEventCollection()[eventId]
    project.save()
    return project

def editEvent(eventId,projectId,newEventData):
    project = projectManager.getProject(projectId)
    project.getEventCollection()[eventId] = newEventData
    project.save()
    return project

def eventListToDictionary(projectEvents): #used in the GUI to display the event Table
    eventList = []
    for event in projectEvents:
        eventList.append(projectEvents[event].eventToDictionary())
    return eventList

