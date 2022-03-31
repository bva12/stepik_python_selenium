#В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

# Ваша программа должна:

#1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
#2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
#3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
#4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
#5. Ввести ответ в текстовое поле.
#6. Отметить checkbox "I'm the robot".
#7. Выбрать radiobutton "Robots rule!".
#8. Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
   
    # Определяем значение х и решаем уравнение
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
   
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    # Выбираем чек-бокс и радиобатон
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
