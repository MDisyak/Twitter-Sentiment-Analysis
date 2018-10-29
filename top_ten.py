import json
import sys


def get_tweet_list(fp):
    return fp.readlines()


def get_tweet_json(tweet_list):
    json_list = []
    for i in tweet_list:
        json_list.append(json.loads(i))
    return json_list  # first entry was not a tweet os it is removed here


def get_hashtags_and_count(tweet_dict):
    hashtag_dict = {}
    for i in tweet_dict:                                # For every tweet
        if "entities" in i.keys() and i['lang'] == 'en':    # not all entries are tweets in the proper form or in english
            entity = i["entities"]                      # get the entities object from the tweet
            hashtags = entity["hashtags"]
            for hashtag in hashtags:
                if hashtag in hashtag_dict:
                    hashtag_dict[hashtag] += 1
                else:
                    hashtag_dict[hashtag] = 1
    return hashtag_dict


def get_top_10_hashtags(hashtags_dict):
    hashtag_freq = hashtags_dict.values()
    total_hashtag_freq = sum(hashtag_freq)
    sorted_freq = sorted(hashtag_freq, reverse=True)
    top_ten_freq = sorted_freq[:10]
    for freq in top_ten_freq:
        print(hashtags_dict.keys()[hashtags_dict.values().index(freq)], freq/float(total_hashtag_freq))


def main():
    tweet_file = open(sys.argv[1])
    #tweet_file = open("output.txt")
    tweet_list = get_tweet_list(tweet_file)
    tweet_list_json = get_tweet_json(tweet_list)
    hashtags_count = get_hashtags_and_count(tweet_list_json)
    get_top_10_hashtags(hashtags_count)


if __name__ == '__main__':
    main()
