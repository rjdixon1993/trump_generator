import builtins
import csv
import re

#url matcher
url_re = "(http)[^\s]+"


# Imports csv file and creates a list of lists, each one containing a tweet and related stuff
with open('tweets.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
   
   #Initialise list to contain processed tweets
    tweets = []

    #Loop through each tweet and do whatever we need to it.
    for row in csv_reader:
        #Only do it if the thing contains a twitter handle
        if re.search(r"[.]*[@]\w*", row[4]) != None: 
            #Replace the twitter handle with @@@@@. Note the 1 at the end controls how many we 
            tweet_processed = re.sub(r"[.]*[@]\w*", "@@@@@", row[4], 1)

            #remove any twitter links
            tweet_processed_link_removed = re.sub(url_re, "",tweet_processed)

            #remove any last line breaks
            tweet_processed_no_breaks = tweet_processed_link_removed.replace("\n", " ")

            #fix quotes so we include the \ bit that means they work when put in JS
            tweet_processed_quote1 = tweet_processed_no_breaks.replace('"', r'\"')
            tweet_processed_quote2 = tweet_processed_no_breaks.replace("'", r"\'")

            #If it's already been put in the list don't put it in again
            #note this doesn't work because we do more processing
            if tweet_processed_quote1 in tweets:
                print ("repeated tweet, not counted")
            else:
                #Put it into the "tweets" list
                tweets.append(tweet_processed_quote1)
                print ("tweet added to list")
 
print (tweets)





with open('trump_tweets.txt', 'w', encoding="utf-8") as f:
    for item in tweets:
        f.write("\"%s\"\n," % item)

#A better way might to be create a list of single strings with the tweets.
#We can then put in a random string where the twitter handle was, which we just replace in JS with the name variable?

#So in JS, I want to put the name in:
#1. in between elements of the list - IE where there is a comma
#2. where there is a blank string. e.g. for x in list, if x is "", then add in the name



