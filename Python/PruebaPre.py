## Software de cotizacion para etiquetas
## Para Pragmatic SAS
## Por Ilse Villalba M.

from tkinter import *
from tkinter import ttk
import TiposPapel
import TiposMaquinas
import CostoImpresion
from tkinter import messagebox

global contador
contador=0
tacha=0
cotizaciones={}


def duplicarcampo():
    global contador

    variableCotizacion = StringVar()
    labelCotizacion = Label(ventanaPrincipal, text="Cantidad etiquetas cotizacion numero " + str (contador+1) ).grid(row=(10+contador),column=0)
    campoCotizacion = Entry(ventanaPrincipal,textvariable=variableCotizacion).grid(row=(10+contador),column=1)
    contador=contador+1
    cotizaciones[contador]=variableCotizacion

def Calcular():
    global tacha
    
    Nombre = variableNombre.get()
    Tintas = int(variableTintas.get())
    Ancho = float (variableAncho.get())
    Largo = float (variableLargo.get())
    TipoImpresion= int(variableTipoImpresion.get())
    TipoPapel = variableTipoPapel.get()
    Maquina = variableMaquina.get()
    Desperdicio = float(variableDesperdicio.get())/100
    Utilidad = float(variableUtilidad.get())/100

    precio_papel=TiposPapel.precioPapel(TipoPapel)

    mensaje=('Cliente: '+ Nombre + "\n" +'Cantidad de tintas: '+ str(Tintas) +"\n"+ 'Tamaño de etiqueta: '+ str(Ancho) +'x'+ str(Largo)+'mm'+"\n"+"\n")


    for i in cotizaciones:
        cantidadEtiquetas=int (cotizaciones[i].get())
        tiempo_impresion=TiposMaquinas.tiempoImpresion(Ancho,Largo,cantidadEtiquetas,Maquina)
        costo_impresion= CostoImpresion.costoImpresion (TipoImpresion,Ancho,Largo,cantidadEtiquetas,precio_papel,tiempo_impresion,Desperdicio,Tintas,Maquina)
        

        mensaje=mensaje+"\n"+'Cotizacion'+str(i)+"\n"+('Cantidad de etiquetas: '+str(cantidadEtiquetas)+"\n"+'Precio de etiquetas: '+str(round(costo_impresion))+"\n")
        

    messagebox.showinfo('Cliente: ',mensaje)
        
       # ,'Tamaño de etiqueta: ',Ancho,'x',Largo,'Cantidad de tintas',Tintas,'Precio de etiquetas',costo_impresion)
 


    


    


ventanaPrincipal=Tk()
ventanaPrincipal.geometry("900x500")
ventanaPrincipal.title("Software cotizacion etiquetas")


variableNombre = StringVar()
labelNombre = Label(ventanaPrincipal, text="Nombre del cliente:").grid(row=0,column=0)
campoNombre = Entry(ventanaPrincipal,textvariable=variableNombre).grid(row=0,column=1)

variableTintas = StringVar()
labelTintas = Label(ventanaPrincipal, text="Cantidad de tintas:").grid(row=1,column=0)
campoTintas = Entry(ventanaPrincipal, textvariable=variableTintas).grid(row=1,column=1)

variableAncho = StringVar()
labelAncho = Label(ventanaPrincipal, text="Ancho de etiqueta en mm: ").grid(row=2,column=0)
campoAncho = Entry(ventanaPrincipal, textvariable=variableAncho).grid(row=2,column=1)

variableLargo = StringVar()
labelLargo = Label(ventanaPrincipal, text="Largo de etiqueta en mm: ").grid(row=3,column=0)
campoLargo = Entry(ventanaPrincipal, textvariable=variableLargo).grid(row=3,column=1)

labelTipoImpresion = Label(ventanaPrincipal, text="Tipo de impresion:").grid(row=4,column=0)
variableTipoImpresion = IntVar()
Radiobutton(ventanaPrincipal, text="Digital", variable=variableTipoImpresion, value=1).grid(row=4,column=1)
Radiobutton(ventanaPrincipal, text="Flexografica", variable=variableTipoImpresion, value=2).grid(row=4,column=2)


labelTipoPapel = Label(ventanaPrincipal, text="Tipo de papel:").grid(row=5,column=0)
variableTipoPapel = IntVar()
Radiobutton(ventanaPrincipal, text="Bond", variable=variableTipoPapel, value=1).grid(row=5,column=1)
Radiobutton(ventanaPrincipal, text="Opalina", variable=variableTipoPapel, value=2).grid(row=5,column=2)
Radiobutton(ventanaPrincipal, text="Propalcote", variable=variableTipoPapel, value=3).grid(row=5,column=3)

labelMaquina = Label(ventanaPrincipal, text="Maquina de impresion:").grid(row=6,column=0)
variableMaquina = IntVar()
Radiobutton(ventanaPrincipal, text="Multili", variable=variableMaquina, value=1).grid(row=6,column=1)
Radiobutton(ventanaPrincipal, text="Adast", variable=variableMaquina, value=2).grid(row=6,column=2)

variableDesperdicio=StringVar()
labelDesperdicio = Label(ventanaPrincipal, text="Porcentaje de desperdicio de papel :").grid(row=7,column=0)
campoDesperdicio= Entry(ventanaPrincipal,textvariable=variableDesperdicio).grid(row=7,column=1)

variableUtilidad=StringVar()
labelUtilidad = Label(ventanaPrincipal, text="Porcentaje de utilidad:").grid(row=8,column=0)
campoUtilidad = Entry(ventanaPrincipal, textvariable=variableUtilidad).grid(row=8,column=1)

botonAgregar = Label(ventanaPrincipal, text="Agregar cotizacion").grid(row=9,column=0)
Button(ventanaPrincipal, text="+", command=duplicarcampo).grid(row=9,column=1)

Button(ventanaPrincipal, text="Calcular", command=Calcular).grid(row=(9),column=2)


 

ventanaPrincipal.mainloop()
