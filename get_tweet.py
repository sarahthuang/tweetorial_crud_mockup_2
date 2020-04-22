import twitter

e = {}
with open('API_KEYS.env', 'r') as fle:
    for line in fle:
        key, val = line.strip().split('=')
        e[key] = val
        #if key.split('_')[0] == 'twitter':
            #e[key[8:].upper()] = val

t = twitter.Api(
    consumer_key=e["CONSUMER_KEY"],
    consumer_secret=e["CONSUMER_SECRET"],
    access_token_key=e["ACCESS_TOKEN"],
    access_token_secret=e["ACCESS_TOKEN_SECRET"],
    sleep_on_rate_limit=True
)


def tweet_url(t):
    return "https://twitter.com/%s/status/%s" % (t['user']['screen_name'], t['id'])

#status_id = '1250065535200616448'

def get_status(status_id):
    try:
        t1 = t.GetStatus(status_id).AsDict()
        print('url:\n', tweet_url(t1))
        print('\n\ntweet dict:\n', t1)
    except twitter.error.TwitterError as e:
        print('got twitter error:', e)
        print('looking at twitter status:', thread[0]['id'])

def get_username(status_id):
    try:
        t1 = t.GetStatus(status_id).AsDict()
        return t1['user']
    except twitter.error.TwitterError as e:
        print('got twitter error:', e)
        print('looking at twitter status:', thread[0]['id'])

def get_dict(status_id):
    try:
        t1 = t.GetStatus(status_id).AsDict()
        return t1
    except twitter.error.TwitterError as e:
        print('got twitter error:', e)
        print('looking at twitter status:', thread[0]['id'])
