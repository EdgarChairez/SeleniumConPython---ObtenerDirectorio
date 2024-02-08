from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.firefox.options import Options  # Ocultar navegador
from selenium.webdriver.common.keys import Keys
from datetime import date
from datetime import datetime
import time

print('Inicia el proceso')
# Crea LOG #
log=open("log_"+str((date.today())) + ".txt","w") 
now = str(datetime.now())
datos_log=open("datos_log_"+str((date.today())) + ".txt","w") 
# Crea LOG #

#driver = webdriver.Firefox()                               # Mostrar proceso
# Ocultar navegador
log.write('-- Inicia servicio - ' + now + ' --\n')
firefox_options = Options()                                 # Ocultar proceso
firefox_options.add_argument('--headless')                  # Ocular proceso
driver = webdriver.Firefox(options=firefox_options)         # Ocularr proceso
print('. ')
# Ocultar navegador

#driver.get('https://www.coppel.com/')
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


# Iniciar secion #
log.write('\n-- Inicia secion - ' + now + ' --')
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
    log.write('\n-- Selecciona Directory  - ' + now + ' --')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Directory')]"))).click()
    print('. ')
except Exception as e:
    log.write('Error al precionar "Directory": ', e)
# Seleccionar Directory

def filtro(locacion):
    # Aplicar filtro #
    log.write('\n\n-- Selecciona Filtro  - ' + now + ' --')
    # Seleccionar selector
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]"))).click()
    # Seleccionar Locación
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'" + locacion + "')]"))).click() 
    # Boton Buscar
    time.sleep(2)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[2]"))).click()
    # Obtener datos
    time.sleep(1)
    datos = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]")))        # Obtener Datos
    # Aplicar Filtro #

    # Imprimir lista #
    log.write('\n-- Crea Lista: ' + locacion + ' - ' + now + ' --')
    datos_log.write('-- -- -- -- -- -- -- -- -- -- -- -- -- -- --')
    datos_log.write('\nHubicacion: ' + locacion + '\n\n')
    print('. ')
    #print('\nHubicacion: ' + locacion + '\n')

    # Dividir lista
    if datos.text!='':
        try:
            print('.')
            nombres = datos.text.split("\n")                                                                                                                              # Separar datos
            contactos = [nombres[i:i + 4] for i in range(0, len(nombres), 4)]

            x=0
            for i in contactos:
                
                for j in range(4):
                    if j==0:
                        #print("Nombre: " + contactos[x][j])
                        datos_log.write("Nombre: " + contactos[x][j] + '\n')
                    if j==1:
                        #print("Puesto: " + contactos[x][j])
                        datos_log.write("Puesto: " + contactos[x][j] + '\n')
                    if j==2:
                        #print("Posicion: " + contactos[x][j])
                        datos_log.write("Posicion: " + contactos[x][j] + '\n')
                    if j==3:
                        #print("Hubicacion: " + contactos[x][j])
                        datos_log.write("Hubicacion: " + contactos[x][j] + '\n')
                x += 1
                #print()
                datos_log.write('\n')
        except Exception as e:
            log.write('Error al dividir lista de nombres: ', e)
        log.write('\n-- Cantidad: '+ str(x))
    else:
        datos_log.write('No se encontraron registros')
        log.write('\n-- No se encontraron registros')
    # Imprimir lista #

filtro('Texas R&D')
time.sleep(2)
filtro('New York Sales Office')
time.sleep(2)
filtro('HQ - CA, USA')
time.sleep(2)
filtro('Canadian Regional HQ')

# Esperar
#time.sleep(5)
# Cerrar
driver.quit()
log.write('\n\n-- Finaliza Servicio  - ' + now + ' --')
print('Finaliza el proceso')
log.close()



