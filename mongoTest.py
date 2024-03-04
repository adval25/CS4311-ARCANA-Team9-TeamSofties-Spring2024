#https://www.mongodb.com/try/download/community
#pip install pymongo
#pip install mongoengine
import mongoengine
from mongoengine import connect
from project import Project
from event import Event
import logIngestor
import dataBaseCommunicator
import pymongo
from bson.objectid import ObjectId


connection = connect("projectsDb")
projectOne = Project(projectName = "Project4FM",analystInitals ="FM",eventCollection = [])
eventDictionary = logIngestor.eventDataListToEventList(logIngestor.csvsToEventDataList(logIngestor.getCsvPaths(logIngestor.get_wlogs())))
dataBaseCommunicator.addEventListToProject(projectOne,eventDictionary)
projectOne.save()

# projectDict = dataBaseCommunicator.getAllProjectsFromDb(client=connection)
# matching_values =  [{"_id": str(project["_id"]), "projectName": project["projectName"]} for project in projectDict]
# print(matching_values)
#Example of grabbing something from the database and edeting it
# def getProjectFromDatabase(selectedName):
#     try:
#         project = Project.objects.get(projectName=selectedName)
#         return project
#     except Project.DoesNotExist:
#         print('No project found with name:', selectedName)
#     except Exception as e:
#         print('An error occurred:', e)
# project = dataBaseCommunicator.getProjectFromDb(dataBaseCommunicator.getAllProjectsFromDb(connection)[0]["_id"])
# print(project.getEventCollection())
# # print(dataBaseCommunicator.getEventDictionaryFromDb( ObjectId(dataBaseCommunicator.getAllProjectsFromDb(connection)[0]["_id"]),connection))
# # foundProject = dataBaseCommunicator.getProjectFromDb( ObjectId("65dd7fd43f7ee0a383a6fcbf"))
# event = Event(eventTimeStamp ="dateCreated",
#                         analystInitals ="FXR",
#                         eventTeam = str("team"),
#                         eventDescription =str("description"), 
#                         eventLocation = str("location"),
#                         eventSourceHost = str("sourceHost"),
#                         eventTargetHost = str("targetHost"),
#                         eventVectorId = str("vectorId"),
#                         eventDataSource = str("dataSource"),
#                         )
# dataBaseCommunicator.addEventToProject(project,event)
# event2 = Event(eventDescription = "HELLO HELLO HELLO 5")
# dataBaseCommunicator.addEventToProject(foundProject,event2)

# foundProject.addEvent(event2)
# foundProject.getCollection()
# foundProject.save()
