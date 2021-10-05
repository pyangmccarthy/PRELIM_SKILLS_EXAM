import xml.etree.cElementTree as et

tree=et.parse("covid_cases_xml.xml")
root=tree.getroot()
date_reported = []
countriesandterritories = []
number_of_cases = []
deaths = []

for date_reported in root.iter('dateRep'):
    date_reported.append(date_reported.text)
for countriesandterritories in root.iter('countriesAndTerritories'):
    countriesandterritories.append(countriesandterritories.text)
for number_of_cases in root.iter('cases'):
    number_of_cases.append(number_of_cases.text)
for deaths in root.iter('deaths'):
    deaths.append(deaths.text)

print(date_reported)
print(countriesandterritories)
print(number_of_cases)
print(deaths)

