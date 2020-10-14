import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class Search_tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'../chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_wondow()
        driver.get('https://www.amazon.com')


    def tearDown(self):
        self.driver.quit()

    def test_search_sony(self):
        driver = self.driver
        search_field = driver.find_element_by_name('field-keywords')
        search_field.clear()
        search_field.send_keys('sony wh-1000xm4')
        search_field.submit()

    
    def test_search_SSD(self):
        driver = self.driver
        search_field = driver.find_element_by_name('field-keywords')
        search_field.clear()
        search_field.send_keys('sandisk ssd 1tb')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span')
        self.assertEqual(1, len(products))





if __name__ == "__main__":
	unittest.main(verbosity=2, testRunner=HTMLTestRunner(output = 'reportes', report_name = 'Amazon-report'))