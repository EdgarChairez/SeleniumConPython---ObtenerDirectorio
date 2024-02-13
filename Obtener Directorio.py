from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.firefox.options import Options  # Ocultar navegador
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE
from selenium.common.exceptions import InvalidSwitchToTargetException as ISE
from selenium.common.exceptions import TimeoutException as TOE
from datetime import date
from datetime import datetime
import time

print('Inicia el proceso')
# Crea LOG #
now = str(datetime.now())
log=open("log_"+str((date.today())) + ".txt","a") 
datos_log=open("datos_log_"+str((date.today())) + ".txt","a") 
# Crea LOG #


#driver = webdriver.Firefox()                               # Mostrar proceso
# Ocultar navegador
log.write('-- Inicia servicio - ' + now + ' --\n')
datos_log.write('-- Inicia servicio - ' + now + ' --')
firefox_options = Options()                                 # Ocultar proceso
firefox_options.add_argument('--headless')                  # Ocular proceso
driver = webdriver.Firefox(options=firefox_options)         # Ocularr proceso
print('. ')
# Ocultar navegador


#driver.get('https://www.coppel.com/')
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


# Iniciar secion #
log.write('\n-- Inicia secion - ' + now + ' --\n')
print('. ')
username = 'Admin'
password = 'admin123'
try:
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    username.send_keys('Admin' + Keys.TAB + 'admin123' + Keys.TAB + Keys.ENTER)
except Exception as e:
    log.write('Error al "Iniciar Secion": ', e)
    print('. ')
# Iniciar secion #


# Seleccionar Directory #
try:
    log.write('\n-- Selecciona Directory  - ' + now + ' --\n')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Directory')]"))).click()
    print('. ')
    datos_log.write('\n.')
except Exception as e:
    log.write('Error al precionar "Directory": ', e)
# Seleccionar Directory


# Aplicar filtro #
def filtro(locacion):
    print(".\nSe realiza busqueda de: " + locacion)
    datos_log.write(".\nSe realiza busqueda de: " + locacion + " - "+ now + "\n")
    log.write('\n-- Selecciona Filtro  - ' + now + ' --\n')
    try:
        # Seleccionar selector
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]"))).click()
        # Seleccionar Locación
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'" + locacion + "')]"))).click() 
        # Boton Buscar
        time.sleep(2)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[2]"))).click()
        # Boton Buscar
    except TOE as t:
        print("No se encontro informacion para la busqueda: " + locacion)
        datos_log.write("No se encontro informacion para la busqueda: " + locacion)
# Aplicar filtro #


# Seleccionar card #
def seleccionar(select):
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'oxd-sheet oxd-sheet--rounded oxd-sheet--white orangehrm-directory-card')])[" + str(select) + "]"))).click() 
# Seleccionar card #

def cantidad():
    time.sleep(2)
    cantidad = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]")))        # Obtener Datos
    res = list(cantidad.find_elements(By.XPATH, "(//div[@class='oxd-grid-item oxd-grid-item--gutters'])"))
    cantidad = (len(res)-3)
    return cantidad
    print('. ')

# Obtener Datos #
def datos():
    try:        
        try: # Obtener Nombre
            nombre = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/p[1]"))).text        # Obtener Datos
        except TOE as e:
            nombre = str("NA")

        try: # Obtener Puesto
            puesto = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/p[2]"))).text        # Obtener Datos
        except TOE as e:
            puesto = str("NA")

        try: # Obtener Posicion
            posicion = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/p[1]"))).text        # Obtener Datos
        except TOE as e:
            posicion = str("NA")

        try: # Obtener Ubicacion
            ubicacion = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/p[2]"))).text        # Obtener Datos
        except TOE as e:
            ubicacion = str("NA")

        try: # Obtener Numero
            numero = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/p[2]"))).text        # Obtener Datos
        except TOE as a:
            numero = str("000-000-0000")
        
        try: # Obtener Email
            email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[6]/div[1]/p[2]"))).text        # Obtener Datos
        except TOE as e:
            email = str("NA")

        personas = { # Crear Diccionario
            "Nombre": nombre,
            "Puesto": puesto,
            "Posicion": posicion,
            "Ubicacion": ubicacion,
            "Numero": numero,
            "Email": email
        }
        return personas
        log.write('\n-- Se obienen datos  - ' + now + ' --\n')
    except WDE as e:
        print("Error al obtener datos: ", e)
        log.write("Error al obtener datos: ", e)
    print('. ')
# Obtener Datos #

# Ejecutar servicio con filtro #
def ejecutar(bus):              
    filtro(bus)                 # Aplicar filtro #
    cantidad()                  # Obtener cantidad de contactos
    if cantidad() > 0:
        print("Se encontraron " + str(cantidad()) + " registros")
        datos_log.write("Se encontraron " + str(cantidad()) + " registros\n")
        for x in range(cantidad()):
            i=x+1
            seleccionar(i)
            #time.sleep(2)
            print(datos())
            datos_log.write(str(datos()) + "\n")
            #time.sleep(2)
            seleccionar(i)
    else:
        print("No se encontraron datos")
        datos_log.write("No se encontraron datos\n.")
        print(".")
# Ejecutar servicio con filtro #


#ejecutar('New York Sales Office')
#ejecutar('HQ - CA, USA')
#ejecutar('New York Sales Office')
ejecutar('Texas R&D')

# Cerrar
driver.quit()
log.write('\n-- Finaliza Servicio  - ' + now + ' --\n\n')
datos_log.write('..\n-- Finaliza Servicio  - ' + now + ' -- \n.\n')
print('.\nFinaliza el proceso')
log.close()
