Всем привет!
![Hello](./pics/hello.jpg)
Захотелось поиграть с датасетом с myanimelist.com. Он старенький, а впрочем как раз будет актуально поделать все CRUD запросы.

Сперва захотелось поискать аниме, где только одна серия есть
![find](./pics/find.jpg)


Дальше попробуем добавить еще одно аниме в датасет, как раз там нет одной части одного известного тайтла
![insert_jojo](./pics/insert_jojo.jpg)
Проверим, что все окей
![find_jojo](./pics/find_jojo.jpg)
Кайф

Слишком ужасное аниме, стоит удалить
![delete](./pics/delete.jpg)
Пока непривык к синтаксису, а впрочем, данным промежуточным результатом я очень доволен.

Чото на первом месте неакутальное аниме, нужно обновить рейтинг актуальный, и количество посмотревших людей
![update](./pics/update.jpg)
Успокоили фанатов алхимика

Сделаем read запрос немного по-труднее. Посмотрим на топ рейтинга с ограничением на количество просмотров
![find_top](./pics/find_top.jpg)

Теперь посмотрим на статистику нашего запроса
![find_explain](./pics/find_explain.jpg)
![amount_of_docs](./pics/amount_of_docs.jpg)

Зафиксировали, что количество документов, проверенных за время выполнение запроса равно 12294, это параметр totalDocsExamined. Время для планирования и выполнения запроса записана в параметре executionTimeMillis, в нашем случае это 13 милисекунд.


Кажется, стоит сделать индекс именно по количеству просмотров, ибо релевантно смотреть на более менее популярные сериалы
![index](./pics/index.jpg)

Посмотрим теперь на количество исследованных документов
![amounD_lol](./pics/amound_of_docs_after_index.jpg)

Видим, что количество милисекунд у нас увеличилось на 2, а вот totalDocsExamined уменьшился в раз 6 примерно. Это наводит нас на мысль, что у нас не так много данных в БД, так что время работы у нас даже увеличилось, однако на более больших БД у нас время уменьшится, ведь количество проверенных за время выполнение запроса у нас уменьшилось в 6 раз. 

