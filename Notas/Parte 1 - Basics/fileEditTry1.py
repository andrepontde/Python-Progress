import os


print(os.getcwd())

# os.chdir(path)

with open(r"C:\Users\andre\OneDrive\Programming\Python\Notas\Parte 1 - Basics\algoDeTexto.py") as textFile:
    text = textFile.read()

print(text)