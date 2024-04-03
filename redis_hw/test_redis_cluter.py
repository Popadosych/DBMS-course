import redis
import json
import time

client = redis.RedisCluster(host="127.0.0.1", port=7000)
events = {}

json_file = open('large-file.json', 'r')
output = open('cluster_result.txt', 'w')
events = json.load(json_file)




print("------------SAVING------------", file=output)

start_time = time.time()
for i in range(len(events)):
	client.set(i, str(events[i]))
print("str", time.time() - start_time, file=output)

start_time = time.time()
for i in range(len(events)):
	client.hset("hset_events", i, str(events[i]))
print("hset", time.time() - start_time, file=output)

start_time = time.time()
for i in range(len(events)):
	client.execute_command("ZADD", "zset_events", i, str(events[i]))
print("zset", time.time() - start_time, file=output)

start_time = time.time()
for i in range(len(events)):
	client.rpush("list_events", str(events[i]))
print("list", time.time() - start_time, file=output)




print("------------READING------------", file=output)

start_time = time.time()
client.get(5555)
print("str", time.time() - start_time, file=output)

start_time = time.time()
client.hget("hset_events", 5555)
print("hset", time.time() - start_time, file=output)

start_time = time.time()
client.zrange("zset_events", 5555, 5555)
print("zset", time.time() - start_time, file=output)

start_time = time.time()
client.lrange("list_events", 5555, 5555)
print("list", time.time() - start_time, file=output)



json_file.close()
output.close()