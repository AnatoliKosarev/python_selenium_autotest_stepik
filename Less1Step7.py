import time
from asyncio import wait_for

from selenium import webdriver
from Part2.Less1Step1 import calc


webdriver = webdriver.Chrome()

try:
    webdriver.get('http://suninjuly.github.io/get_attribute.html')

    x = webdriver.find_element_by_id('treasure').get_attribute('valuex')
    if x and x.isdigit:
        result = calc(x)

        input_field = webdriver.find_element_by_id('answer')
        print(input_field.get_attribute('id'))
        input_field.send_keys(result)
        webdriver.find_element_by_id('robotCheckbox').click()
        webdriver.find_element_by_id('robotsRule').click()
        webdriver.find_element_by_css_selector('button[type=\'submit\']').click()

finally:
    time.sleep(5)
    webdriver.quit()
