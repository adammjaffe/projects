# Adam Jaffe
# amj2158
# Introduction to Computer Science for Engineers
# Professor Cannon
# file: Sentiments.py

# Import the necessary modules.
import string, datetime, csv, math
import tweet_tools as tt

def load_file():
    '''This loads and returns the chosen tweets file.'''

    print 'Welcome to the Python Tweet Analysis Wizard!'
    print 'First, enter the name of a file of tweets you would like to analyze.'
    
    # Make a list of words and their sentiment values.
    sent_list=tt.make_sent(csv)
    # Make a list of zip codes.
    zip_list=tt.make_zip(csv)
    # Make a list of tweets stored as dictionaries.
    tweets=tt.tweets_list()

    # For each tweet:
    for j in range(len(tweets)):
        # Isolate the text of the tweet.
        tweets_text=tt.tweet_text(j,tweets)
        # Split that text into individual words.
        tweets_words=tt.tweet_words(tweets_text,string)
        # Calculate the average sentiment of each tweet by identifying the
        # sentiment value of each word in the tweet.
        avg_sent=tt.sentiment_calc(tweets_words,sent_list,j)
        # Add the average sentiment value to the tweet under the dictionary key
        # 'sentiment'.
        tweets=tt.add_sent(j,tweets,avg_sent)
        # Isolate the latitude and longitude of each tweet.
        tweet_loc=tt.tweet_location(j,tweets)
        # Find the zip code and state of each tweet.
        geo_info=tt.find_zip(tweet_loc,zip_list)
        # Add that geographic information to the tweet under the dictionary
        # keys 'state' and 'zipcode'.
        tweets=tt.add_geo(j,tweets,geo_info)

    print 'The loading function has finished.'
    print 'To filter tweets, call the filtration function on the next line.'
    print 'Format your filters as such:'
    print "filtration(tweets, text='python', zipcode='10027', state='NY')"
    print 'most_positive(tweets,word)'
    print 'most_negative(tweets,word)'

    return tweets

def filtration(tweets,**kwargs):
    '''This is the filtering function.'''
    # Filter the list of tweets according to the user's preferences.
    filter_lists=tt.tweet_filter(tweets,**kwargs)
    # Merge the multiple lists of satisfactory tweets into one list.
    filtered_tweets=tt.list_merger(filter_lists)
    # Calculate the average sentiment value of the fully filtered list.
    list_sent=tt.avg_sent_of_list(filtered_tweets)
    # Write the filtered list of tweets to an outfile.
    tt.write_tweets(filtered_tweets)

    print list_sent

def most_positive(tweets,word):
    '''This returns the postal code of the state with the most positive
    sentiment value for tweets containing a certain word.'''
    # Make a list of postal codes.
    postal_list=tt.make_postal(csv)
    
    # Initialize a lowest possible sentiment value and a current state value.
    low_sent=-1.0
    current_state='None'

    # For every state in the postal code directory:
    for state in postal_list:
        # Filter the list of tweets by word and state and calculate the average
        # sentiment value of the filtered tweets.
        list_sent=tt.alt_filtration(tweets,word,state)

        # If that value is greater than the current minimum, reset the current
        # minimum.
        if list_sent!='No tweets meet these filtration criteria.' and \
            list_sent>low_sent:
            low_sent=list_sent
            current_state=state

    print current_state

def most_negative(tweets,word):
    '''This returns the postal code of the state with the most negative
    sentiment value for tweets containing a certain word.'''
    # Make a list of postal codes.
    postal_list=tt.make_postal(csv)
    
    # Initialize a lowest possible sentiment value and a current state value.
    low_sent=1.0
    current_state='None'

    # For every state in the postal code directory:
    for state in postal_list:
        # Filter the list of tweets by word and state and calculate the average
        # sentiment value of the filtered tweets.
        list_sent=tt.alt_filtration(tweets,word,state)

        # If that value is greater than the current minimum, reset the current
        # minimum.
        if list_sent!='No tweets meet these filtration criteria.' and \
            list_sent<low_sent:
            low_sent=list_sent
            current_state=state

    print current_state

tweets=load_file()
