# ДЗ2 - Redis

В данном домашнем задании пробуем redis на вкус. Зашел на гитхаб ![redis-py](https://github.com/redis/redis-py) и почитаем ридмишку. Для начала, находим как скачать redis. Пожалуй, это стоит сделать

``` bash
docker run -p 6379:6379 -it redis/redis-stack:latest
```

Отлично. Теперь попробуем проделать запросы чтения и сохранения с json файлом (взял вот ![такой](./large-file.json)) с помощью разных структур. Для этого написал ![небольшой код](./test_redis.py). Получили результат в ![файл](./result.txt), но, на всякий, продублирую результат в отчете

```
------------SAVING------------
str 0.3634650707244873
hset 0.37328600883483887
zset 0.3713865280151367
list 0.3655095100402832
------------READING------------
str 5.269050598144531e-05
hset 3.409385681152344e-05
zset 4.744529724121094e-05
list 4.1961669921875e-05
```

Теперь перейдем к более трудному, к поднятию отказоусточего кластера. Действовал по этому ![гайду](https://ilhamdcp.hashnode.dev/creating-redis-cluster-with-docker-and-compose), и давайте кратко скажу шаги, которые были сделаны:

1. Сделали 6 директорий: 7000, 7001, ..., 7005, в которых каждом из которых лежит ![файл](./7000/redis.conf), в котором записано:

```
 port 7000
 cluster-enabled yes
 cluster-config-file nodes.conf
 cluster-node-timeout 5000
 appendonly yes
 bind 0.0.0.0
```

(ну и понятно, что в разных папках разные порты)

2. Запустили ноды на каждом из 6 терминалов с помощью команды

``` bash
 docker run -v `pwd`/7000:/redis --name node-1 -p 7000:7000 --network redis-cluster redis redis-server /redis/redis.conf
```

3. В 7 терминале подключаемся к одной из нод, например

``` bash
 docker exec -it node-1 bash
```

Ну и там уже запускаем кластер: 

``` bash
redis-cli -p 7000 --cluster create node-1:7000 node-2:7001 node-3:7002 node-4:7003 node-5:7004 node-6:7005 --cluster-replicas 1 --cluster-yes
```

Получаем победу


