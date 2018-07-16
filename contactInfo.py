import re

from decorators.name import Name
from decorators.email import Email
from decorators.phone import Phone

class ContactInfo():

    # Whenever a ContactInfo object is created, it creates three 'sub-objects'
    # that are hidden to the user. Those objects are Name, Email, and Phone. The
    # get methods in this class will get overridden in each of the 'sub-classes'
    def __init__(self, document):
        self.name = Name(document)
        self.email = Email(document)
        self.phone = Phone(document)
        
    def getName(self):
        return self.name.getName()

    def getEmail(self):
        return self.email.getEmail()
        
    def getPhone(self):
        return self.phone.getPhone()
        


