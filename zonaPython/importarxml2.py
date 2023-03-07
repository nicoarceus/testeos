import xml.etree.ElementTree as ET
try:
    archivo_xml= open('C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/xmlPruebas/prueba4.xml')
    if archivo_xml.readable:
        dato_xml = ET.fromstring(archivo_xml.read())
        print("dato xml: ",dato_xml)
        nodoSetDTE = dato_xml.find('SetDTE')
        print("nodoSetDTE",nodoSetDTE)
        nodoDTE = dato_xml.find('DTE')
        nodoDocumento = nodoDTE.find('Documento')
        nodoEncabezado = nodoDocumento.find('Encabezado') 
        nodoEmisor = nodoEncabezado.find('Emisor')
        print('RznSoc',nodoEmisor.find('RznSoc').text)
    else:
        print(False)
except Exception as err:
    print(err)
finally:
    archivo_xml.close()