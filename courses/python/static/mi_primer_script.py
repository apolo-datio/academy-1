import math
     
print("Hola gente del curso de Python")
print("¿Cuántos sois hoy en clase?")

number = input()
number = int(number)
root = math.sqrt(number)

print("Por cierto, la raiz de %i es %f" %(number, root))
