import pandas as pd
import matplotlib.pyplot as plt

import client

def get_client():
    return client.client

def getUser(username):
    client = get_client()

    user = client.get_user(username=username)

    print(user)

def count_tweets(query):
    client = get_client()

    count = client.get_recent_tweets_count(query=query)

    print(count.meta)

    df = pd.DataFrame(count.data)
    print(df)
    df.plot(x='start', y='tweet_count')
    plt.show()

# Driver code
if __name__ == '__main__':

    getUser("devdevdev1001")

    count_tweets("interest rates")