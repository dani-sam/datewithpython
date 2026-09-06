import redis

r = redis.Redis(host="redis", port=6379)
count = r.incr("hits")
print(f"Hit count: {count}")
