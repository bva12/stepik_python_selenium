# Commands 

```
add selection
```
Add a selection to the set of options in a multi-select element.

**arguments**

* locator: An element locator.

* value: The value to input.
____________

Добавьте выделение к набору параметров в элементе с множественным выбором.

**аргументы**

* локатор: Локатор элементов.

* значение: значение для ввода.
___
```
answer on next prompt
```
Affects the next alert prompt. This command will send the specified answer string to it. If the alert is already present, then use "webdriver answer on visible prompt" instead.

**arguments**

* answer: The answer to give in response to the prompt pop-up.
___
Влияет на следующее приглашение предупреждения. Эта команда отправит ему указанную строку ответа. Если предупреждение уже присутствует, то вместо этого используйте "webdriver answer on visible prompt".

**аргументы**

* ответ: ответ, который нужно дать в ответ на всплывающее приглашение.
___
```
assert
```
Check that a variable is an expected value. The variable's value will be converted to a string for comparison. The test will stop if the assert fails.

**arguments**

* variable name: The name of a variable without brackets.

* expected value: The result you expect a variable to contain (e.g., true, false, or some other value).
___
Убедитесь, что переменная является ожидаемым значением. Значение переменной будет преобразовано в строку для сравнения. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* имя переменной: имя переменной без скобок.

* ожидаемое значение: результат, который, как вы ожидаете, будет содержать переменная (например, true, false или какое-либо другое значение).
___
```
assert alert
```
Confirm that an alert has been rendered with the provided text. The test will stop if the assert fails.

**arguments**

* alert text: text to check
___
Подтвердите, что предупреждение было отображено с предоставленным текстом. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* текст предупреждения: текст для проверки
___
```
assert checked
```
Confirm that the target element has been checked. The test will stop if the assert fails.

**arguments**

* locator: An element locator.
___
Убедитесь, что целевой элемент был проверен. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* локатор: Локатор элементов.
___
```
assert confirmation
```
Confirm that a confirmation has been rendered. The test will stop if the assert fails.

**arguments**

* text: The text to use.
___
Подтвердите, что подтверждение было получено. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* текст: текст для использования.
___
```
assert editable
```
Confirm that the target element is editable. The test will stop if the assert fails.

**arguments**

* locator: An element locator.
___
Убедитесь, что целевой элемент доступен для редактирования. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* локатор: Локатор элементов.
___
```
assert element present
```
Confirm that the target element is present somewhere on the page. The test will stop if the assert fails.

**arguments**

* locator: An element locator.
___
Убедитесь, что целевой элемент присутствует где-то на странице. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* локатор: Локатор элементов.
___
```
assert element not present
```
Confirm that the target element is not present anywhere on the page. The test will stop if the assert fails.

**arguments**

* locator: An element locator.
___
Убедитесь, что целевой элемент нигде на странице не присутствует. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* локатор: Локатор элементов.
___
```
assert not checked
```
Confirm that the target element has not been checked. The test will stop if the assert fails.

**arguments**

* locator: An element locator.
___
Убедитесь, что целевой элемент не был проверен. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* локатор: Локатор элементов.
___
```
assert not editable
```
Confirm that the target element is not editable. The test will stop if the assert fails.

**arguments**

* locator: An element locator.
___
Убедитесь, что целевой элемент недоступен для редактирования. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* локатор: Локатор элементов.
___
```
assert not selected value
```
Confirm that the value attribute of the selected option in a dropdown element does not contain the provided value. The test will stop if the assert fails.

**arguments**

* select locator: An element locator identifying a drop-down menu.

* text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.
___
Убедитесь, что атрибут value выбранного параметра в выпадающем элементе не содержит указанного значения. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* выберите локатор: Локатор элемента, определяющий выпадающее меню.

* текст: точное совпадение строк. Поддержка сопоставления с образцом находится в стадии разработки. Смотри https://github.com/SeleniumHQ/selenium-ide/issues/141 для получения более подробной информации.
___
```
assert not text
```
Confirm that the text of an element does not contain the provided value. The test will stop if the assert fails.

**arguments**

* locator: An element locator.

* text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.
___
Убедитесь, что текст элемента не содержит указанного значения. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* локатор: Локатор элементов.

* текст: точное совпадение строк. Поддержка сопоставления с образцом находится в стадии разработки. Смотри https://github.com/SeleniumHQ/selenium-ide/issues/141 для получения более подробной информации.
___
```
assert prompt
```
Confirm that a JavaScript prompt has been rendered. The test will stop if the assert fails.

**arguments**

* text: The text to use.
___
Подтвердите, что приглашение JavaScript было отображено. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* текст: текст для использования.
___
```
assert selected value
```
Confirm that the value attribute of the selected option in a dropdown element contains the provided value. The test will stop if the assert fails.

**arguments**

* select locator: An element locator identifying a drop-down menu.

* text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.
___
Убедитесь, что атрибут value выбранного параметра в раскрывающемся списке содержит указанное значение. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* выберите локатор: Локатор элемента, определяющий выпадающее меню.

* текст: точное совпадение строк. Поддержка сопоставления с образцом находится в стадии разработки. Видишь https://github.com/SeleniumHQ/selenium-ide/issues/141 для получения более подробной информации.
___
```
assert selected label
```
Confirm that the label of the selected option in a dropdown element contains the provided value. The test will stop if the assert fails.

**arguments**

* select locator: An element locator identifying a drop-down menu.

* text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.
___
Убедитесь, что метка выбранного параметра в раскрывающемся списке содержит указанное значение. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* выберите локатор: Локатор элемента, определяющий выпадающее меню.

* текст: точное совпадение строк. Поддержка сопоставления с образцом находится в стадии разработки. Видишь https://github.com/SeleniumHQ/selenium-ide/issues/141 для получения более подробной информации.
___
```
assert text
```
Confirm that the text of an element contains the provided value. The test will stop if the assert fails.

**arguments**

* locator: An element locator.

* text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.
___
Убедитесь, что текст элемента содержит указанное значение. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* локатор: Локатор элементов.

* текст: точное совпадение строк. Поддержка сопоставления с образцом находится в стадии разработки. Видишь https://github.com/SeleniumHQ/selenium-ide/issues/141 для получения более подробной информации.
___
```
assert title
```
Confirm the title of the current page contains the provided text. The test will stop if the assert fails.

**arguments**

* text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.
___
Подтвердите, что заголовок текущей страницы содержит предоставленный текст. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* текст: точное совпадение строк. Поддержка сопоставления с образцом находится в стадии разработки. Видишь https://github.com/SeleniumHQ/selenium-ide/issues/141 для получения более подробной информации.
___
```
assert value
```
Confirm the (whitespace-trimmed) value of an input field (or anything else with a value parameter). For checkbox/radio elements, the value will be "on" or "off" depending on whether the element is checked or not. The test will stop if the assert fails.

**arguments**

* locator: An element locator.

* text: An exact string match. Support for pattern matching is in the works. See https://github.com/SeleniumHQ/selenium-ide/issues/141 for details.
___
Подтвердите (с пробелами) значение поля ввода (или что-либо еще с параметром value). Для элементов checkbox/radio значение будет "включено" или "выключено" в зависимости от того, установлен флажок или нет. Тест будет остановлен, если утверждение завершится неудачей.

**аргументы**

* локатор: Локатор элементов.

* текст: точное совпадение строк. Поддержка сопоставления с образцом находится в стадии разработки. Видишь https://github.com/SeleniumHQ/selenium-ide/issues/141 для получения более подробной информации.
___
```
check
```
Check a toggle-button (checkbox/radio).

**arguments**

* locator: An element locator.
___
Установите переключатель (флажок/переключатель).

**аргументы**

* локатор: Локатор элементов.
___
```
choose cancel on next confirmation
```
Affects the next confirmation alert. This command will cancel it. If the alert is already present, then use "webdriver choose cancel on visible confirmation" instead.
___
Влияет на следующее оповещение о подтверждении. Эта команда отменит его. Если предупреждение уже присутствует, то вместо этого используйте "webdriver выбирает отмену при видимом подтверждении".
___
```
choose cancel on next prompt
```
Affects the next alert prompt. This command will cancel it. If the alert is already present, then use "webdriver choose cancel on visible prompt" instead.
___
Влияет на следующее приглашение предупреждения. Эта команда отменит его. Если предупреждение уже присутствует, то вместо этого используйте "webdriver choose cancel on visible prompt".
___
```
choose ok on next confirmation
```
Affects the next confirmation alert. This command will accept it. If the alert is already present, then use "webdriver choose ok on visible confirmation" instead.
___
Влияет на следующее оповещение о подтверждении. Эта команда примет его. Если предупреждение уже присутствует, то вместо этого используйте "webdriver выберите ok при видимом подтверждении".
___
```
click
```
Clicks on a target element (e.g., a link, button, checkbox, or radio button).

**arguments**

* locator: An element locator.
___
Щелкает по целевому элементу (например, ссылке, кнопке, флажку или переключателю).

**аргументы**

* локатор: Локатор элементов.
___
```
click at
```
Clicks on a target element (e.g., a link, button, checkbox, or radio button). The coordinates are relative to the target element (e.g., 0,0 is the top left corner of the element) and are mostly used to check effects that relay on them, for example the material ripple effect.

**arguments**

* locator: An element locator.

* coord string: Specifies the x,y position (e.g., - 10,20) of the mouse event relative to the element found from a locator.
___
Щелкает по целевому элементу (например, ссылке, кнопке, флажку или переключателю). Координаты указаны относительно целевого элемента (например, 0,0 - верхний левый угол элемента) и в основном используются для проверки эффектов, которые на них воздействуют, например эффекта пульсации материала.

**аргументы**

* локатор: Локатор элементов.

* * coordstring: Задает положение x,y (например, - 10,20) события мыши относительно элемента, найденного с помощью локатора.
___
```
close
```
Closes the current window. There is no need to close the initial window, IDE will re-use it; closing it may cause a performance penalty on the test.
___
Закрывает текущее окно. Нет необходимости закрывать начальное окно, IDEA будет использовать его повторно; его закрытие может привести к снижению производительности теста.
___
```
debugger
```
Breaks the execution and enters debugger
___
Прерывает выполнение и входит в отладчик
___
```
do
```
Create a loop that executes the proceeding commands at least once. Terminate the branch with the repeat if command.
___
Создайте цикл, который выполняет следующие команды по крайней мере один раз. Завершите ветвь с помощью команды repeat if.
___
```
double click
```
Double clicks on an element (e.g., a link, button, checkbox, or radio button).

**arguments**

* locator: An element locator.
___
Двойной щелчок по элементу (например, ссылке, кнопке, флажку или переключателю).

**аргументы**

* локатор: Локатор элементов.
___
```
double click at
```
Double clicks on a target element (e.g., a link, button, checkbox, or radio button). The coordinates are relative to the target element (e.g., 0,0 is the top left corner of the element) and are mostly used to check effects that relay on them, for example the material ripple effect.

**arguments**

* locator: An element locator.

* coord string: Specifies the x,y position (e.g., - 10,20) of the mouse event relative to the element found from a locator.
___
Двойной щелчок по целевому элементу (например, ссылке, кнопке, флажку или переключателю). Координаты указаны относительно целевого элемента (например, 0,0 - верхний левый угол элемента) и в основном используются для проверки эффектов, которые на них воздействуют, например эффекта пульсации материала.

**аргументы**

* локатор: Локатор элементов.

* * coordstring: Задает положение x,y (например, - 10,20) события мыши относительно элемента, найденного с помощью локатора.
___
```
drag and drop to object
```
Drags an element and drops it on another element.

**arguments**

* locator of object to be dragged: The locator of element to be dragged.

* locator of drag destination object: The locator of an element whose location (e.g., the center-most pixel within it) will be the point where locator of object to be dragged is dropped.
___
Перетаскивает элемент и помещает его на другой элемент.

**аргументы**

* locatorofobjecttobedragged: местоположение перетаскиваемого элемента.

* локатор объекта назначения перетаскивания: локатор элемента, местоположение которого (например, самый центральный пиксель внутри него) будет точкой, в которой будет удален локатор перетаскиваемого объекта.
___
```
echo
```
Prints the specified message into the third table cell in your Selenese tables. Useful for debugging.

**arguments**

* message: The message to print.
___
Выводит указанное сообщение в третью ячейку таблицы в ваших таблицах Selenese. Полезно для отладки.

**аргументы**

* сообщение: Сообщение для печати
___
```
edit content
```
Sets the value of a content editable element as if you typed in it.

**arguments**

* locator: An element locator.

* value: The value to input.
___
Задает значение редактируемого элемента содержимого, как если бы вы ввели его.

**аргументы**

* локатор: Локатор элементов.

* значение: значение для ввода.
___
```
else
```
Part of an if block. Execute the commands in this branch when an if and/or else if condition are not met. Terminate the branch with the end command.
___
Часть блока if. Выполняйте команды в этой ветке, когда условие if и/или else if не выполняется. Завершите ветвь с помощью команды end.
___
```
else if
```
Part of an if block. Execute the commands in this branch when an if condition has not been met. Terminate the branch with the end command.

**arguments**

* conditional expression: JavaScript expression that returns a boolean result for use in control flow commands.
___
Часть блока if. Выполняйте команды в этой ветке, если условие if не было выполнено. Завершите ветвь с помощью команды end.

**аргументы**

* условное выражение: выражение JavaScript, которое возвращает логический результат для использования в командах потока управления.
___
```
end
```
Terminates a control flow block for if, while, and times.
___
Завершает блок потока управления для if, while и times.
___
```
execute script
```
Executes a snippet of JavaScript in the context of the currently selected frame or window. The script fragment will be executed as the body of an anonymous function. To store the return value, use the 'return' keyword and provide a variable name in the value input field.

**arguments**

* script: The JavaScript snippet to run.

* variable name: The name of a variable without brackets.
___
Выполняет фрагмент JavaScript в контексте выбранного в данный момент фрейма или окна. Фрагмент скрипта будет выполняться как тело анонимной функции. Чтобы сохранить возвращаемое значение, используйте ключевое слово 'return' и укажите имя переменной в поле ввода значения.

**аргументы**

* скрипт: фрагмент кода JavaScript для запуска.

* имя переменной: имя переменной без скобок.
___
```
execute async script
```
Executes an async snippet of JavaScript in the context of the currently selected frame or window. The script fragment will be executed as the body of an anonymous function and must return a Promise. The Promise result will be saved on the variable if you use the 'return' keyword.

**arguments**

* script: The JavaScript snippet to run.

* variable name: The name of a variable without brackets.
___
Выполняет асинхронный фрагмент JavaScript в контексте текущего выбранного фрейма или окна. Фрагмент скрипта будет выполняться как тело анонимной функции и должен возвращать обещание. Результат обещания будет сохранен в переменной, если вы используете ключевое слово 'return'.

**аргументы**

* скрипт: фрагмент кода JavaScript для запуска.

* имя переменной: имя переменной без скобок.
___






