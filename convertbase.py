#!/usr/bin/python
import time

def dec2any():
    dec = float(input("quanl valor decimal vc deseja converter??(por favor, digite um numero qualquer!) "))
    base_final = int(input("qual a base final? "))
    limite = int(input("qual o limete que deseja parar caso gere uma dizima? "))
    count=0
    base_final = int(base_final)
    dec = float(dec)
    inteiro = int(dec)
    inddot = str(dec).find(".")
    imprimir = ""
    aux = 0.0
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numero_final_temp = []
    numero_final_frac = []
    numero_final = ''
#    print("parte inteira=%d",inteiro)
    while(inteiro!=0):
	if(inteiro<base_final):
		numero_final_temp.append(dic[inteiro])
		break	
	numero_final_temp.append(dic[inteiro%base_final])
	inteiro = inteiro/base_final
#	print(inteiro)
	time.sleep(0.1)
	count=count+1
	if(count==10):
		break

#    print(numero_final_temp)
    count = 0
    if (inddot):
	numero_final_frac.append(".")
#	print("dec= %f",dec)
	frac = float(str(dec)[inddot:])
#	print("frac= %f",frac)
	while(frac!=0.0):
		aux = frac*base_final
		numero_final_frac.append(str(int(aux)))
		frac = float(str(aux)[str(aux).find("."):])
#		print(frac)
		count=count+1
		if(count==limite):
			break
	
    numero_final_temp.reverse()
#    print(numero_final_temp)
#    print(numero_final_frac)
    for a in numero_final_temp:
	imprimir = imprimir + a
    for a in numero_final_frac:
	imprimir = imprimir + a
    print("o numero "+str(dec)+ " na base " +str(base_final) +" eh "+str(imprimir))
#numero_final_temp.append(int(dec)%base_final)
    

dec2any()

##str(dec)._len_().)
