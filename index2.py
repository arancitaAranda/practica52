import json
import os
json_file_path = os.path.join('practica52', 'datos.json')

print(f" Manipulación de datos.json ")
try:
    with open(json_file_path, mode='r', encoding='utf-8') as file:
        data_json = json.load(file)

    print(f"Tipo de datos cargados del JSON: {type(data_json)}")

    if isinstance(data_json, list) and data_json:
        print(f"Primer elemento del JSON (si es una lista):")
        print(json.dumps(data_json[0], indent=2)) 

        
        if 'id' in data_json[0]:
            print(f"\nAccediendo al 'id' del primer elemento: {data_json[0]['id']}")
        if 'nombre' in data_json[0]:
            print(f"Accediendo al 'nombre' del primer elemento: {data_json[0]['nombre']}")
        
        
        if 'contacto' in data_json[0] and isinstance(data_json[0]['contacto'], dict):
            if 'email' in data_json[0]['contacto']:
                print(f"Accediendo al email anidado: {data_json[0]['contacto']['email']}")

    elif isinstance(data_json, dict):
        print(f"Contenido completo del JSON (si es un diccionario):")
        print(json.dumps(data_json, indent=2)) # Muestra el diccionario completo formateado
        
        if 'configuracion' in data_json:
            print(f"\nAccediendo a la clave 'configuracion':")
            print(json.dumps(data_json['configuracion'], indent=2))

    else:
        print("El contenido del JSON no es ni una lista ni un diccionario (o está vacío).")

except FileNotFoundError:
    print(f"Error: El archivo '{json_file_path}' no se encontró. Asegúrate de que esté en la carpeta 'practica52'.")
except json.JSONDecodeError:
    print(f"Error: El archivo '{json_file_path}' no es un JSON válido.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo JSON: {e}")

print(f"\nBeneficios observados para JSON en este escenario:")
print(f"- **Representación de Datos Complejos**: JSON es excelente para datos jerárquicos y anidados, como objetos con propiedades complejas y listas dentro de objetos.")
print(f"- **Intercambio de Datos en Web**: Es el formato estándar para APIs web, lo que facilita la integración con aplicaciones frontend (JavaScript) y backend.")
print(f"- **Legibilidad Humana**: A pesar de su complejidad, su estructura de clave-valor lo hace relativamente fácil de leer y entender para los desarrolladores.")
print(f"")