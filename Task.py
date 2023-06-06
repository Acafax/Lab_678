import json
import yaml
import os
import sys
import xml.etree.ElementTree as ET

source_path =  sys.argv[1] # ŚCIEZKA ŹRÓDŁOWA
dest_path = sys.argv[2] #ściezka docelowa

source_ext = os.path.splitext(source_path)[1] # czy źródłowa to json, yaml, xml 
dest_ext = os.path.splitext(dest_path)[1] # czy docelowa to json, yaml, xml