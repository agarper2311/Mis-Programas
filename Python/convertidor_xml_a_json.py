import xml.etree.ElementTree as ET
import json
import tkinter as tk
from tkinter import filedialog

def xml_to_dict(element):
    """
    Convierte un elemento XML en un diccionario.
    """
    if not element:
        # Si no tiene hijos, retorna su texto o vacío si es None
        return element.text if element.text else ''

    result = {}
    for child in element:
        child_result = xml_to_dict(child)

        if child.tag not in result:
            result[child.tag] = child_result
        else:
            if type(result[child.tag]) is list:
                result[child.tag].append(child_result)
            else:
                result[child.tag] = [result[child.tag], child_result]

    return result

def validate_and_convert_xml_to_json(xml_file, json_file):
    """
    Valida un archivo XML y lo convierte a JSON.
    """
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        data = xml_to_dict(root)

        with open(json_file, 'w') as jsonf:
            json.dump(data, jsonf, indent=4)

        return True
    except ET.ParseError as e:
        print(f'Error al parsear XML: {e}')
        return False
    except Exception as e:
        print(f'Error: {e}')
        return False

# Uso del programa
xml_file = 'ejemplo.xml'
json_file = 'salida.json'

if validate_and_convert_xml_to_json(xml_file, json_file):
    print(f'Archivo XML convertido a JSON y guardado en {json_file}')
else:
    print('Fallo la validación o conversión del archivo XML.')

def open_file_dialog():
    """
    Abre un diálogo para seleccionar un archivo XML.
    """
    file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    if file_path:
        json_file = file_path.rsplit('.', 1)[0] + '.json'
        if validate_and_convert_xml_to_json(file_path, json_file):
            print(f'Archivo XML convertido a JSON y guardado en {json_file}')
        else:
            print('Fallo la validación o conversión del archivo XML.')

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Convertidor XML a JSON")

# Botón para abrir el diálogo de selección de archivo
open_button = tk.Button(root, text="Abrir archivo XML", command=open_file_dialog)
open_button.pack(pady=20)

# Iniciar el bucle de eventos de Tkinter
root.mainloop()