#!/usr/bin/python
# Python program to parse a XML file

"""
Usage: Python-XML.py

Process a XML file and generates human readable content

Options
_______

-h or help		Displays this message
"""

import xml.etree.ElementTree as ET
from sys import argv, exit

if len(argv) > 1:
    print(__doc__)
    exit(0)

with open('F1-Grand-Prix-Australia.xml', 'r') as xmlFile:
    xmlTree = ET.parse(xmlFile)

print "\n"

datawrite = open('XMLResults.txt', 'w+')

for treeProperties in xmlTree.findall('.//'):
    for prop in treeProperties.findall('properties/property'):
        propName = prop.get('name')
        propValue = prop.get('value')
        if propName == 'startnumber' or propName == "team":
        break
        else:
            print "%s: %s" % (propName, propValue)
            datawrite.write('%s: %s' % (propName, propValue) + '\n')
		fastest = prop.findall('.//participant')
        if fastest:
            for f in fastest:
                fastestPerson = f.get('name')
                print "Fastest participant name:", fastestPerson
                datawrite.write('Fastest participant name: %s' % (fastestPerson) + '\n')

print "\n**Event participants**\n"
datawrite.write('\n*Event participants**\n')

for treeEvent in xmlTree.findall('.//'):
    for event in treeEvent.findall('event/event_participant'):
        participantNumber = event.get('number')
        participantName = event.find('participant').get('name')
        participantGender = event.find('participant').get('gender')

        print "Participant number: %s" % participantNumber
        datawrite.write('Participant number: %s' % (participantNumber) + '\n')		
        print "Name: %s, Gender: %s" % (participantName, participantGender)
        datawrite.write('Name: %s, Gender: %s' % (participantName.encode('utf8'), participantGender) + '\n')
		
		
        results = event.findall('.//result')
        if results:
            for result in results:
                resultName = result.get('result_code')
                resultValue = result.get('value')
                print "%s: %s" % (resultName, resultValue)
                datawrite.write('%s: %s' % (resultName, resultValue) + '\n')
				
        print "******************************************"
        datawrite.write('******************************************' + '\n')

datawrite.close()
xmlFile.close()
