from contactInfo import ContactInfo

class BusinessCardParser():
    
    # this method returns an object of Contact info passing the 
    # text block as parameter
    def getContactInfo(self, document):
        return ContactInfo(document)