from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)

    # wait when price down for $100
    WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
        )
    
    # find and click booking button
    booking_btn = browser.find_element_by_id('book')
    booking_btn.click()

    # read variable and calculate answer
    x = browser.find_element_by_id('input_value').text
    answer = calc(x)

    # send answer 
    answer_input = browser.find_element_by_id('answer')
    answer_input.send_keys(answer)

    # submit solve 
    solve_btn = browser.find_element_by_id('solve')
    solve_btn.click()

finally:
    time.sleep(15)
    browser.quit()
