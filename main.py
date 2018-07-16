import sys
from contactInfo import ContactInfo
from businessCardParser import BusinessCardParser

input = open(sys.argv[1], 'r')
document = input.read()

bcp = BusinessCardParser()
# ci is a ContactInto object. 
ci = bcp.getContactInfo(document)

print()
print('Name: ' +ci.getName())
print('Email: ' +ci.getEmail())
print('Phone: ' +ci.getPhone())
print()
