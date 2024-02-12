#https://www.mongodb.com/try/download/community
#pip install pymongo
#pip install mongoengine
import mongoengine
from mongoengine import connect
from project import Project
from event import Event

connect("projects-FM")

projectOne = Project(projectName = "Project1FM",analystInitals ="FM")
projectOne.save()
event1 = Event(eventDescription = "HELLO HELLO HELLO ")
projectOne.addEvent(event1)
event2 = Event(eventDescription = "HELLO HELLO HELLO 1")
projectOne.addEvent(event2)
projectOne.save()
