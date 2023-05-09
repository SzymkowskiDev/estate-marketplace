import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# # Define a dictionary to store
# mydict = {'date': '2002-10-10', 'seller_id': 30, 'buyer_id': 45, 'offer_id': 23}

# # Set the dictionary in Redis as a hash
# r.hmset('offer_23_seller_30_buyer_45_date_2002-10-10', mydict)

# # Get the dictionary back from Redis
# stored_dict = r.hgetall('myhash')

# # Print the dictionary
# print(stored_dict)

r.set('offer_23_seller_30_buyer_45_date_2002-10-10', 'in progress')
# values: placed (buyer asks to buy) -> accepted (seller accepted, awaiting payment) -> completed (buyer made payment)
# also: 

value = r.get('mykey')
print(value)

# r.delete('mykey')