"""
La función drops retorna un string vacío en caso de no cumplir la condición
o retornará el sonido de las gotas de agua
"""
def drops(num):
    drop = {3:'Plic',5:'Plac',7:'Ploc'}
    value = ''
    for keys,song in drop.items():
        if num % keys == 0:
            value += song
    return '"'+str(num)+'"' if (value == '') else '"'+value+'"'

#llamada a la función drop e impresión de resultados
print("Result: ",drops(28))
print("Result: ",drops(30))
print("Result: ",drops(34))


    
    
