#Aqui lo que está pasando es que python reconoce los folders cercanos como packages por que contienen el script con el nombre __init__.py en ellos, asi que me permite importar de el packete primario y el secundario de la siguiente manera, al igual que me permite llamar las funciones en estos scripts con el syntax que se ve:

from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

#Aqui <------------<<<
some_main_script.report_main()

mysubscript.sub_report()

#simplemente lo que estpy haciendo aqui es poner todo lo que esta en otro codigo o "module" a otra pagina, no tiene nada de complicado, pero tengo que definir las cosas muy bien para que funcionen
from Intro import my_func

my_func() 
print("Holaa")



