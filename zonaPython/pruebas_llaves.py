import base64
import hmac
import hashlib
import datetime
import jks

def extraer_llave_cifrado(jks_path, jks_password):
    try:
        # Cargar el archivo JKS
        keystore = jks.KeyStore.load(jks_path, jks_password)
        
        # Imprimir información sobre el keystore
        print(f"Keystore cargado: {keystore}")
        print(f"Claves privadas en el keystore: {keystore.private_keys}")
        print(f"Certificados en el keystore: {keystore.certs}")
        print(f"Claves secretas en el keystore: {keystore.secret_keys}")
        for alias, secret_key in keystore.secret_keys.items():
            print(f"Alias: {alias}")
            print(f"Clave secreta: {secret_key}")
            key = secret_key.key
            # Codificar la llave en base64
            llave_cifrado_b64 = base64.b64encode(key).decode('utf-8')
            print(llave_cifrado_b64)
            return llave_cifrado_b64
        
        print("Error: No se encontró ninguna clave privada en el keystore.")
        return None
    except jks.util.KeystoreSignatureException:
        print("Error: Contraseña del keystore incorrecta.")
    except jks.KeystoreException:
        print("Error: No se pudo cargar el keystore. Verifique el archivo y la contraseña.")
    except KeyError:
        print("Error: Alias no encontrado en el keystore.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def generar_contraseña(rut_empresa, dv, convenio, llave_cifrado_b64):
    # Decodificar la llave de cifrado desde base64
    llave_cifrado = base64.b64decode(llave_cifrado_b64)
    
    # Generar la fecha actual en el formato yyyy/mm/dd
    fecha_actual = datetime.datetime.now().strftime('%Y/%m/%d')
    
    # Crear el texto de entrada
    texto_entrada = f"{rut_empresa};{dv};{convenio};{fecha_actual}"
    
    # Generar HMAC-SHA256
    hmac_sha256 = hmac.new(llave_cifrado, texto_entrada.encode('utf-8'), hashlib.sha256).digest()
    
    # Codificar el resultado en base64
    contraseña_seguridad = base64.b64encode(hmac_sha256).decode('utf-8')
    
    return contraseña_seguridad

# Ejemplo de uso
jks_path = "C:/tools/respaldoBaseDatos/cliente5509_KeystoreHash.jks"  
jks_password = "hAHnZp855kEs"  # Contraseña del JKS
key_password = "AALOHA"  # Contraseña de la llave

# Extraer la llave de cifrado en base64
llave_cifrado_b64 = extraer_llave_cifrado(jks_path, jks_password)

print(llave_cifrado_b64)
# Datos para generar la contraseña
rut_empresa = "78251940"
dv_empresa = "9"
convenio = "46424"
fecha = "2024/07/26"

# Generar la contraseña de seguridad
contraseña = generar_contraseña(rut_empresa, dv_empresa, convenio, llave_cifrado_b64)
print("Contraseña de seguridad:", contraseña)
