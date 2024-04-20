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
projectList = Project.objects.get()
print(projectList.id)
