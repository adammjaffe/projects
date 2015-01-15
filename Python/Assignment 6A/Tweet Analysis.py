# Adam Jaffe
# amj2158
# Introduction to Computer Science for Engineers
# Professor Cannon
# file: Tweet Analysis.py

# Import the necessary modules.
import string, datetime, csv, math

def main():
    '''This is the main operating function.'''
    zip_list=make_zip(csv)
    tweets=tweets_list()
    for j in range(len(tweets)):
        tweet_loc=tweet_location(j,tweets)
        geo_info=find_zip(tweet_loc,zip_list)
        geo_tweets=add_geo(j,tweets,geo_info)
        write_tweets(geo_tweets)

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

def tweet_text(item):
    '''Return the text of a tweet as a string.'''
    # Locate the text of the tweet in the dictionary and return it as a string.
    tweets_text=str(item['text'])
    
    return tweets_text

def tweet_words(tweets_text,string,item):
    '''Return a list of the words in the text of a tweet not
    including punctuation.'''
    # Split the string of text into a list of string bits that make up the
    # tweet.
    tweets_text=tweets_text.split()

    # Strip each string bit of all punctuation as defined by string.punctuation.
    for i in range(len(tweets_text)):
        tweets_text[i]=tweets_text[i].strip(string.punctuation)

    # Join the pieces back into a whole tweet.
    tweet_words=' '.join(tweets_text)

    # Return the stripped text.
    return tweet_words

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
    d2=10000.0

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
    tweets[j]['zip']=geo_info[0]
    tweets[j]['state']=geo_info[1]

    return tweets

def write_tweets(geo_tweets):
    '''Writes the tweet includng geographic information to a text file with
    the name tweets.txt and designated outfile.'''
    # Open an outfile to write to.
    outfile=open('tweets.txt','w')
    
    # Convert each item in the geo_tweet dictionary to a string for writing.
    for item in geo_tweets:
        geo_tweet=str(item)
        
        # Write the tweet to the outfile.
        outfile.write(geo_tweet + '\n')

    # Close the outfile.
    outfile.close()

# Run the main function.
main()
