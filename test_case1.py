from selenium import webdriver

#Caso de pruebas "Validar carro de compras"
def run():
    driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
    driver.get('https://www.amazon.com')
    search_field = driver.find_element_by_id('nav-cart')
    search_field.click()


if __name__ == '__main__':
    run()