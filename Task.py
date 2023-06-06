import json
import yaml
import os
import sys
import xml.etree.ElementTree as ET

source_path =  sys.argv[1] # ŚCIEZKA ŹRÓDŁOWA
dest_path = sys.argv[2] #ściezka docelowa

source_ext = os.path.splitext(source_path)[1] # czy źródłowa to json, yaml, xml 
dest_ext = os.path.splitext(dest_path)[1] # czy docelowa to json, yaml, xml

def odczyt_json(source_path):
    try:
        with open(source_path, 'r') as file:
            tekst = json.load(file)
            #json_zamiana(tekst, dest_ext, dest_path) # Kontynuacja do kolejnego Taska
            return tekst

    except FileNotFoundError:
        print(f"błąd nie znaleziono pliku")
        return None
    except json.JSONDecodeError:
        print(
            f"Nie poprawna składnia tekstu pliku {source_path} prosze ją poprawić {str(json.JSONDecodeError)}")
        return None



if os.path.exists(source_path) == True and os.path.exists(dest_path) == True:
    if source_ext == ".json":
        odczyt_json(source_path)

if os.path.exists(source_path) != True or os.path.exists(dest_path) != True:
    print("poszczególne pliki nie istnieją albo ścieżki nie są poprawne")
    input("Naciśnij enter aby zakończyć")
if source_path == dest_path:
    print(f"BŁĄD ścieżka początkowa {source_path} i ścieżka końcowa {dest_path} są identyczne")
    input("Naciśnij enter aby zakończyć")