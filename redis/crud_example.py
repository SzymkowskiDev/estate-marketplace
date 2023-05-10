import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# value = r.get('offer_23_seller_30_buyer_45_date_2002-10-10')
# print(value)

# r.delete('mykey')

# get the first 100 key-value pairs
keys_iter = r.scan_iter(count=100)
for key in keys_iter:
    value = r.get(key)
    print(key.decode('utf-8'), value.decode('utf-8'))
