class calculadora_ahorro:
    def __init__(self, P0=0.0, PMT=0.0, tasa=0.0, meses=0):
        self.P0 = P0        
        self.PMT = PMT      
        self.tasa = tasa    
        self.meses = meses

    def calcular_fv(self):
        try: 
            if self.tasa < 0 or self.meses <= 0:
                raise ValueError("La tasa no puede ser negativa y los meses deben ser > 0")
            if self.tasa == 0:
                return self.P0 + self.PMT * self.meses
            return self.P0 * (1 + self.tasa) ** self.meses + self.PMT * ((1 + self.tasa) ** self.meses - 1) / self.tasa)
        except ZeroDivisionError:
            return self.P0 + self.PMT * self.meses
        
    def calcular_pmt(self, meta):
        if self.tasa == 0:
            return (meta - self.P0) / self.meses
        return ((meta - self.P0 * (1 + self.tasa) ** self.meses) * self.tasa) / ((1 + self.tasa) ** self.meses - 1)

