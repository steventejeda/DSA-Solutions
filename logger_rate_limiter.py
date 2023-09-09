class Logger:
    def __init__(self):
        self.message_dict = {}
    
    def shouldPrintMessage(self, timestamp, message):
        if message not in self.message_dict:
            self.message_dict[message] = timestamp

            return True

        if timestamp - self.message_dict[message] >= 10:
            self.message_dict[message] = timestamp

            return True
        else:
            return False