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
        #print(i)
        json_list.append(json.loads(i))
    return json_list  # first entry was not a tweet os it is removed here


def get_sentiment_dict():
    afinnfile = open("AFINN-111.txt")
    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores


def get_score_for_tweets(tweet_dict, sentiment_dict):
    for i in tweet_dict:                        # For every tweet
        sentiment_score = 0
        if "text" in i.keys() and i['lang'] == 'en':  # not all entries are tweets in the proper form or in english
            tweet_text = i["text"]             # get the text from the tweet
            for word, score in sentiment_dict.items():         # For every word in the sentiment dictionary
                #unicode(word, 'unicode')
               # print(type(word), type(score), type(tweet_text))
              #  print(word, score, tweet_text)
              #  tweet_text = str(tweet_text.encode('utf-8'))
               # word = str(word.encode('utf-8'))
               # print(type(word), type(score), type(tweet_text))
                word = word.decode('utf-8')
               # print(type(word), type(score), type(tweet_text))
               # print(word, score, tweet_text)
                if tweet_text.find(word) > -1:
                    sentiment_score += score
        print(sentiment_score)





def main():
    # sent_file = open(sys.argv[1])
    tweet_file = open("newline_output.txt")
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    sent_dict = get_sentiment_dict()
    tweet_list = get_tweet_list(tweet_file)
    print(len(tweet_list))
    tweet_list_json = get_tweet_json(tweet_list)
    get_score_for_tweets(tweet_list_json, sent_dict)


if __name__ == '__main__':
    main()
