from behave import *
import pyautogui as pag
import subprocess as sp
import pytest
import time
import os
import pygetwindow as gw

def iniciar_aplicacion():
    print("Iniciando la aplicación...")
    script_path = os.path.abspath("Ahorcado/AhorcadoApp.py")
    
    process = sp.Popen(['python', script_path], stdout=sp.PIPE, stderr=sp.PIPE)
    time.sleep(1)  # Tiempo de espera para cargar la aplicación
    
    # Verifica si la ventana está abierta
    """ ventana_juego = None
    for ventana in gw.getAllTitles():
        if "Ahorcado" in ventana:
            ventana_juego = ventana
            break """
    
    # if ventana_juego is None:
    #     process.terminate()
    #     print("Error: La ventana del juego no se inició correctamente.")
    #     return None

    print("Aplicación iniciada correctamente.")
    return process


def cerrar_aplicacion(process):
    """Cierra la aplicación después de la prueba."""
    if process:
        process.terminate()
        process.wait()
        print("Aplicación cerrada.")

@given('la palabra es {palabraTest}')
def step_impl(context,palabraTest):
    context.process = iniciar_aplicacion()
    
    textInput = pag.locateOnScreen("Ahorcado/textInput.png")
    pag.click(pag.center(textInput))
    pag.write(palabraTest)

    startButton = pag.locateOnScreen("Ahorcado/empezar_juego.png")

    pag.click(pag.center(startButton))

@when('jugador ingresa {palabraTest}')
def step_impl(context,palabraTest):
    # Localizar el campo de entrada para la palabra
    palabraInput = pag.locateOnScreen("Ahorcado/palabra_input.png")

    pag.click(pag.center(palabraInput))
    pag.write(palabraTest)

    # Localizar el botón para adivinar la palabra
    adivinarPalabraButton = pag.locateOnScreen("Ahorcado/adivinar_palabra.png")

    pag.click(pag.center(adivinarPalabraButton))

    print(f"El jugador ingresó la palabra: {palabraTest}")
    
@when('jugador intenta las letras {listaLetras}')
def step_impl(context,listaLetras):
    lista = listaLetras.split(',')

    letraInput = pag.locateOnScreen("Ahorcado/letra_input.png")
    letraButton = pag.locateOnScreen("Ahorcado/adivinar_letra.png")
    for l in lista:
        pag.click(pag.center(letraInput))
        pag.write(l)
        pag.click(pag.center(letraButton))

@then('se muestra pantalla {mensaje}')
def step_impl(context,mensaje):
    Msg = pag.locateOnScreen(f'Ahorcado/{mensaje}.png')

    assert Msg is not pag.ImageNotFoundException
    cerrar_aplicacion(context.process)

@given('se muestra pantalla {mensaje}')
def step_impl(context,mensaje):
    #context.process = iniciar_aplicacion()>
    Msg = pag.locateOnScreen(f'Ahorcado/{mensaje}.png')

    assert Msg is not pag.ImageNotFoundException

@when('jugador clickea en {boton}')
def step_impl(context,boton):
    Button = pag.locateOnScreen(f'Ahorcado/{boton}.png')
    pag.click(pag.center(Button))