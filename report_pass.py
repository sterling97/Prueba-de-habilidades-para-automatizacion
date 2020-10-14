import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class Amazon_test(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(10)

	def test_hello_world(self):
		driver = self.driver
		driver.get('https://www.amazon.com')

	def test_visit_wikipedia(self):
		driver = self.driver
		driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity=2, testRunner=HTMLTestRunner(output = 'reportes', report_name = 'Amazon-report'))