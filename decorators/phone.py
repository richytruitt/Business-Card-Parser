import re

class Phone():
    
    def __init__(self, document):
        search = re.compile('(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})', re.MULTILINE)
        match = re.search(search, document)
        
        self.phone = match.group(0)

    def getPhone(self):
        return self.phone