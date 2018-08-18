from os import listdir
from os.path import isfile, join
import pandas as pd
import csv

mi_path = "."
solo_archivos = [
    cosa for cosa listdir(mi_path)
    if isfile(join(mi_path,f))]
for archivo in solo_archivos:
    print(archivo)

file = open("eggs.csv","w", newline ='')
file.close()
