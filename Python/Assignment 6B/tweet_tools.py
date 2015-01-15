# Adam Jaffe
# amj2158
# Introduction to Computer Science for Engineers
# Professor Cannon
# file: Tweet Tools.py

# Import the necessary modules.
import string, datetime, csv, math

def make_sent(csv):
    '''Return sentiment values in a list of dictionaries.'''
    # Open the .csv file with the sentiment information.
    sentiment=open('sentiments.csv','r')

    # Create a list to store the dictionaries that define the sentiments.
    sent_list=[]

    # Open the reader to process the .csv file.
    var=csv.reader(sentiment)

    # For each entry in the sentiments file, get the necessary information
    # and store it as the appropriate data type.
    for sent in var:
        if sent!='':
            word=str(sent[0])
            val=float(sent[1])

            # Create the dictionary.
            sent_dic={'word':word,'value':val}

            # Insert the dictionary into the last position in the list.
            sent_list.insert(len(sent_list),sent_dic)

    # Close the file.
    sentiment.close()

    # Return the list of sentiment dictionaries.
    return sent_list

def make_zip(csv):
    '''Return a zip code, represented as a python dictionary.'''
    # Open the .csv file with the zip code information.
    zipcode=open('zips.csv','r')
        
    # Create a list to store the dictionaries that define the zip codes.
    zip_list=[]

    # Open the reader to process the .csv file.
    var=csv.reader(zipcode)

    # Ignore the first line of the .csv file that contains storage information
    # but no information about zip codes.
    for zip_line in var:
        if zip_line[0]!='zip code':
            # Store the necessary information as the data type it should be.
            zip_no=str(zip_line[0])
            state=str(zip_line[1][2:4])
            lat=float(zip_line[2][3:len(zip_line[2])-1])
            lon=float(zip_line[3][3:len(zip_line[3])-1])
            city=str(zip_line[4][2:len(zip_line[4])-1])
            
            # Create the dictionary by key and return it.
            zip_dic={'zip':zip_no,'state':state,'lat':lat,'lon':lon,'city':city}

            # Insert the zip code dictionary into the last position of the list.
            zip_list.insert(len(zip_list),zip_dic)

    # Close the file.
    zipcode.close()

    # Return the list of dictionaries.
    return zip_list

def make_postal(csv):
    '''This makes a list of postal codes by reading the .csv file
    postal_codes.csv'''
    # Open the .csv file.
    post_codes=open('postal_codes.csv','U')

    # Create a list to store the data in the .csv file.
    postal_list=[]

    # Open the reader to process the .csv file.
    var=csv.reader(post_codes)

    for postal_line in var:
        i=0
	if postal_line!='':
            # Isolate the postal code.
	    post_string=postal_line[i][0:2]
            # Append the information to the list.
            postal_list.append(post_string)
            i=i+1

    return postal_list

def tweets_list():
    '''This gradually adds individual tweet dictionaries to a list of tweets.'''
    # Create an empty list.
    tweets=[]

    # Create a file to keep track of errors.
    error_log=open('error_log.txt','w')
    
    # Open the user's choice of file containing tweets.
    infile=open(raw_input('Input file name:'), 'r')

    # For each line in the file, convert it to a tweet and add it to tweets
    # list of dictionaries.
    for i in infile:
        tweet=make_tweet(string,datetime,i,error_log)
        if tweet!={}:
            tweets.append(tweet)
            
    # Close the infile and the error file.
    infile.close()
    error_log.close()

    # Return the list of tweets.
    return tweets
        
def make_tweet(string,datetime,i,error_log):
    '''Return a tweet, represented as a Python dictionary.'''
    # Split the tweet data into a list.
    tweet_line=i.split()

    # If the tweet actually contains text, proceed to read it and store it as
    # a dictionary object.
    if len(tweet_line)>=5:
        # Determine the latitude of the tweet by reading only the characters of
        # the latitude data that have numbers.Determine the longitude in a
        # similar way.
        lat=float(tweet_line[0][1:len(tweet_line[0])-1])
        lon=float(tweet_line[1][0:len(tweet_line[1])-1])

        # Create a datetime object for the tweet by reading its time stamp.
        # Isolate the relevant integers from the date.
        d=tweet_line[3]
        d=d.split('-')
        for i in range(len(d)):
            d[i]=int(d[i])
        # Isolate the relevant integers from the time.
        t=tweet_line[4]
        t=t.split(':')
        for i in range(len(t)):
            t[i]=int(t[i])
        # If the date and time conditions are of the correct size, create
        # the datetime object. Otherwise, report the line as an error.
        if len(d)==3 and len(t)==3:
            dt=datetime.datetime(d[0],d[1],d[2],t[0],t[1],t[2])
        else:
            error_log.write('There is an error in a line that reads: ' + i)
            # Ensure that some result is returned to other functions, but set
            # it as an empty tweet.
            tweet={}

        # Create a string that contains the text of the tweet in only lowercase.
        first_word=str(tweet_line[5])
        text=first_word.lower()
        for j in range(6,len(tweet_line)):
            word=str(tweet_line[j])
            text=text+' '+word.lower()

        # Create the tweet as a dictionary and return it.
        tweet={'text':text,'time':dt,'lat':lat,'lon':lon}

    # If the tweet does not actually contain text, log it as an error.
    else:
        error_log.write('There is an error in a line that reads: ' + i)
        # Ensure that some result is returned to other functions, but set
        # it as an empty tweet.
        tweet={}

    return tweet

def tweet_text(j,tweets):
    '''Return the text of a specific tweet in tweets as a string.'''
    # Locate the text of the tweet in the dictionary and return it as a string.
    tweets_text=str(tweets[j]['text'])
    
    return tweets_text

def alt_tweet_text(tweet):
    '''Return the text of a tweet as a string.'''
    # Locate the text of the tweet in the dictionary and return it as a string.
    tweets_text=str(tweet['text'])
    
    return tweets_text

def tweet_words(tweets_text,string):
    '''Return a list of the words in the text of a tweet not
    including punctuation.'''
    # Split the string of text into a list of string bits that make up the
    # tweet.
    tweets_text=tweets_text.split()

    # Strip each string bit of all punctuation as defined by string.punctuation.
    for i in range(len(tweets_text)):
        tweets_text[i]=tweets_text[i].strip(string.punctuation)

    # Join the pieces back into a whole tweet.
    tweets_words=' '.join(tweets_text)

    # Return the stripped text.
    return tweets_words

def tweet_time(tweet):
    '''Return the datetime that represents when the tweet was posted.'''
    # Locate the datetime of the tweet in the dictionary and return it.
    tweet_time=tweet['time']

    return tweet_time

def tweet_location(j,tweets):
    '''Return an tuple that represents the tweet's location.'''
    # Locate the latitude and longitude of the tweet and save them as a tuple.
    # Return the tuple.
    lat=tweets[j]['lat']
    lon=tweets[j]['lon']

    tweet_loc=tuple([lat,lon])

    return tweet_loc
    
def find_zip(tweet_loc,zip_list):
    '''Return zip code associated with a tweets location data.'''
    # Create an initializing distance that is ensures at least one zip code is
    # within one radial distance of the location.
    d2=100.0

    # Create an initial likely_zip and likely_state value to be changed if
    # there exists one somewhere in the United States.
    likely_zip='Not in US'
    likely_state='Not in US'
    
    # Go through every zip code in the zip_list and calculate the distance
    # between it and the location of the tweet. The shortest distance suggests
    # that that is the zip code from which the tweet was sent.
    for i in zip_list:
        loc1=tweet_loc
        loc2=tuple([i['lat'],i['lon']])
        d1=geo_distance(loc1,loc2,math)
        if d1<d2:
            d2=d1
            likely_zip=str(i['zip'])
            likely_state=str(i['state'])

    # Package the zip code and state information as a tuple.
    geo_info=tuple([likely_zip,likely_state])
    
    # Return the tuple.
    return geo_info

def geo_distance(loc1,loc2,math):
    ''' Return the great circle distance (in miles) between two
    tuples of (latitude,longitude) by using the haversine formula.'''
    
    # Create shorthands for the different values within the tuples. r is the
    # radius of the earth in miles. Convert degree values to radians.
    lat1=math.radians(loc1[0])
    lon1=math.radians(loc1[1])
    lat2=math.radians(loc2[0])
    lon2=math.radians(loc2[1])
    r=3959

    # Create variious variable pieces to split the haversine formula into
    # more manageable bits to check and debug.
    lat_part=float(((math.sin(.5*(lat2-lat1)))**2))

    lon_part1=float((math.cos(lat1))*(math.cos(lat2)))
    lon_part2=float((math.sin(.5*(lon2-lon1)))**2)
    lon_part=float(lon_part1*lon_part2)

    a=float(lat_part+lon_part)
    c=float(2*(math.atan2(math.sqrt(a),math.sqrt(1-a))))

    # Calculate the distance by the haversine formula.
    d=float(r*c)

    return d

def add_geo(j,tweets,geo_info):
    '''Adds the new keys state and zip to each tweet dictionary it is given.'''
    # Add the new keys and values to the tweet dictionary.
    tweets[j]['zipcode']=geo_info[0]
    tweets[j]['state']=geo_info[1]

    return tweets

def sentiment_calc(tweets_words,sent_list,j):
    '''Calculate the avergae sentiment value for a tweet.'''
    # Split the words of the tweet into a list of bits of the tweet.
    tweets_words=tweets_words.split()
    
    # Create a variable to keep track of the total sentiment value of the tweet.
    sent_value=float(0)
    
    # Find the length of the tweet in number of words.
    length=len(tweets_words)

    # For each word in the list of bits, find the corresponding value and add
    # it to the total sentiment value variable.
    for word in tweets_words:
        for sent in sent_list:
            if word==sent['word']:
                sent_value=sent_value+sent['value']

    # Calculate the average sentiment value.
    if length==0:
        avg_sent='No tweets meet these filtration criteria.'
    else:
        avg_sent=float(sent_value/length)

    # Return the sentiment value for the tweet.
    return avg_sent

def add_sent(j,tweets,avg_sent):
    '''Adds the sentiment value to each tweet dictionary.'''
    # Add the new key and sentiment value to the tweet dictionary.
    tweets[j]['sentiment']=avg_sent

    return tweets

def write_tweets(filtered_tweets):
    '''Writes the tweet includng geographic information to a text file with
    the name tweets.txt and designated outfile.'''
    # Open an outfile to write to.
    outfile=open('tweets.txt','w')
    
    # Convert each item in the geo_tweet dictionary to a string for writing.
    for item in filtered_tweets:
        geo_tweet=str(item)
        
        # Write the tweet to the outfile.
        outfile.write(geo_tweet + '\n')

    # Close the outfile.
    outfile.close()

def tweet_filter(tweets,**kwargs):
    '''This filters the list of tweets into three lists: one of all tweets
    containing a specific word, one of all tweets from a specific zip code,
    and one of all tweets from a specific state.'''
    # Create the filter lists that will be filled by tweets that meet the
    # user's criteria.
    text_filter=[]
    zip_filter=[]
    state_filter=[]

    # Create some Boolean variables to determine if a certain filter list has
    # been made.
    check_text=False
    check_zip=False
    check_state=False

    # Associate a value for each filter type chosen by the user, i.e. if a user
    # sorted by state='NY', the filter type would be state and the value would
    # be 'NY.'
    for filt,val in kwargs.items():
        if filt=='text':
            check_text=True
        elif filt=='zipcode':
            check_zip=True
        elif filt=='state':
            check_state=True   
        for tweet in tweets:
            # If the user chose to filter by text and it has not yet been
            # filtered:
            if filt=='text':
                # Create a list of tweets that meet the user's specifications.
                text_filter=filter_by_word(tweet,val,text_filter)    
            # Filter by zip code as above.
            elif filt=='zipcode':
                zip_filter=filter_by_zip(tweet,val,zip_filter)    
            # Filter by state as above.
            elif filt=='state':
                state_filter=filter_by_state(tweet,val,state_filter)
                

    # If a certain type of filter were not implemented, pass the entire
    # list of tweets through.
    if check_text==False:
        text_filter=tweets
    if check_zip==False:
        zip_filter=tweets
    if check_state==False:
        state_filter=tweets

    filter_lists=tuple([text_filter,zip_filter,state_filter])
    
    return filter_lists

def filter_by_word(tweet,val,text_filter):
    '''This function filters the list tweets into a list called text_filter
    of only the tweets containing a word specified by the user.'''
    # Isolate the text
    tweets_text=alt_tweet_text(tweet)
    tweets_words=tweet_words(tweets_text,string)

    # If the filter word is in the list of words, add the tweet to the list of
    # tweets that meet the words criterion.
    if val in tweets_words:
        text_filter.append(tweet)

    return text_filter

def filter_by_zip(tweet,val,zip_filter):
    '''This function filters the list tweets into a list called zip_filter
    of only the tweets from a zip code chosen by the user.'''
    # If the zip code of the tweet is the same as that specified by the user,
    # add the tweet to the list of tweets that meet the zip code criterion.
    if tweet['zipcode']==val:
        zip_filter.append(tweet)

    return zip_filter

def filter_by_state(tweet,val,state_filter):
    '''This function filters the list tweets into a list called state_filter
    of only the tweets from a state chosen by the user.'''
    # If the state of the tweet is the same as that specified by the user,
    # add the tweet to the list of tweets that meet the state criterion.
    if tweet['state']==val:
        state_filter.append(tweet)

    return state_filter

def list_merger(filter_lists):
    '''This merges all the lists of tweets filtered by different criteria into
    one list of tweets that meet all filter criteria.'''
    # Create an empty list of tweets that satisfy all the filters.
    filtered_tweets=[]
    
    # Retrieve each filtered list from the tuple.
    text_filter=filter_lists[0]
    zip_filter=filter_lists[1]
    state_filter=filter_lists[2]

    # Find the smallest list of filtered tweets to speed up the search for the
    # intersection of the three filtered lists.
    len_text=len(text_filter)
    len_zip=len(zip_filter)
    len_state=len(state_filter)

    # If the list of tweets filtered by text is the shortest:
    if len_text<=len_zip and len_text<=len_state:
        # For each tweet that satisfies that filter:
        for i in text_filter:
            # If it also satisfies the other filters:
            if i in zip_filter:
                if i in state_filter:
                    # Add it to the list of filtered tweets.
                    filtered_tweets.append(i)

    # If the list of tweets filtered by zip code is the shortest, find the
    # list of tweets that satisfy all filters by the same method.
    elif len_zip<=len_text and len_zip<=len_state:
        for i in zip_filter:
            if i in text_filter:
                if i in state_filter:
                    filtered_tweets.append(i)

    # Otherwise, the list of tweets filtered by state is shortest. Find the
    # fully filtered list of tweets by the same method.
    elif len_state<=len_text and len_state<=len_zip:
        for i in state_filter:
            if i in text_filter:
                if i in zip_filter:
                    filtered_tweets.append(i)           

    # Return the filtered list.
    return filtered_tweets

def avg_sent_of_list(filtered_tweets):
    '''This calculates the average sentiment value of the list of tweets as
    filtered according to the user's preferences.'''
    # Create an initial sentiment value for the list.
    total_sent=0.0

    # Find the length of the totally filtered list.
    length=len(filtered_tweets)

    # For every tweet in the filtered list, add the sentiment value to the
    # total.
    for tweet in filtered_tweets:
        if isinstance(tweet['sentiment'],float):
            sent=float(tweet['sentiment'])
            total_sent=total_sent+sent

    # Find the average by dividing the toal by the length of the list.
    if length==0:
        list_sent='No tweets meet these filtration criteria.'
    else:
        list_sent=total_sent/length

    return list_sent

def alt_filtration(tweets,word,state):
    '''This is the filtering function that takes one word'''
    # Filter the list of tweets according to the user's preferences.
    filter_lists=alt_tweet_filter(tweets,word,state)
    # Merge the lists of filtered tweets.
    filtered_tweets=list_merger(filter_lists)
    # Calculate the average sentiment value of the fully filtered list.
    list_sent=avg_sent_of_list(filtered_tweets)

    return list_sent

def alt_tweet_filter(tweets,word,state):
    '''This filters the list of tweets into two lists: one of all tweets
    containing a specific word and one of all tweets from a specific state.'''
    # Create the filter lists that will be filled by tweets that meet the
    # user's criteria.
    text_filter=[]
    zip_filter=tweets
    state_filter=[]

    for tweet in tweets:
        if word!=None:
            # Create a list of tweets that meet the user's specifications.
            val=word
            text_filter=filter_by_word(tweet,val,text_filter)        
        # Filter by state as above.
        val=state
        state_filter=filter_by_state(tweet,val,state_filter)

    if word==None:
        text_filter=tweets

    filter_lists=tuple([text_filter,zip_filter,state_filter])
    
    return filter_lists
