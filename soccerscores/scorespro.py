#Written by James Kelly on 28/06/13

import feedparser
import time
import datetime


def get_feed():
    url = "http://www.scorespro.com/rss/live-soccer.xml"
    feed = feedparser.parse(url)
    return feed


def extract_info(game):
    game_info = {}

    start = game['title'].find('#', 0)
    end = game['title'].find('vs', 0)
    game_info['home'] = game['title'][start+1:end-1]

    start = game['title'].find('#', start+1)
    end = game['title'].find(':', start)
    game_info['away'] = game['title'][start+1:end]

    start = game['title'].find(' ', end)
    end = game['title'].find('-', start)
    game_info['home_goals'] = game['title'][start:end]

    start = end + 1
    end = len(game['title'])
    game_info['away_goals'] = game['title'][start:end]

    game_info['summary'] = game['summary']
    game_info['timestamp'] = datetime.datetime.now()
    return game_info


def process_feed(feed):
    nicely_processed_feed = []
    for game in feed.entries:
        nicely_processed_feed.append(extract_info(game))
    return nicely_processed_feed


def get_feed_processed():
    return process_feed(get_feed())


def print_in_play_games():
    for info in get_feed_processed():
        if (info['summary'] != "Game Finished"):
            print info['home'] + " : " + info['home_goals']
            print info['away'] + " : " + info['away_goals']
            print info['summary']
            print ""
