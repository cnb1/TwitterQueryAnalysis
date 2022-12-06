import pandas as pd
import matplotlib.pyplot as plt

import client

def get_client():
    return client.client

def count_tweets(query):
    client = get_client()

    count = client.get_recent_tweets_count(query=query)

    # print(count.meta)

    df = pd.DataFrame(count.data)
    # print(df)
    df.plot(x='start', y='tweet_count')
    plt.show()

# Driver code
if __name__ == '__main__':

    toStop = False

    while not toStop:
        print("Type the command to search twitter: ")
        query = str(input())

        if query == "quit":
            toStop = True

        else :
            count_tweets(query)

    print("stopping the program...")