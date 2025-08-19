# PROYECTO-1

## **Descripción del proyecto**

Este programa tiene el proposito de Crear una calculadora financiera de ahorros funcional teniendo metas y proyecciones a largo plazo. 

El proyecto contiene dos clases principales las cuales son:


- Calculadora_ahorro:

Esta es una clase creada la cual contiene la logica matemática del programa permitiendo calcular valores con los datos dados por el usuario los cuales serian capital inicial entre otros y usando las tasas de interes y el número de meses que se desea utilizar para el calculo y aportes mensuales para llegar a las metas deseadas por el usuario.

- InterfazCalculadora:

Esta clase  maneja la interacción del usuario por medio de un menú en el cual ellos pueden elegir opciones como calcular cuanto dinero llegaran a tener en el futuro, cuanto deben ahorrar y de igual manera este menú redirecciona a otro en el cual el usuario puede ingresar sus datos para poder hacer el calculo.



## **Instrucciones de uso del programa**
1. Abrir el programa
2. Al iniciar el programa saldrá un menú de opciones en el cual el usuario debe de elegir cual quiere presionando el numero de opción que sea: 
  
    - 1.  Calcular cuanto  tendrás en el futuro
    - 2. Calcular cuanto debes ahorrar cada mes
    - 3. salir del programa


3. Ingresar datos según la opcion que eligió:

- Si se eligió la opcion 1 en este caso **Calcular FV** el programa le presentara unas preguntas las cuales debe de responder el usuario y las preguntas son las siguientes

    - Ingresar capital inicial
    - Ingresar aporte mensual
    - Ingresar la tasa de interes anual
    - Ingresar el numero de meses que desea ahorrar

luego de que el usuario responda estas preguntas se mostrará el FV o sea el valor futuro.

- Si se le eligió la opcion 2 **Calcular PMT**

    - Ingresar la meta de ahorro que usted desea.
    - Ingresar el capital inicial (po).
    - Ingresar la tasa de interes anual en números decimales.
    - Ingresar el numero de meses que desea ahorrar.

luego de haber respondido las preguntas que el programa presenta se mostrar cuanto debe de ahorrar el usuario cada mes (PMT)

- Si se eligio la opción 3 **Salir del programa**, el programa regresa al menú principal para que usted puede elegir otra opcion o bien salir del programa por completo

   
## **Integrantes del equipo y roles**

-Heidelle Esther Legrand Aceituno --------- Modelador matemático 

-Mario Javier Muñoz Bendfeldt ----------- Tester

-Rocio Iveth Cojulum Juárez------- Documentador tecnico

-El trabajo de interfaz de flujo será repartido entre los 3 integrantes

### **Problemas econtrados y soluciones**

En este trabajo se presentarios diversos retos los cuales con investigación logramos resolver

- Conocimientos bajos sobre interes compuesto 
    - La solución a este problema fue investigar sobre qué es, como se usa, deficiones

- Calculos: se desconocia como eran las formulas para poder hacer los calculos que debiamos implementar en el programa
    - La solución a este problema fue buscar diversas formulas comprarlas y analizar con las deficiones para ver cual era la correcta

- Errores en codigo, al intentar implementar las formulas en el codigo hubieron ciertos fallos ya que desconociamos sobre los calculos y no daba siempre la respuesta acertada
    - Como solución fue revisar paso por paso cada parte del codigo y analizar la estructura para evitar errores 




