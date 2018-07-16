import re

class Email():
    
    def __init__(self, document):
        search = re.compile('\\S+@.+', re.MULTILINE)
        match = re.search(search, document)
        self.email = match.group(0)

    def getEmail(self):
        return self.email