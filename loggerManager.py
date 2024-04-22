import projectManager
from userActivityLogger import UserActivityLogger


def getUserActivityLogger():
    userActivityLogger = UserActivityLogger.objects.first()

    # If no object is found, create a new one
    if userActivityLogger is None:
        userActivityLogger = UserActivityLogger()
        userActivityLogger.save()

    return userActivityLogger

def addUserActivity(activityLog):
     userActivityLogger = getUserActivityLogger()
     userActivityLogger.appendToDebugList(activityLog)
     userActivityLogger.save()
     return

def clearLog():
    userActivityLogger = getUserActivityLogger()
    userActivityLogger.clearLog()
    userActivityLogger.save()



    