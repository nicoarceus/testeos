from xml.etree.ElementTree import parse
import os
os.system('cls')

estructura_xml  = parse("C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/xmlPruebas/prueba2.xml") 
root = estructura_xml.getroot()
for child in root:
    print(child.tag, child.attrib)
for movie in root.iter('movie'):
    print(movie.attrib)
xml = parse("C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/xmlPruebas/prueba5.xml")
raizXml=xml.getroot()
for child in raizXml:
    print(child.tag,child.attrib,child.tail)
for child in raizXml.iter('setDTE'):
    print(child.attrib)
xml = parse("C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/xmlPruebas/prueba4.xml")
raizXml=xml.getroot()
for child in raizXml:
    print(child.tag,child.attrib,child.tail)
for child in raizXml.iter('setDTE'):
    print(child.attrib)
xml = parse("C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/xmlPruebas/prueba3.xml")
raizXml=xml.getroot()
for child in raizXml:
    print(child.tag,child.attrib,child.tail)
for child in raizXml.iter('setDTE'):
    print(child.attrib)
xml = parse("C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/xmlPruebas/prueba1.xml")
raizXml=xml.getroot()
for child in raizXml:
    print(child.tag,child.attrib,child.tail)
for child in raizXml.iter('setDTE'):
    print(child.attrib)