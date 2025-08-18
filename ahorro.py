def calcular_fv (P0, PMT, tasa, meses):
    try: 
        if tasa <0 or meses <=0:
            raise ValueError ("La tasa no puede ser un valor negativo y los meses deben ser mayor a 0")
        if tasa == 0:
            return P0 + PMT * meses
        return P0 * (1 + tasa)**meses + PMT * (((1 + tasa)**meses - 1) / tasa)
    except ZeroDivisionError:
        return P0 + PMT * meses
