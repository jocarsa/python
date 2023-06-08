import tkinter as interfaz

def calcula():
    print("La base imponible es de: "+baseimponible.get())
    print("El porcentaje de IRPF es de: "+irpf.get())
    print("El porcentaje de IVA es de: "+iva.get())
    totalnumero = float(baseimponible.get())
    irpfnumero = float(irpf.get())/100
    print("El irpf es: "+str(irpfnumero))
    print("La cantidad de IRPF es:"+str(totalnumero*irpfnumero))
    totalbase = totalnumero - totalnumero*irpfnumero
    ivanumero = float(iva.get())/100
    print("Total IVA: "+str(totalbase*ivanumero))
    totalfinal = totalbase*ivanumero + totalbase
    print(totalfinal)

raiz = interfaz.Tk()
raiz.geometry("600x600+50+50")
raiz.title("Calculadora Freelance")
raiz.iconbitmap("icono.ico")

baseimponible = interfaz.StringVar(raiz)
irpf = interfaz.StringVar(raiz)
iva = interfaz.StringVar(raiz)

panel = interfaz.Frame()
panel.pack()

imagen = interfaz.PhotoImage(file="titulo.png")
interfaz.Label(panel, image=imagen).pack()

interfaz.Label(panel,text="Introduce la base imponible").pack(pady=3)
interfaz.Entry(panel, width= 40,textvariable=baseimponible,justify="right").pack(pady=3)
interfaz.Label(panel,text="Introduce el impuesto 1 (IRPF)").pack(pady=3)
interfaz.Entry(panel, width= 40,textvariable=irpf,justify="right").pack(pady=3)
interfaz.Label(panel,text="Introduce el impuesto 2 (IVA)").pack(pady=3)
interfaz.Entry(panel, width= 40,textvariable=iva,justify="right").pack(pady=3)
interfaz.Button(panel,width=40,text="¡Calcula!",command=calcula).pack(pady=3)

