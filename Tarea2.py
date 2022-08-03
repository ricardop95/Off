#este programa tiene por funcion determinar el tiempo de uso de la pc y luego saltar a una pagina de relajacion en youtube
import webbrowser
import time
import random
navegador = 'chrome'
print("hola estas iniciando a usarme a las "+ time.ctime())
TimeOff = 3 # preguntarle a ramon por que no usar def 
TimeTravel = 0 
while(TimeTravel<TimeOff):
    pregunta= input("¿deseas tomar un descanso?")
    if "si" == pregunta:
        time.sleep(10)
        webbrowser.open('https://www.youtube.com/watch?v=ec_xGmM_tJc', new=2, autoraise=True)
    if "no"== pregunta:
        print("tienes que descansar entrare en modo suspension 5 minutos")