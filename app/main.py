import pandas as pd
import requests
import json
import os

def download_google_drive_file(google_drive_file, destination):
    """
    Descarga un archivo público de Google Drive.
    """
    response = requests.get(google_drive_file, stream=True)
    if response.status_code == 200:
        with open(destination, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Archivo descargado en: {destination}")
    else:
        raise Exception(f"No se pudo descargar el archivo. Código de estado: {response.status_code}")

def excel_to_json(excel_path, json_path):
    """
    Convierte un archivo Excel en formato JSON.
    """
    try:
        # Leer el archivo Excel
        excel_data = pd.read_excel(excel_path, sheet_name=None, engine="openpyxl")
        # Crear un diccionario para todas las hojas
        data = {sheet: df.to_dict(orient="records") for sheet, df in excel_data.items()}
        # Guardar como JSON
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"Archivo JSON creado en: {json_path}")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")

if __name__ == "__main__":
    # Enlace directo de Google Drive (export=download&id=<ID>)
    google_drive_file = "https://docs.google.com/uc?export=download&id=19_hbkiN87dlbxmWuaBWnfYFekzZ7IxS2"
    excel_file_path = "./temp/archivo_temporal.xlsx"  # Nombre temporal del archivo descargado
    json_file_path = "../data/productos.json" # Nombre del archivo JSON

    try:
        # Descargar el archivo desde Google Drive
        download_google_drive_file(google_drive_file, excel_file_path)
        
        # Convertir el archivo Excel a JSON
        excel_to_json(excel_file_path, json_file_path)
        
    finally:
        # Eliminar el archivo temporal Excel si existe
        if os.path.exists(excel_file_path):
            os.remove(excel_file_path)
            print(f"Archivo temporal eliminado: {excel_file_path}")
