
import TiposMaquinas

def costoImpresion (TipoImpresion,Ancho,Largo,CantidadEtiquetas,PrecioPapel,TiempoImpresion,Desperdicio,Tintas,Maquina):


    if TipoImpresion== 1:
        costoImpresion=costoImpresionDigital(Ancho,Largo,CantidadEtiquetas,PrecioPapel,TiempoImpresion)
        

    elif TipoImpresion== 2:
        costoImpresion=costoImpresionFlexografica(Ancho,Largo,CantidadEtiquetas,PrecioPapel,TiempoImpresion,Desperdicio,Tintas,Maquina)


    return costoImpresion


def costoImpresionDigital(Ancho,Largo,CantidadEtiquetas,PrecioPapel,TiempoImpresion):

    costoHoraTrabajador=4000
    costoMinTrabajador=4000/60
    AreaEtiqueta=(Ancho/25.4)*(Largo/25.4) #area pulg cuadrada
    
    costoDigital=(AreaEtiqueta*CantidadEtiquetas*PrecioPapel)+(TiempoImpresion*costoMinTrabajador)

    return costoDigital





def costoImpresionFlexografica(Ancho,Largo,CantidadEtiquetas,PrecioPapel,TiempoImpresion,Desperdicio,Tintas,Maquina):

    costoHoraTrabajador=4000
    costoMinTrabajador=4000/60

    AreaEtiqueta=(Ancho/25.4)*(Largo/25.4) #area pulg cuadrada
    tiempoPreparacionMaquina=TiposMaquinas.caracteristicasMaquina(Maquina)[0]

    costoFlexografica=((AreaEtiqueta+Desperdicio)*CantidadEtiquetas*PrecioPapel)+((tiempoPreparacionMaquina*Tintas)*costoMinTrabajador)+(TiempoImpresion*costoMinTrabajador)
    return costoFlexografica

