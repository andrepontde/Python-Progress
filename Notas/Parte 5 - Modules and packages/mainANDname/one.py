def func():
    print("func() ran in one.py")

print("top-level print inside of one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
    
#Lo que hacen estas funciones de __name__ == es que checan si se está ejecutando el codigo directamente o si es se está ejecutando desde otro codigo, aquí si en la terminal ejecuto ope.py va a imprimir "one.py is being run directly" si lo hago desde two.py donde esta importado, va a imprimir "one.py is being imported into another module"

