import sys
import json

#  containts state abbreviation as key and a list containing the  average longitude, average latitude,
#  and total senttment score of all tweets from that state, number of tweets from that state
avg_long_lat = {'AL':	[32.806671,	-86.791130, 0, 0],
                'AK':	[61.370716,	-152.404419, 0, 0],
                'AZ':	[33.729759,	-111.431221, 0, 0],
                'AR':	[	34.969704,	-92.373123, 0, 0],
                'CA':	[	36.116203,	-119.681564, 0, 0],
                'CO':	[	39.059811,	-105.311104, 0, 0],
                'CT':	[	41.597782,	-72.755371, 0, 0],
                'DE':	[	39.318523,	-75.507141, 0, 0],
                'DC':	[	38.897438,	-77.026817, 0, 0],
                'FL':	[	27.766279,	-81.686783, 0, 0],
                'GA':	[	33.040619,	-83.643074, 0, 0],
                'HI':	[	21.094318,	-157.498337, 0, 0],
                'ID':	[	44.240459,	-114.478828, 0, 0],
                'IL':	[	40.349457,	-88.986137, 0, 0],
                'IN':	[	39.849426, -86.258278, 0, 0],
                'IA':	[	42.011539,	-93.210526, 0, 0],
                'KS':	[	38.526600,	-96.726486, 0, 0],
                'KY':	[	37.668140,	-84.670067, 0, 0],
                'LA':	[	31.169546,	-91.867805, 0, 0],
                'ME':	[	44.693947,	-69.381927, 0, 0],
                'MD':	[	39.063946,	-76.802101, 0, 0],
                'MA':	[	42.230171,	-71.530106, 0, 0],
                'MI':	[	43.326618,	-84.536095, 0, 0],
                'MN':	[	45.694454,	-93.900192, 0, 0],
                'MS':	[	32.741646,	-89.678696, 0, 0],
                'MO':	[	38.456085,	-92.288368, 0, 0],
                'MT':	[	46.921925,	-110.454353, 0, 0],
                'NE':	[	41.125370,	-98.268082, 0, 0],
                'NV':	[	38.313515,	-117.055374, 0, 0],
                'NH':	[	43.452492,	-71.563896, 0, 0],
                'NJ':	[	40.298904,	-74.521011, 0, 0],
                'NM':	[	34.840515,	-106.248482, 0, 0],
                'NY':	[	42.165726,	-74.948051, 0, 0],
                'NC':	[	35.630066,	-79.806419, 0, 0],
                'ND':	[	47.528912,	-99.784012, 0, 0],
                'OH':	[   40.388783,	-82.764915, 0, 0],
                'OK':	[	35.565342,	-96.928917, 0, 0],
                'OR':	[	44.572021,	-122.070938, 0, 0],
                'PA':	[	40.590752,	-77.209755, 0, 0],
                'RI':	[	41.680893,	-71.511780, 0, 0],
                'SC':	[	33.856892,	-80.945007, 0, 0],
                'SD':	[	44.299782,	-99.438828, 0, 0],
                'TM':	[	35.747845,	-86.692345, 0, 0],
                'TX':	[	31.054487,	-97.563461, 0, 0],
                'UT':	[	40.150032,	-111.862434, 0, 0],
                'VT':	[	44.045876,	-72.710686, 0, 0],
                'VA':	[	37.769337,	-78.169968, 0, 0],
                'WA':	[	47.400902,	-121.490494, 0, 0],
                'WV':	[	38.491226,	-80.954453, 0, 0],
                'WI':	[	44.268543,	-89.616508, 0, 0],
                'WY':	[	42.755966,	-107.302490, 0, 0]}

def get_tweet_list(fp):
    return fp.readlines()


def get_tweet_json(tweet_list):
    json_list = []
    for i in tweet_list:
        json_list.append(json.loads(i))
    return json_list  # first entry was not a tweet os it is removed here


def get_location(tweet_dict, sent_dict):
    for i in tweet_dict:  # For every tweet
        if "text" in i.keys() and i['lang'] == 'en':  # not all entries are tweets in the proper form or in english
            sent_score = get_score_for_tweets(i["text"], sent_dict)
            tweet_coord = i["coordinates"] # get the text from the tweet
            if tweet_coord is not None:
                coords_diff = [999999, 9999999]  # The difference between reference long and lat and the tweet's long/lat
                coords = tweet_coord["coordinates"]
                long = coords[0]
                lat = coords[1]
                for value in avg_long_lat.values():
                    ref_long = value[0]
                    ref_lat = value[1]
                    long_diff = abs(ref_long-long)
                    lat_diff = abs(ref_lat-lat)
                    if long_diff < coords_diff[0] and lat_diff < coords_diff[1]:
                        state = avg_long_lat.keys()[avg_long_lat.values().index(value)]  # Prints george
                        avg_long_lat[state][2] = sent_score  # change score for sentiment from that state
                        avg_long_lat[state][3] += 1 # increment number of tweets
                        coords_diff = [long_diff, lat_diff]


def get_highest_sentiment_state():
    state_name = ""
    highest_avg_sent = -999999
    for state, data in avg_long_lat.items():
        if data[3] is not 0:                    # if there were tweets from this state
            avg_sent = data[2]/float(data[3])
            if avg_sent > highest_avg_sent:
                state_name = state
                highest_avg_sent = avg_sent
    print(state_name)

def get_sentiment_dict(sent_file):
    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores


def get_score_for_tweets(tweet_text, sentiment_dict):
        sentiment_score = 0
        for word, score in sentiment_dict.items():  # For every word in the sentiment dictionary
            word = word.decode('utf-8')
            if tweet_text.find(word) > -1:
                sentiment_score += score
        return sentiment_score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #sent_file = open('AFINN-111.txt')
    #tweet_file = open('output.txt')

    tweet_list = get_tweet_list(tweet_file)
    tweet_json = get_tweet_json(tweet_list)
    sent_dict = get_sentiment_dict(sent_file)
    get_location(tweet_json, sent_dict)
    get_highest_sentiment_state()


if __name__ == "__main__":
    main()