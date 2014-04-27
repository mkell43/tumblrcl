import sys
import yaml
import tumblrtokens

from os import stat
from os.path import isfile, expanduser


auth_file = expanduser("~") + '/tumblrauth'


def auth_check_file():

    if isfile(auth_file) is False or stat(auth_file)[6] == 0:
        print "Looks like your auth file is either empty or doesn't exist."
        print "Please re-run with the create-auth command to build your auth file."
        sys.exit()
    # TODO :: Check to see if auth file authenticates appropriately.


def auth_tokens():

    auth_check_file()

    f = open(auth_file, "r")
    tokens = yaml.safe_load(f)
    f.close()

    return tokens


def auth_create(consumer_key, consumer_secret):

    if consumer_key is None or consumer_secret is None:
        raise Exception("Please make sure that consumer_key and consumer_secret are set.")

    # Set the URL to authorize against.
    authorize_url = 'http://www.tumblr.com/oauth/authorize'

    # Get our consumer.
    consumer = tumblrtokens.consumer(consumer_key, consumer_secret)

    # Get our request token.
    request_token = tumblrtokens.request_token(consumer)

    # Print out the authorization URL.
    print "\n\nPlease go to the url below to authorize:\n%s?oauth_token=%s" % (authorize_url,
                                                                               request_token['oauth_token'][0])
    request_response = raw_input("\n\nPaste the url you were redirected to below:\n")

    # Get our access token.
    access_token = tumblrtokens.access_token(consumer, request_response, request_token)

    # Build our tokens.
    tokens = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret,
        'oauth_token': access_token['oauth_token'][0],
        'oauth_token_secret': access_token['oauth_token_secret'][0]
    }

    # Open our file for writing to.
    f = open(auth_file, 'w')

    # Dump our tokens into the file and close it.
    yaml.dump(tokens, f, indent=2)
    f.close()

    print "New authfile created at " + auth_file