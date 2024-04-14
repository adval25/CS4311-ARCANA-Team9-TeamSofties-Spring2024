# Ingests logs from directory and returns lists with log directories

import os
import pymongo
import csv
from event import Event
from bson.objectid import ObjectId

path = os.getcwd()
folder_name = 'pdrr'
file_path = os.path.join(path, folder_name)


def get_wlogs(file_path): # Returns a list of file paths for White team logs
    wlogs_dir = [] # final list that will be returned with directories of all white team logs
    white_sd_list = [] # contains a list of sub-directories for folders labeled "white"

    # populates list with "white" folder sub-directories
    for dirpath, subdirs, filenames in os.walk(file_path):
        if 'white' in subdirs:
            white_sd_list.append(os.path.join(dirpath, 'white'))

    # compiles a list of file paths for all "white" team log files
    for dir in white_sd_list:
        for dirpath, subdirs, filenames in os.walk(dir):
            for file in filenames:
                fp = os.path.join(dirpath, file)
                if os.path.isfile(fp):
                    wlogs_dir.append(fp)

    return wlogs_dir

def get_blogs(file_path): # Returns a list of file paths for Blue team logs
    blogs_dir = [] # final list that will be returned with directories of all blue team logs
    blue_sd_list = [] # contains a list of sub-directories for folders labeled "blue"

    # populates list with "blue" folder sub-directories
    for dirpath, subdirs, filenames in os.walk(file_path):
        if 'blue' in subdirs:
            blue_sd_list.append(os.path.join(dirpath, 'blue'))

    # compiles a list of file paths for all "blue" team log files
    for dir in blue_sd_list:
        for dirpath, subdirs, filenames in os.walk(dir):
            for file in filenames:
                fp = os.path.join(dirpath, file)
                if os.path.isfile(fp):
                    blogs_dir.append(fp)

    return blogs_dir

def get_rlogs(file_path): # Returns a list of file paths for Red team logs
    rlogs_dir = [] # final list that will be returned with directories of all red team logs
    red_sd_list = [] # contains a list of sub-directories for folders labeled "red"

    # populates list with "red" folder sub-directories
    for dirpath, subdirs, filenames in os.walk(file_path):
        if 'red' in subdirs:
            red_sd_list.append(os.path.join(dirpath, 'red'))

    # compiles a list of file paths for all "red" team log files
    for dir in red_sd_list:
        for dirpath, subdirs, filenames in os.walk(dir):
            for file in filenames:
                fp = os.path.join(dirpath, file)
                if os.path.isfile(fp):
                    rlogs_dir.append(fp)

    return rlogs_dir

def combineLogLists(logPath):
   return  get_wlogs(logPath) +  get_rlogs(file_path) + get_blogs(file_path)


def getCsvPaths(listOfFilePaths):
    csvPaths = []
    for paths in listOfFilePaths:
        if(paths.endswith(".csv")): #grabs all the csvs in the found file paths
            csvPaths.append(paths)
    return csvPaths

def csvsToEventDataList(csvPaths): #turns all of the csv rows into dictionaries
    eventAccumulator =[]
    for csvFile in csvPaths:
        with open(csvFile) as openedCsv:
            listOfEvents = csv.DictReader(openedCsv)
            for event in listOfEvents:
                event["dataSource"] = csvFile #adds datasource attribute to the eventData
                eventAccumulator.append(event)
    return eventAccumulator

def eventDataListToEventDictionary(eventAccumulator): #turns all of the event data into event objects and returns a list of events
    eventDict ={}
    for eventInfromation in eventAccumulator:
        if eventInfromation.get("dateCreated") == None:
            break
        event = Event(eventTimeStamp = str(eventInfromation["dateCreated"]),
                        analystInitals = str(eventInfromation["initials"]),
                        eventTeam = str(eventInfromation["team"]),
                        eventDescription =str(eventInfromation["description"]), 
                        eventLocation = str(eventInfromation["location"]),
                        eventSourceHost = str(eventInfromation["sourceHost"]),
                        eventTargetHost = str(eventInfromation["targetHost"]),
                        eventVectorId = str(eventInfromation["vectorId"]),
                        eventDataSource = str(eventInfromation["dataSource"]),
                        eventId = str(ObjectId())
                        )    
        eventDict[event.getId()] = event
    return eventDict
