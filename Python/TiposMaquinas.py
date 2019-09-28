

def caracteristicasMaquina(Maquina):

    if Maquina== 1:
        TipoMaquina="Multili"
        tiempoPreparacion=0.5 #[horas]
        anchoRodillo=15 #[pulg]
        velocidadImpresion=5 #[pulg/min]
        
    elif Maquina== 2:
        TipoMaquina="Adast"
        tiempoPreparacion=0.1 #[horas]
        anchoRodillo=30 #[pulg]
        velocidadImpresion=20 #[pulg/min]

    tiempoPreparacion=tiempoPreparacion*60

    return tiempoPreparacion,anchoRodillo,velocidadImpresion

def tiempoImpresion(Ancho,Largo,CantidadEtiquetas,Maquina):

    tiempoAncho=tiempoImpresionAncho(Ancho,Largo,CantidadEtiquetas,Maquina)
    tiempoLargo=tiempoImpresionLargo(Ancho,Largo,CantidadEtiquetas,Maquina)

    if tiempoAncho<tiempoLargo:
        tiempoDeImpresion=tiempoAncho
    else:
        tiempoDeImpresion=tiempoLargo

    
    return tiempoDeImpresion


def tiempoImpresionAncho(Ancho,Largo,CantidadEtiquetas,Maquina):

    anchoPapel=caracteristicasMaquina(Maquina)[1]
    velocidad =caracteristicasMaquina(Maquina)[2]
    anchoEtiqueta = (float(Ancho))/25.4
    LargoEtiqueta = (float(Largo))/25.4

    cantidadEtiquetasAncho=(int (anchoPapel))/anchoEtiqueta
    cantidadEtiquetasAncho= int (cantidadEtiquetasAncho)
    cantidadEtiquetasLargo=CantidadEtiquetas/cantidadEtiquetasAncho
    cantidadEtiquetasLargo= round (cantidadEtiquetasLargo)
    LargoPapel=cantidadEtiquetasLargo*LargoEtiqueta
    TiempoAncho=LargoPapel/velocidad
    return TiempoAncho

def tiempoImpresionLargo(Ancho,Largo,CantidadEtiquetas,Maquina):

    anchoPapel=caracteristicasMaquina(Maquina)[1]
    velocidad =caracteristicasMaquina(Maquina)[2]
    anchoEtiqueta = (int(Ancho))/25.4
    largoEtiqueta = (int(Largo))/25.4

    cantidadEtiquetasAncho=(int (anchoPapel))/largoEtiqueta
    cantidadEtiquetasAncho= int (cantidadEtiquetasAncho)
    cantidadEtiquetasLargo=CantidadEtiquetas/cantidadEtiquetasAncho
    cantidadEtiquetasLargo= round (cantidadEtiquetasLargo)
    LargoPapel=cantidadEtiquetasLargo*anchoEtiqueta
    TiempoLargo=LargoPapel/velocidad
    
    return TiempoLargo


