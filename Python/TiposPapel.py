
def precioPapel(TipoPapel):

    if TipoPapel== 1:
        papel="Bond"
        precio=500
         
        
    elif TipoPapel== 2:
        papel="Opalina"
        precio=1000
        
    elif TipoPapel== 3:
        papel="Propalcote"
        precio=2000

    #pasando el precio de metro cuadrado a pulg cuadrada

    precioPapelPulg=precio/1550

    return precioPapelPulg
