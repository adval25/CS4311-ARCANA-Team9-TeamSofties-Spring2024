import loggerManager
import mongoengine
from project import Project
mongoengine.connect("projectsDB2", alias="default", host="mongodb", port=27017)
newProject = Project(projectName = "hello from local host",analystInitals ="FXR",eventCollection = {},eventGraph = None)
newProject.save()