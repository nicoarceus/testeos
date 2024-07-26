import base64
import hmac
import hashlib

# Datos de ejemplo
rut_empresa = "78251940"
dv_empresa = "9"
convenio = "46424"
fecha = "2024/07/26"
llave_cifrado_base64 = f"Vk0rJrVZB5AT+qD8zxhTfSVJeNbONhoOCnAHhF/iTVFhovwtdG5+2DwcgsNdyMRsb4ReeP3g3KaTOwCY1OuMizy5qFf8UHjsif7SSm2jVpwKRxTh/TqswAlAt+gYJEsPOrzUiV8uV66sMvFo53/sezZAEPGktBCEN8ZnLV+mvticpDL7oO8Z6vPhnMxl/GNEIUDJ1kvJ5LuJ60w6+Nm7x9MY3XFi8ND/HgDKt4IUKRYQzsWThsNn8W31UrX6moSWqpTOnhsTzu9u6C538HRD+XKZI2UAx+2wSpSheWpSwgs3mF0mHtpaTI9dJnvBdSQbs7DQOrBHAtW170qLIoAJSg=="

# Generar el texto de entrada
texto_entrada = f"{rut_empresa};{dv_empresa};{convenio};{fecha}"

# Decodificar la llave de cifrado de Base64
llave_cifrado = base64.b64decode(llave_cifrado_base64)
# Crear el HMAC-SHA256
hmac_sha256 = hmac.new(llave_cifrado, texto_entrada.encode(), hashlib.sha256)

# Codificar el resultado en Base64
password_base64 = base64.b64encode(hmac_sha256.digest()).decode()

print(f"La contraseña de seguridad es: {password_base64}")


