import os
from dash import dcc
def nodeIconDropDownMaker(dropDownId):
    filenames = os.listdir("assets/NodeIcons") if os.path.isdir("assets/NodeIcons") else []
    dropdown_options = [{'label': filename, 'value': filename} for filename in filenames]
    dropDown = dcc.Dropdown(id=dropDownId,options=dropdown_options,placeholder="Select an image...",value=None)
    return dropDown
