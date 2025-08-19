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
            return self.P0 * (1 + self.tasa) ** self.meses + self.PMT * (((1 + self.tasa) ** self.meses - 1) / self.tasa)
        except ZeroDivisionError:
            return self.P0 + self.PMT * self.meses
        
    def calcular_pmt(self, meta):
        if self.tasa == 0:
            return (meta - self.P0) / self.meses
        return ((meta - self.P0 * (1 + self.tasa) ** self.meses) * self.tasa) / ((1 + self.tasa) ** self.meses - 1)

class InterfazCalculadora:
    @staticmethod
    def pedir_float(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Entrada inválida. Ingresa un número válido.")

    @staticmethod
    def  pedir_int(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print(" Entrada inválida. Ingresa un número entero válido.")

    @staticmethod
    def menu():
        while True:
            print("\n=== Calculadora de Ahorro (POO) ===")
            print("1. Calcular cuánto tendré en el futuro (FV)")
            print("2. Calcular cuánto debo ahorrar cada mes (PMT)")
            print("3. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                P0 = float(input("Capital inicial: "))
                PMT = float(input("Aporte mensual: "))
                tasa_anual = float(input("Tasa de interés anual (ej. 0.05 = 5%): "))
                meses = int(input("Número de meses: "))
                calc = calculadora_ahorro(P0, PMT, tasa_anual / 12, meses)
                fv = calc.calcular_fv()
                print(f"En {meses} meses tendrás: {fv:.2f}")

            elif opcion == "2":
                meta = float(input("Meta de ahorro: "))
                P0 = float(input("Capital inicial: "))
                tasa_anual = float(input("Tasa de interés anual (ej. 0.05 = 5%): "))
                meses = int(input("Número de meses: "))
                calc = calculadora_ahorro(P0, 0, tasa_anual / 12, meses)
                pmt = calc.calcular_pmt(meta)
                print(f"Debes ahorrar cada mes: {pmt:.2f}")

            elif opcion == "3":
                print("¡Hasta luego! :)")
                break
            else:
                print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    InterfazCalculadora.menu()
