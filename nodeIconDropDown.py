import os
from dash import dcc
def nodeIconDropDownMaker():
    filenames = os.listdir("NodeIcons") if os.path.isdir("NodeIcons") else []
    dropdown_options = [{'label': filename, 'value': filename} for filename in filenames]
    dropDown = dcc.Dropdown(id='select-image-dropdown',options=dropdown_options,placeholder="Select an image...",)
    return dropDown
