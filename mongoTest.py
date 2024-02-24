#https://www.mongodb.com/try/download/community
#pip install pymongo
#pip install mongoengine
import mongoengine
from mongoengine import connect
from project import Project
from event import Event
import logIngestor

connect("projects-FM")

projectOne = Project(projectName = "Project1FM",analystInitals ="FM",eventCollection = [])
projectOne.save()

eventDictionary = logIngestor.eventDataListToEventList(logIngestor.csvsToEventDataList(logIngestor.getCsvPaths(logIngestor.get_wlogs())))
projectOne.addEvent(eventDictionary)
projectOne.save()




#Example of grabbing something from the database and edeting it
def getProjectFromDatabase(selectedName):
    try:
        project = Project.objects.get(projectName=selectedName)
        return project
    except Project.DoesNotExist:
        print('No project found with name:', selectedName)
    except Exception as e:
        print('An error occurred:', e)

foundProject = getProjectFromDatabase("Project1FM")
event2 = Event(eventDescription = "HELLO HELLO HELLO 4")
foundProject.addEvent(event2)
foundProject.getCollection()
foundProject.save()
