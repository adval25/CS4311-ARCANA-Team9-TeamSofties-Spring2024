import mongoengine
class UserActivityLogger(mongoengine.Document):
    userDebugLog = mongoengine.ListField(default=[])


    def appendToDebugList(self,debugInfo):
        self.userDebugLog.append(debugInfo)

    def getUserDebugList(self):
        return self.userDebugLog

    def clearLog(self):
        self.userDebugLog = []