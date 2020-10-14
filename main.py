import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(15)
		driver.maximize_window()
		driver.get('https://www.amazon.com')

	def test_search_text_field(self):
		search_field = self.driver.find_element_by_id('search') 

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity = 2)