import xml.etree.ElementTree as ET
try:
    archivo_xml= open('C:/Users/Interhouse HP/Desktop/zonaTesting/testeos/zonaPython/xmlPruebas/prueba4.xml')
    datosProov = []
    if archivo_xml.readable:
        dato_xml = ET.fromstring(archivo_xml.read())
        nodoSetDTE = dato_xml.find('{http://www.sii.cl/SiiDte}SetDTE')
        nodoDTE = nodoSetDTE.find('{http://www.sii.cl/SiiDte}DTE')
        nodoDocumento = nodoDTE.find('{http://www.sii.cl/SiiDte}Documento')
        nodoEncabezado = nodoDocumento.find('{http://www.sii.cl/SiiDte}Encabezado') 
        nodoEmisor = nodoEncabezado.find('{http://www.sii.cl/SiiDte}Emisor')
        print('Rut emisor = ',nodoEmisor.find('{http://www.sii.cl/SiiDte}RUTEmisor').text)
        print('Direccion Origen emisor = ',nodoEmisor.find('{http://www.sii.cl/SiiDte}DirOrigen').text)
        print('Comuna Origen emisor = ',nodoEmisor.find('{http://www.sii.cl/SiiDte}CmnaOrigen').text)
        print('RazonSocial = ',nodoEmisor.find('{http://www.sii.cl/SiiDte}RznSoc').text)
        print('giro emisor = ',nodoEmisor.find('{http://www.sii.cl/SiiDte}GiroEmis').text)
        datosProveedor=nodoEmisor.find('{http://www.sii.cl/SiiDte}RUTEmisor').text,nodoEmisor.find('{http://www.sii.cl/SiiDte}DirOrigen').text,nodoEmisor.find('{http://www.sii.cl/SiiDte}CmnaOrigen').text,nodoEmisor.find('{http://www.sii.cl/SiiDte}RznSoc').text,nodoEmisor.find('{http://www.sii.cl/SiiDte}GiroEmis').text
        print(datosProveedor)
    else:
        print(False)
except Exception as err:
    print(err)
finally:
    archivo_xml.close()