from dash import Dash, html
import mongoengine
import dash_cytoscape as cyto
from project import Project
import dataBaseCommunicator
from mongoengine.context_managers import switch_db
import projectManager



mongoengine.connect("projectsDb", alias="default")

allProjects = Project.objects()

def get_all_documents(database_alias):
    # Retrieve the database connection by its alias
    database = mongoengine.get_connection(database_alias)
    
    # Use the specified database connection to query all documents
    all_documents = Project.objects.using(database_alias)[:]
    
    return all_documents

def add_document_to_database(title, content, database_alias):
    # Create an instance of your document model
    with switch_db(Project,database_alias):
        new_document = projectManager.createProject(title,content,"")
        # Save the document to the specified database using its alias
        new_document.save()

# Example usage
document_model = dataBaseCommunicator.getAllProjectsFromSeprateDb("projectsDB2","host")
projectList = projectManager.projectObjectListToName(document_model)
for project in projectList:
    print(project["_id"])
    print(project["projectName"])

mongoengine.disconnect(alias="projectsDb2")
