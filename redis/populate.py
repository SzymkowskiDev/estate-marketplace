import redis
import random
import datetime

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def populate_transactions(r, n):
    for i in range(n):
        print('Populating redis with random transactions ...')
        offer_id = random.randint(1, 4657)
        seller_id = random.randint(1, 3000)
        buyer_id = random.randint(1, 2000)

        start_date = datetime.date(2020, 1, 1)  # start date
        end_date = datetime.date(2021, 12, 31)  # end date
        # calculate the number of days between the start and end dates
        delta = (end_date - start_date).days
        # generate a random number of days within the range
        random_days = random.randrange(delta)
        # add the random number of days to the start date to get the random date
        random_date = start_date + datetime.timedelta(days=random_days)

        random_key = 'offer_' + str(offer_id) + '_seller_' + str(seller_id) + '_buyer_' + str(buyer_id) + '_date_' + str(random_date)

        options = ['placed', 'accepted', 'completed', 'aborted']
        # values: placed (buyer asks to buy) -> accepted (seller accepted, awaiting payment) -> completed (buyer made payment)
        # also: aborted (any system error or unexpected situation in the business flow)
        random_status = random.choice(options)

        r.set(random_key, random_status)



# delete all keys and their values
r.flushall()

# Generate 1000 random transactions
populate_transactions(r, 1000)