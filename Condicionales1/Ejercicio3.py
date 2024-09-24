calificacion = float(input("Ingrese tu calificacion"))

calificacion = round (calificacion)
print(calificacion)

if calificacion >= 60 and calificacion <= 100:
    print("Aprobo")
elif calificacion >= 0 and calificacion <60:
    print("Reprobo")
else:
    print("La calificacion no es valida")
