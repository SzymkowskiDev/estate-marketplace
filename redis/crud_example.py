import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('mykey', 'myvalue')

value = r.get('mykey')
print(value)

# r.delete('mykey')
