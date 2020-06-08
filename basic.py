#En Python podemos declarar las variables sin especificar de que tipo son,
#esto es detectado automaticamente, sin usar punto y coma al final

primero = 50
segundo = 20

#Al declarar dos variables cuyos valores son integer, se detectan como tales
#y podemos realizar las operaciones matematicas basicas con ellos de la siguiente forma

print(primero + segundo) # Suma

print(primero * segundo) #Multiplicacion

print(primero / segundo) #Division

print(primero % segundo) #Modulo o cociente de division

print(primero - segundo) #Resta

print(primero ** segundo) #Potencia

#En Python como en la mayoria de lenguajes de programacion, pomemos encontrar
#fidelidad a la jerarquia de operaciones matematicas
print( (20 * 50) / (4 - 1))