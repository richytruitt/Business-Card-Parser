import re

class Phone():
    
    def __init__(self, document):
        phonePattern = re.compile(r'(.*(\d\d\d)?-?\d\d\d-?\d\d\d\d)')

        phoneIncluders = ['TEL', 'PHONE', 'CELL', 'C']
        self.phone=''

        #Returns a list of tuples. Each tuple includes the line that includes a phone number. 
        result = phonePattern.findall(document)
        #the resulting tuple returns an empty string as index [1]. So I remove the empty string using this
        result = [x[:-1] for x in result] 

        #before running it through the algorithm to test against the phone
        # inclusion list, I save the phone number to a variable 
        # just incase it doesn't have something to test phone numbers
        self.phone = result[0][0]
        
        # for each item in the regex result, and for each item in the inclusion list
        # if the result index includes one of the items from the inclusion list
        # then it will set the saved phone number to the index value after the length 
        # of the includer string +1
        for i in result:
            for x in phoneIncluders:
                if x in i[0].upper():
                    self.phone = i[0][len(x)+1:]


    def getPhone(self):
        # return self.phone
        return self.phone