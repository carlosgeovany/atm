#!/usr/bin/python

from time import gmtime, strftime

print ("Bienvenido a su cajero automático...")
print ("Ingrese su contraseña, solo tiene 3 intentos")

pwd = "1235"
password = input("contraseña: ")
saldo = 1000

flag = 0
intentos = 3
historico = []

if pwd != password:
	while flag <  2:
		flag += 1
		intentos -= 1
		input(f"contraseña incorrecta, vuelve a intentarlo, te quedan {intentos} intentos...")
	print("Lo sieto ha superado el límete máximo de intentos. Finalizando el programa")

if pwd == password:
	print ("Bienvenido Carlos")
	print ("====MENU====")
	ans = True
	while ans:
	    print ("""
		1.Consultar saldo
		2.Retiro de efectivo
		3.Histórico de movimientos
		4.Salir
	    """)
	    ans = input("Selecciona la opción deseada: ") 

	    if ans == "1":
	    	print ("\n====Consulta de Saldo====\n")
	    	print (f"Su actual es de ${saldo} pesos")
	    	print ("""
	    		1.Volver al menú principal
	    		2.Salir
	    	""")
	    	opc = input ("Selecciona la opción deseada: ")
	    	if opc == "1":
	    		pass
	    	elif opc == "2":
	    		print("\nGracias por usar su cajero automático, hasta luego")
	    		break
	    	else:
	    		print("\nOpción inválida, vuelve a Menú principal")

	    elif ans=="2":
	    	print("\n====Retiro de efectivo====\n")
	    	if saldo == 0:
	    		print("Lo sentimos su saldo actual es de $0 pesos")
	    	else:
		    	try:
		    		retiro = int(input("¿Qué cantidad desea retirar? "))
		    		if retiro > saldo:
		    			print("Fondos insuficientes...")
		    		else:		    			
		    			historico.append([saldo, retiro, strftime("%Y-%m-%d %H:%M:%S", gmtime())])
		    			saldo -= retiro
		    			print("Retiro realizado con éxito")
		    	except:
		    		print("Introduce solo valores numéricos enteros...")
	    	print ("""
	    		1.Volver al menú principal
	    		2.Salir
	    	""")
	    	opc = input ("Selecciona la opción deseada: ")
	    	if opc == "1":
	    		pass
	    	elif opc == "2":
	    		print("\nGracias por usar su cajero automático, hasta luego")
	    		break
	    	else:
	    		print("\nOpción inválida, vuelve a Menú principal")
            

	    elif ans=="3":
	    	print("\n====Histórico de movimientos====\n")
	    	if len(historico) == 0:
	    		print("Cuenta sin movimientos")
	    	else:
	    		for mov in historico:
	    			print(f"Saldo inicial:\t{mov[0]}\t|\tRetiro:\t {mov[1]}\t|\tSaldo Final:\t {mov[0]-mov[1]}\t|\tFecha:\t {mov[2]}")
	    	print ("""
	    		1.Volver al menú principal
	    		2.Salir
	    	""")
	    	opc = input ("Selecciona la opción deseada: ")
	    	if opc == "1":
	    		pass
	    	elif opc == "2":
	    		print("\nGracias por usar su cajero automático, hasta luego...")
	    		break
	    	else:
	    		print("\nOpción inválida, vuelve a Menú principal")

	    elif ans=="4":
	    	print("\nGracias por usar su cajero automático, hasta luego")
	    	break
	    elif ans !="":
	    	print("\nOpción inválida, inténtelo de nuevo...") 


