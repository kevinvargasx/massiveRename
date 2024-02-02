import os

def rename(directorio, parte_antigua, parte_nueva):
    for archivo in os.listdir(directorio):
        # Construir la ruta completa del archivo
        ruta_antigua = os.path.join(directorio, archivo)

        # Verificación si es un archivo
        if os.path.isfile(ruta_antigua):
            # Verificar si la parte antigua está en el nombre del archivo
            if parte_antigua in archivo:
                # Reemplazar la parte antigua por la nueva en el nombre del archivo
                nuevo_nombre = archivo.replace(parte_antigua, parte_nueva)

                # Construir la ruta completa del nuevo archivo
                ruta_nueva = os.path.join(directorio, nuevo_nombre)

                # Renombrar el archivo
                os.rename(ruta_antigua, ruta_nueva)
                print(f"Archivo renombrado: {ruta_antigua} -> {ruta_nueva}")

if __name__ == "__main__":
    # ruta
    directorio_a_renombrar = "D:/ejemplo/directory"

    # parte antigua
    parte_antigua = "old"

    # parte nueva
    parte_nueva = "new"

    # Llamado de la función
    rename(directorio_a_renombrar, parte_antigua, parte_nueva)
