

# print()

#print("mi", "nombre", "es", "Johan", sep= "\n")

import time 

for i in range(3):
    print(f"Cargando {i}...", end = "", flush = True) # Para no guardar nada en el buffer (flush =  True)
    time.sleep(1)