from behave import *
import pyautogui as pag
import subprocess as sp
import pytest
import time
import os

@given('la palabra es {palabraTest}')
def step_impl(context,palabraTest):
    
    textInput = pag.locateOnScreen("textInput.png")
    pag.click(pag.center(textInput))
    pag.write(palabraTest)

    startButton = pag.locateOnScreen("empezar_juego.png")

    pag.click(pag.center(startButton))

@when('jugador ingresa {palabraTest}')
def step_impl(context,palabraTest):
    # Localizar el campo de entrada para la palabra
    palabraInput = pag.locateOnScreen("palabra_input.png")

    pag.click(pag.center(palabraInput))
    pag.write(palabraTest)

    # Localizar el botón para adivinar la palabra
    adivinarPalabraButton = pag.locateOnScreen("adivinar_palabra.png")

    pag.click(pag.center(adivinarPalabraButton))

    print(f"El jugador ingresó la palabra: {palabraTest}")
    
@when('jugador intenta las letras {listaLetras}')
def step_impl(context,listaLetras):
    lista = listaLetras.split(',')

    letraInput = pag.locateOnScreen("letra_input.png")
    letraButton = pag.locateOnScreen("adivinar_letra.png")
    for l in lista:
        pag.click(pag.center(letraInput))
        pag.write(l)
        pag.click(pag.center(letraButton))

@then('se muestra pantalla {mensaje}')
def step_impl(context,mensaje):
    Msg = pag.locateOnScreen(f'{mensaje}.png')

    assert Msg is not pag.ImageNotFoundException

@given('se muestra pantalla {mensaje}')
def step_impl(context,mensaje):
    Msg = pag.locateOnScreen(f'{mensaje}.png')

    assert Msg is not pag.ImageNotFoundException

@when('jugador clickea en {boton}')
def step_impl(context,boton):
    Button = pag.locateOnScreen(f'{boton}.png')
    pag.click(pag.center(Button))