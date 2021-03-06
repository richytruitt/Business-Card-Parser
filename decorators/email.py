import re

class Email():
    
    def __init__(self, document):
        search = re.compile('[a-zA-Z0-9\S]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+', re.MULTILINE)
        match = re.search(search, document)
        self.email = match.group(0)

    def getEmail(self):
        return self.email