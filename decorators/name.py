import re

class Name():
    
    def __init__(self, document):

        # this is the list of exclusions to test against when i perform the 'findall'
        # query. TODO: break these out into a config file
        nameExclusions = ['ENGINEER', 'STREET', 'ROAD', 'SOFTWARE', 'DEVELOPER', 'INC', 'TECHNOLOGIES', 'COMPANY', 'SENIOR', 'LTD']
        
        name_regex = '[A-Za-z]+\s[A-Za-z]+'

        # starting to loop through the queries against the regex
        for name in re.findall(name_regex, document):
            # breaking each result into a list of 2
            nameParts = name.upper().split(" ")
            # temp list to hold matches against the nameExclusions list
            not_name = []
            for i in nameExclusions:
                for n in nameParts:
                    if i == n:
                        not_name.append(i)

            # if the list is empty, that means there were no business or address
            # associations, thus a name match. if the list size was zero
            # it sets the variable, and returns it to it proper capitalization
            if len(not_name) == 0:
                self.name = nameParts
                self.name = ' '.join(self.name)
                self.name = ' '.join(i.capitalize() for i in self.name.split(' '))

    def getName(self):
        return self.name