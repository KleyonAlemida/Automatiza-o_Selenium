#type: ignore  Colocando aqui em cima ignoramos todo o arquivo

import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Pegando o arquivo raiz
ROOT_FOLDER = Path(__file__).parent 
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' /'chromedriver.exe'
# Acima pegamos a subpasta e o driver contido

def make_chrome_browser(*options: str) -> webdriver.Chrome:  
    chrome_options = webdriver.ChromeOptions()
    
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    chrome_service = Service(
        executable_path=str(CHROMEDRIVER_EXEC),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example

    options = ()
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com.br/')
    
    # Espere para encontra o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.NAME, 'q'))) 
    
    # Pedimos para digitar o text abaixo
    search_input.send_keys('Hello World!') 
    search_input.send_keys(Keys.ENTER) 
    # Acima configuramos para o comando dar enter após a digitação da linha 49
    
    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click() # Aqui pedimos para o comando dar um click no primeiro resultado
    
time.sleep(TIME_TO_WAIT)
