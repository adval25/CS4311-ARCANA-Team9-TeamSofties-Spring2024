import loggerManager
import mongoengine
mongoengine.connect("projectsDb", alias="default") 
user_activity_logger = loggerManager.getUserLogs()
data=[{"log_description": log} for log in user_activity_logger]
print(data)