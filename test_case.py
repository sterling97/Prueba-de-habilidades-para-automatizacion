from selenium import webdriver

#Caso de prueba "Busqueda de producto"
def run():
    driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
    driver.get('https://www.amazon.com')
    search_field = driver.find_element_by_name('field-keywords')
    search_field.clear()
    search_field.send_keys('sony wh-1000xm4')
    search_field.submit()


if __name__ == '__main__':
    run()
