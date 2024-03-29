#https://www.mongodb.com/try/download/community
#pip install pymongo
#pip install mongoengine
import mongoengine
from mongoengine import connect
from project import Project
from node import Node
from event import Event

import projectManager
import dataBaseCommunicator
import pymongo
from bson.objectid import ObjectId

# node = Node(50,75,"Name1","title1","")

connection = connect("projectsDb")
projectOne = projectManager.getProject("6600f0c4df5e2b59b4db56e4")
event = projectOne.getEvent("6600f0c4df5e2b59b4db56c4")
node = Node(50,75,"Name1","title1","",event)
print(node.getNodeDescription())