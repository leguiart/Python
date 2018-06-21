pago=0
while pago==0:
    try:
        horas= raw_input("Cuantas horas trabajaste?")
        salario= raw_input("Cual es tu salario?")
        pago= int(horas) * float (salario)
    
    except:
        horas= "0"
        salario= "0"
        pago=0
        print "Ha habido un error, porfavor introduzca unicamente valores numericos"

horasbono=40
salariobono=0        
if horas>40:
    salario= float(salario)
    horas=int(horas)
    horasbono= horas-horasbono
    print "Horas extra trabajadas:",horasbono
    salariobono= salario*horasbono
    salariobono= salariobono*1.5
    print "Bono de productividad:",salariobono
    horas=40
    pago= (horas*salario)+salariobono
    
else:
    print "No has recibido bono de productividad"
    
print "Pago total:", pago #holiiiiii