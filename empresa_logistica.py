#empresa logistica  cobra una tarifa base por kilogramo que depende  de la zona de destino.

print("tarifa base por kilo")

print("Ingrese el peso del paquete en Kg (puede usar decimales)")
Ing_Datos = float(input("Peso del paquete:"))
print(Ing_Datos)

print("Ingrese la zona de destino:(América,Europa,Resto del Mundo)")
Zona_D = input("Ingrese la Zona:")

if Zona_D == "América":
    #se multiplica el peso por $5.0 por kilo
    Resultado1 = Ing_Datos * 5.0 
    print ("total a pagar: $", Resultado1)
elif Zona_D == "Europa":
    #se multiplica el peso por $7.5 por kilo
    Resultado2 = Ing_Datos * 7.5
    print ("total a pagar: $", Resultado2)
elif Zona_D == "Resto del Mundo":
    #se multiplica el peso por $10 por kilo
    Resultado3 = Ing_Datos * 10
    print ("total a pagar: $", Resultado3)
else:
    print("Eso no existe te jalaste papà :P")