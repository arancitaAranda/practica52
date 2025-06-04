import csv
import os

csv_file_path = os.path.join('practica52', 'datos.csv')

print(f"--- Manipulación de datos.csv ---")

try:
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader) 
        data_csv = list(reader) 

    print(f"Encabezado del CSV: {header}")
    print(f"Primeras 5 filas del CSV:")
    for row in data_csv[:5]:
        print(row)

    
    try:
        
        columna_a_filtrar_nombre = 'Estado' 
        
        if columna_a_filtrar_nombre in header:
            idx_columna_filtro = header.index(columna_a_filtrar_nombre)
            valor_a_filtrar = 'Activo' 
            print(f"\nFiltrando filas donde la columna '{columna_a_filtrar_nombre}' es '{valor_a_filtrar}':")
            filas_filtradas = [row for row in data_csv if len(row) > idx_columna_filtro and row[idx_columna_filtro] == valor_a_filtrar]

            if filas_filtradas:
                for row in filas_filtradas[:5]: 
                    print(row)
                print(f"... y {len(filas_filtradas)} filas en total cumplen el criterio.")
            else:
                print(f"No se encontraron filas con '{columna_a_filtrar_nombre}' igual a '{valor_a_filtrar}'.")
        else:
            print(f"Columna '{columna_a_filtrar_nombre}' no encontrada en el encabezado del CSV. No se pudo filtrar.")

    except IndexError:
        print("Error: El índice de columna para filtrar está fuera de rango. Revisa tu CSV.")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el filtrado: {e}")

except FileNotFoundError:
    print(f"Error: El archivo '{csv_file_path}' no se encontró. Asegúrate de que esté en la carpeta 'practica52'.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo CSV: {e}")

print(f"\nBeneficios observados para CSV en este escenario:")
print(f"- **Facilidad de Lectura/Escritura**: El módulo `csv` de Python facilita la lectura y escritura de datos tabulares de forma sencilla y directa.")
print(f"- **Eficiencia en Datos Tabulares**: Es muy eficiente para almacenar y procesar grandes volúmenes de datos donde cada registro tiene la misma estructura de columnas.")
print(f"- **Compatibilidad**: Es universalmente compatible con hojas de cálculo y muchas herramientas de análisis de datos.")
print(f"")