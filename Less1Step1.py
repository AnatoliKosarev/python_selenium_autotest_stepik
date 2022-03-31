import math
import time

from selenium import webdriver


webdriver = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def run_test():
    try:
        webdriver.get('http://suninjuly.github.io/math.html')

        x = webdriver.find_element_by_id('input_value').text
        if x and x.isdigit:
            result = calc(x)

            input_field = webdriver.find_element_by_id('answer')
            input_field.send_keys(result)
            webdriver.find_element_by_css_selector('label[for=\'robotCheckbox\']').click()
            webdriver.find_element_by_id('robotsRule').click()
            webdriver.find_element_by_css_selector('button[type=\'submit\']').click()

    finally:
        time.sleep(5)
        webdriver.quit()
