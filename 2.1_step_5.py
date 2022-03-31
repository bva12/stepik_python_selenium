#Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера, но сложным для человека.Ваша программа должна выполнить следующие шаги:

#1. Открыть страницу http://suninjuly.github.io/math.html.
#2. Считать значение для переменной x.
#3. Посчитать математическую функцию от x (код для этого приведён ниже).
#4. Ввести ответ в текстовое поле.
#5. Отметить checkbox "I'm the robot".
#6. Выбрать radiobutton "Robots rule!".
#7. Нажать на кнопку Submit.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
   
    # Определяем значение х и решаем уравнение
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
   
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    # Выбираем чек-бокс и радиобатон
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
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
