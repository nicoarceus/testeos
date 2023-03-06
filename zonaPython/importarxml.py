from xml.etree.ElementTree import parse
import os
os.system('cls')

estructura_xml  = parse("C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/ejemplo.xml") 
xml = parse("C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/archivo.xml")

# Obtiene el elemento raíz:

for item in estructura_xml.iterfind('record'):
    print(item.findtext('first_name'))
print("***************************")
import pandas as pd
first_name = []
last_name = []
gender = []
ip_address = []
for item in estructura_xml.iterfind('record'):
    first_name.append(item.findtext('first_name'))
    last_name.append(item.findtext('last_name'))
    gender.append(item.findtext('gender'))
    ip_address.append(item.findtext('ip_address'))
    
df = pd.DataFrame({'First name':first_name, 'Last name':last_name, 'Gender':gender, 'ip':ip_address})

print(df)
for item in xml.iterfind('Emisor'):
    print(item)
    print(item.findtext('CorreoEmisor'))

