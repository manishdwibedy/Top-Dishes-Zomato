import requests
import urllib
from util import constant

def getAccessTokenData():
    '''
    Returns the access token data needed to get the access token
    :return: access token data
    '''

    return "grant_type=client_credentials&client_id=" \
           + constant.client_id + \
            "&client_secret=" + urllib.quote(constant.client_secret, safe='')\
           + "&scope=http://api.microsofttranslator.com"

def getToken():
    '''
    Returns the access token for future API hits
    :return: access token in string format
    '''
    URL = "https://datamarket.accesscontrol.windows.net/v2/OAuth2-13"

    # Hitting the API with needed headers and parameters
    response = requests.post(URL, data=getAccessTokenData()).json()

    return response['access_token']


if __name__ == "__main__":
    token = getToken()

