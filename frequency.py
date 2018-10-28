import sys
import json


def get_tweet_list(fp):
    return fp.readlines()


def get_tweet_json(tweet_list):
    json_list = []
    for i in tweet_list:
        json_list.append(json.loads(i))
    return json_list  # first entry was not a tweet os it is removed here


def count_frequency(tweet_dict):
    master_count_list = {}
    for i in tweet_dict:  # For every tweet
        if "text" in i.keys() and i['lang'] == 'en':  # not all entries are tweets in the proper form or in english
            tweet_text = i["text"]  # get the text from the tweet
            tweet_words = tweet_text.split(" ")
            for word in tweet_words:   # for every word in a tweet
                word = word.lower()
                word = str(word.encode('ascii', 'ignore'))
                if word in master_count_list.keys():
                    master_count_list[word] += 1
                else:
                    master_count_list[word] = 1
    total_terms = float(sum(master_count_list.values()))
    print("TOTAL TERMS _-----------------------------------------------------", total_terms)
    for term in master_count_list.keys():
        print(term, master_count_list[term]/total_terms)


def main():
    tweet_file = open(sys.argv[1])
    #tweet_file = open('output.txt')
    tweet_list = get_tweet_list(tweet_file)
    tweet_json = get_tweet_json(tweet_list)
    count_frequency(tweet_json)


if __name__ == "__main__":
    main()