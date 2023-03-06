from xml.etree.ElementTree import parse
import os
os.system('cls')

estructura_xml  = parse("C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/xmlPruebas/ejemplo.xml") 
xml = parse("C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/xmlPruebas/pruebas1.xml")
raizXml=xml.getroot()
# Obtiene el elemento raíz:
print(estructura_xml)
print(xml)
for item in estructura_xml.iterfind('record'):
    print(item.findtext('first_name'))
print("***************************")
for movie in raizXml:
    print(movie.attrib)
import pandas as pd
first_name = []
last_name = []
gender = []
ip_address = []
email=[]
for item in estructura_xml.iterfind('record'):
    first_name.append(item.findtext('first_name'))
    last_name.append(item.findtext('last_name'))
    gender.append(item.findtext('gender'))
    ip_address.append(item.findtext('ip_address'))
    email.append(item.findtext('email'))
    
df = pd.DataFrame({'First name':first_name, 'Last name':last_name, 'Gender':gender, 'ip':ip_address,'email':email})

    
print(df)


