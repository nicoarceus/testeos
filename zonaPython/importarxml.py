from xml.dom import minidom

doc = minidom.parse("testeos/zonaPython/ejemplo.xml")

nombre = doc.getElementsByTagName("nombre")[0]
print(nombre.firstChild.data)

empleados = doc.getElementByTagName("empleado")
for empleado in empleados:
    sid = empleado.getAttribute("id")
    username = empleado.getElementsByTagName("username")[0]
    password = empleado.getElementsByTagName("password")[0]
    print("id:%s " % sid)
    print("username:%s" % username.firstChild.data)
    print("password:%s" % password.firstChild.data)
