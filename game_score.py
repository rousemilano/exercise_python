score = [5,2,8,1,20] #Lista original
scores = score.copy() #Copia de la lista original


# La función que se encarga de retornar el puntaje maximo de la lista
def getTheThreeHigher(listScores):
    value = max(listScores)
    listScores.remove(value)
    return value

"""
Se usa la Comprensión de listas para obtener una nueva lista que contiene los 3
puntajes más altos
"""
theTreeScoreHigher = [getTheThreeHigher(scores) for n in range(3)]

#función que retorna el puntaje más alto de la lista
scoreMax = lambda scoreM: max(scoreM)

#función que retorna el último puntaje agregado
scoreLastAdd = lambda scoreL: scoreL[-1:]

#imprimiendo resultados y llamadas de las funciones

print ("Los tres puntajes más altos: ",theTreeScoreHigher)
print ("Puntaje más alto: ",scoreMax(score))
print ("Última puntuación agregada: ",scoreLastAdd(score))

