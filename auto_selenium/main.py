#type: ignore  Colocando aqui em cima ignoramos todo o arquivo

import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Dessa forma pegamos o arquivo "pai" do main que é oque estamos agora = aula316
ROOT_FOLDER = Path(__file__).parent 
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' /'chromedriver.exe'
# Aqui acima estamos linkando com o caminho da line 7, falamos para ele oque quermos dentro do folder aula 316

def make_chrome_browser(*options: str) -> webdriver.Chrome:  
    chrome_options = webdriver.ChromeOptions()

    #chrome_options.add.argument('--headless')
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
    # O headles é basicamente deixar invisivel
    options = ()
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com.br/')
    
    # Espere para encontra o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.NAME, 'q'))) # Aguardar pelo fato de que é feito por JS e demora um pouco

    search_input.send_keys('Hello World!') # Esse send keys literalmente pedimos para ele usar teclas para digitar o text que passamos
    search_input.send_keys(Keys.ENTER) # aqui estamos mandando que após digitar o texto acima pressionar enter

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()
time.sleep(TIME_TO_WAIT)