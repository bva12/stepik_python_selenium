#Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

#Напишите код, который реализует следующий сценарий:

#1. Открыть страницу http://suninjuly.github.io/selects1.html
#2. Посчитать сумму заданных чисел
#3. Выбрать в выпадающем списке значение равное расчитанной сумме
#4. Нажать кнопку "Submit"


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
   
    # Находим сумму чисел
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    z = str(int(x) + int(y))
    
    # Выбираем в выпадающем списке значение, равное рассчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)

    # Нажимаем на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
