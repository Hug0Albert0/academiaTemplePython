

salario_mensual = 10000

if salario_mensual > 10000:
   print("Ganas mas que muchos otros devs")
elif salario_mensual < 10000:
   print("Ganas menos que muchos otros devs")
else:
   print("Ganas 10k, lo suficiente")


validacion = True
error = False

if validacion or error:
   print("Hay al menos una sentencia correcta")
else:
   print("Hay al menos una declaracion falsa")

lista = [1,2, 6, 9]

for elemento in lista:
   print(elemento)