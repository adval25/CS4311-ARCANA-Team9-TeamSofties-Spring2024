ARCANA System Ver 1.4

Language: Python

System Requirements: Linux OS, Mongo & Mongo DB Compass, Docker
dash==2.14.2
dash-bootstrap-components==1.5.0
dash-core-components==2.0.0
dash-html-components==2.0.0
dash-table==5.0.0
dash_ag_grid==31.0.1
dash_cytoscape==0.2.0
mongoengine==0.27.0
pandas==2.2.0
pymongo==4.6.1
Flask==3.0.1
gunicorn==22.0.0

In case of issues with program launch, Ensure the following are properly installed

    Docker Download:
    https://docs.docker.com/desktop/install/linux-install/

    MongoDB Download: 
    https://www.mongodb.com/try/download/community

    Ensure Mongosh is downloaded properly as well:
    https://downloads.mongodb.com/compass/mongosh-2.2.4-linux-x64.tgz

Update Description (4/1/24):

    This version of ARCANA supports basic graph functionality.
    Using dash_cytoscope, the graph now displays nodes that you can manipulate in space and edit information.
    The program supports edge creation, deletion, and manipulation between nodes in the graph.

Update Description (4/22/24):

Added logging to all major user activity.
    Fixed add node funtion.
    Added Dcoker functionality.
    Added ability to access database of other machine using docker (Sync function).
    Fixed various GUI bugs.