from dash import Dash, html
import mongoengine
import dash_cytoscape as cyto
from project import Project
import dataBaseCommunicator
from mongoengine.context_managers import switch_db
import projectManager
import io
import base64
import dash
from flask import Flask, send_from_directory
import os




mongoengine.connect("projectsDb", alias="default")

# allProjects = Project.objects()

# def get_all_documents(database_alias):
#     # Retrieve the database connection by its alias
#     database = mongoengine.get_connection(database_alias)
    
#     # Use the specified database connection to query all documents
#     all_documents = Project.objects.using(database_alias)[:]
    
#     return all_documents

# def add_document_to_database(title, content, database_alias):
#     # Create an instance of your document model
#     with switch_db(Project,database_alias):
#         new_document = projectManager.createProject(title,content,"")
#         # Save the document to the specified database using its alias
#         new_document.save()

# # Example usage
# document_model = dataBaseCommunicator.getAllProjectsFromSeprateDb("projectsDB2","host")
# projectList = projectManager.projectObjectListToName(document_model)
# for project in projectList:
#     print(project["_id"])
#     print(project["projectName"])
from dash import Dash, html
import dash_cytoscape as cyto

app = Dash(__name__)

terminal_nodes = [
    {
        'data': {
            'id': name,
            'label': name.capitalize(),
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/' + url + '/150px-' + url.split('/')[-1]
        }
    }
    for name, url in [
        ['porifera', '4/45/Spongilla_lacustris.jpg'],
        ['ctenophora', 'c/c8/Archaeocydippida_hunsrueckiana.JPG'],
        ['cnidaria', 'c/c1/Polyps_of_Cnidaria_colony.jpg'],
        ['acoela', 'a/aa/Waminoa_on_Plerogyra.jpg'],
        ['echinodermata', '7/7a/Ochre_sea_star_on_beach%2C_Olympic_National_Park_USA.jpg'],
        ['chordata', 'd/d6/White_cockatoo_%28Cacatua_alba%29.jpg']
    ]
]

stylesheet = [
    {
        'selector': 'node',
        'style': {
            'content': 'data(label)',
            'width': 90,
            'height': 80,
            'background-fit': 'cover',
            'background-image': 'data(url)',
            'border-color': '#000',
            'border-width': 1
        }
    },
    {
        'selector': 'node:selected',
        'style': {
            'overlay-color': 'blue',
            'overlay-opacity': 0.5
        }
    },
    {
        'selector': '.terminal',
        'style': {
            'width': 90,
            'height': 80,
            'background-fit': 'cover',
            'background-image': 'data(url)'
        }
    },
    {
        'selector': '.nonterminal',
        'style': {
            'shape': 'rectangle'
        }
    }
]

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-two-nodes',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '400px'},
        elements=[
            {'data': {'id': 'porif1era', 'label': 'Porifera', 'url': 'url(/assets/fileImage.png)'}},
            {'data': {'id': 'porifera', 'label': 'Porifera', 'url': 'url(/assets/fileImage.png)'}}
        ],
        stylesheet=stylesheet
    )
])

if __name__ == '__main__':
    app.run(debug=True)

print(terminal_nodes[0])
