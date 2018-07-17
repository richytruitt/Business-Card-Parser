from contactInfo import ContactInfo

class BusinessCardParser():
    
    # this method returns an object of Contactinfo passing the 
    # text block as parameter
    def getContactInfo(self, document):
        return ContactInfo(document)