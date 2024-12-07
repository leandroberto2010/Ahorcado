from behave import fixture
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options



from Ahorcado import Ahorcado

def esperarElemento(dr,id, timeout=10):
    try:
        wait = WebDriverWait(dr, 5)  # Tiempo máximo de espera: 5 segundos
        elemento = wait.until(EC.element_to_be_clickable((By.ID, id)))
        return elemento
    except StaleElementReferenceException:
        return esperarElementoCambiante(dr, id, timeout)
    except TimeoutException:
        print(f"El botón {id} no se pudo hacer click después de esperar 10 segundos")

def esperarElementoCambiante(driver, id, timeout=10, retries=3):
    for _ in range(retries):
        try:
            wait = WebDriverWait(driver, timeout)
            elemento = wait.until(EC.presence_of_element_located((By.ID, id)))
            if elemento.is_displayed():
                return elemento
        except StaleElementReferenceException:
            continue
    raise Exception(f"No se pudo encontrar el elemento con ID: {id}")

def iniciar_aplicacion():
    print("Iniciando la aplicación...")

    options = Options()
    options.add_argument("--headless")  # Ejecutar Chrome en modo headless
    options.add_argument("--disable-gpu")  # Desactivar la aceleración por GPU
    options.add_argument("--no-sandbox")  # Evitar problemas de sandboxing

    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5000/")

    while driver.execute_script("return document.readyState") != "complete":
        pass

    print("Aplicación iniciada correctamente.")
    return driver

def cerrar_aplicacion(driver):
    #Cierra la aplicación después de la prueba.
    if driver:
        driver.quit()
        print("Aplicación cerrada.")

def palabraInicial(dr,palabraTest):
    input = esperarElemento(dr,"palabra")
    input.click()
    input.send_keys(palabraTest)
        
    startBoton = esperarElemento(dr,"iniciar")
    startBoton.click()

def adivinaPalabra(dr,palabraTest):
    # Localizar el campo de entrada para la palabra
    input = esperarElemento(dr,"palabra-completa")
    input.click()
    input.send_keys(palabraTest)

    boton = esperarElemento(dr,"adivina-palabra")
    boton.click()

@fixture
def before_scenario(context,scenario):
    context.driver = iniciar_aplicacion()

def after_scenario(context,scenario):
    cerrar_aplicacion(context.driver)

def before_step(context,step):
    dr = context.driver
    if ('Reiniciar juego luego de' in context.scenario.name):
        if (step.step_type == 'given' and 'se muestra mensaje' in step.name):
            palabraInicial(dr,'PALABRA')
            if ('perder' in context.scenario.name):
                adivinaPalabra(dr,'MANZANA')
            else:
                adivinaPalabra(dr,'PALABRA')