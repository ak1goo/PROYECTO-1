Error1 - Bug:
LINE 39: InterfazCalculadora takes no arguments.
LINE 59: InterfazCalculadora.menu()

Error2 - Bug:
LINE49: pmt= calc.calcular_pmt(meta)
LINE21: ZeroDivisionError: float division by zero

Error 3 = Bug:
Entrada invalida no numerica. 
Value Error.

ERRORES CONOCIDOS:
1. Tasa anual negativa
   - Qué pasa: Si el usuario ingresa un valor negativo en la tasa de interés, el cálculo de FV o PMT no tiene sentido financiero.
   - Solución: Se lanza un ValueError y se solicita al usuario ingresar una tasa ≥ 0.

2. Meses o tiempo <= 0
   - Qué pasa: No se puede calcular FV o PMT si el número de meses es cero o negativo.
   - Solución: Se valida la entrada y se muestra un mensaje de error si el valor es inválido.

3. División por cero en cálculo de PMT
   - Qué pasa: Si la tasa mensual es 0 y no se maneja, se produce una división por cero.
   - Solución: Se calcula PMT como (meta - P0)/meses cuando la tasa es 0.

4. Entrada no numérica
   - Qué pasa: Si el usuario ingresa letras en lugar de números para capital, tasa o meses.
   - Solución: Se usa try/except para capturar ValueError y solicitar una entrada válida.
