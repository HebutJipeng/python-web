from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--headless")  # 后台静默运行
driver = webdriver.Chrome('/Users/jipeng/htdoc/frontend/python_web/v2/chromedriver')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()