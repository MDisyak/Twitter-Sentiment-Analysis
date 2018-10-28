import sys
import json


def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def get_tweet_list(fp):
    return fp.readlines()


def get_tweet_json(tweet_list):
    json_list = []
    for i in tweet_list:
        json_list.append(json.loads(i))
    return json_list  # first entry was not a tweet os it is removed here


def get_sentiment_dict():
    afinnfile = open("AFINN-111.txt")
    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores


def calculate_sentiment_for_new_words(tweet_dict, sentiment_dict):
    new_master_list_sentiment = {}
    for i in tweet_dict:                                # For every tweet
        sentiment_score = 0
        new_tweet_words = {}
        if "text" in i.keys() and i['lang'] == 'en':    # not all entries are tweets in the proper form or in english
            tweet_text = i["text"]                      # get the text from the tweet
            tweet_words = tweet_text.split(" ")
            for tweet_word in tweet_words:
                if tweet_word in sentiment_dict:        # if the word is in the sentiment dictionary
                    tweet_words.remove(tweet_word)      # remove the word
                    sentiment_score += sentiment_dict[tweet_word]

            #  Update master word list
            for word in set(tweet_words):               # for every word in the tweets
                word = word.lower()
                if sentiment_score < 0:
                    if word in new_master_list_sentiment:
                        new_master_list_sentiment[word] -= 1
                    else:
                        new_master_list_sentiment[word] = -1
                else:
                    if word in new_master_list_sentiment:
                        new_master_list_sentiment[word] += 1
                    else:
                        new_master_list_sentiment[word] = 1

    for key in new_master_list_sentiment:
        print(str(key.encode('ascii', 'ignore')), new_master_list_sentiment[key])


def main():
    # sent_file = open(sys.argv[1])
    tweet_file = open("output.txt")
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    sent_dict = get_sentiment_dict()
    tweet_list = get_tweet_list(tweet_file)
   # print(len(tweet_list))
    tweet_list_json = get_tweet_json(tweet_list)
    calculate_sentiment_for_new_words(tweet_list_json, sent_dict)


if __name__ == '__main__':
    main()
