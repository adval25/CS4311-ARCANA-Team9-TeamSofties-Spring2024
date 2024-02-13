#https://www.mongodb.com/try/download/community
#pip install pymongo
#pip install mongoengine
import mongoengine
from mongoengine import connect
from project import Project
from event import Event
import logIngestor
import pandas as pd

connect("projects-FM")

projectOne = Project(projectName = "Project1FM",analystInitals ="FM")
projectOne.save()

eventsDataFrame = logIngestor.csvsToDataFrame(logIngestor.getCsvPaths(logIngestor.get_wlogs()))
index = 1
while index < len(eventsDataFrame):
    event = Event(eventTimeStamp = str(eventsDataFrame["dateCreated"][index]),
                    analystInitals = str(eventsDataFrame["initials"][index]),
                    eventTeam = str(eventsDataFrame["team"][index]),
                    eventDescription =str(eventsDataFrame["description"][index]), 
                    eventLocation = str(eventsDataFrame["location"][index]),
                    eventSourceHost = str(eventsDataFrame["sourceHost"][index]),
                    eventTargetHost = str(eventsDataFrame["targetHost"][index]),
                    eventVectorId = str(eventsDataFrame["vectorId"][index]),)
    projectOne.addEvent(event)
    index += 1
projectOne.save()


def getProjectFromDatabase(selectedName):
    try:
        project = Project.objects.get(projectName=selectedName)
        return project
    except Project.DoesNotExist:
        print('No project found with name:', selectedName)
    except Exception as e:
        print('An error occurred:', e)

# foundProject = getProjectFromDatabase("Project1FM")
# event2 = Event(eventDescription = "HELLO HELLO HELLO 4")
# foundProject.addEvent(event2)
# foundProject.getCollection()
# foundProject.save()
