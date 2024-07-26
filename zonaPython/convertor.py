import codecs

def utf8_to_ansi(text_utf8):
    # Decodifica el texto desde UTF-8 a Unicode
    text_unicode = text_utf8.decode('utf-8')
    # Codifica el texto desde Unicode a ANSI (Windows-1252)
    text_ansi = text_unicode.encode('cp1252', errors='replace')
    return text_ansi

# Ejemplo de uso:
texto_utf8 = "Hola, ¿cómo estás? ¡Todo bien!"
# Asegúrate de que el texto esté en formato bytes
texto_utf8_bytes = texto_utf8.encode('utf-8')

texto_ansi = utf8_to_ansi(texto_utf8_bytes)
print(texto_ansi)
