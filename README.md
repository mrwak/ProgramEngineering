# ProgramEngineering
Labs and practices

В программу подается текст из файла, состоящего из строчек формата  
`Имя Фамилия|Возраст|ТелефонныйНомер|ЭлектроннаяПочта`  
Необходимо проверить данные на корректность, и по возможности, 
исправленную версию поместить в другой файл. 
Если данные ошибочные, то часть строки оставить пустой. К примеру, из строки  
_"ИванИванов|27|+7999000 1 1 11|example@@yandex..ru"_  
может после исправления получиться строка   
_"Иван Иванов|27|+7 (999) 0001111|example@yandex.ru"_

---  
##### Пример работы программы:
```  
|||||  
Invalid line format  
  
|||  
Invalid line format  
  
|1|1|lol@mail.ru  
Invalid line format  
  
ИванИванов|27|+7999000 1 1 11|example@@yandex..ru  
Иван Иванов|27|+7 (999) 000-1111|example@yandex.ru  
  
Иван Иванов|27|+7 (999) 0001111|example@yandex.ru  
Иван Иванов|27|+7 (999) 000-1111|example@yandex.ru  
  
johnDow|21|8-800-555-11-22|mega.ultra.man98@mail.domain.top.level  
John Dow|21|+7 (800) 555-1122|mega.ultra.man98@mail.domain.top.level  
  
adam smith| 45 | + 7 9 9 9 0 0 0 1111|mail_could_not_ends_withdot.@mail.domain  
Adam Smith|45|+7 (999) 000-1111|mail_could_not_ends_withdot.@mail.domain неверное поле  
  
name surname|25|telephone number| mylo@gmail.com  
Name Surname|25|telephonenumber неверное поле|mylo@gmail.com  
  
ЭрихМария ремарк|51|+79992223344|remark@@@@@lit....gb.bg  
Эрих Мария Ремарк|51|+7 (999) 222-3344|remark@lit.gb.bg  
  
Имя Фамилия|старый|домашний|test1@test2@domain.com  
Имя Фамилия|старый неверное поле|домашний неверное поле|test1@test2@domain.com неверное поле  ```  
