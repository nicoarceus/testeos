from xml.etree.ElementTree import parse

estructura_xml  = parse("C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/prueba2.xml") 
root = estructura_xml.getroot()

for child in root:
    print(child.tag, child.attrib)
for movie in root.iter('movie'):
    print(movie.attrib)
   