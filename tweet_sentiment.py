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


def get_score_for_tweet(tweet_dict):
    for i in tweet_dict:

        if "text" in i: #not all entries are tweets
            tweet_text = i["text"]


def main():
    # sent_file = open(sys.argv[1])
    tweet_file = open("output.txt")
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    sent_dict = get_sentiment_dict()
    tweet_list = get_tweet_list(tweet_file)
    tweet_list_json = get_tweet_json(tweet_list)
    get_score_for_tweet(tweet_list_json)


if __name__ == '__main__':
    main()
