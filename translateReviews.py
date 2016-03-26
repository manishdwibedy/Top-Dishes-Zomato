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

def translate(token, text, destinationLanguage):
    '''
    Translate the given text
    :param token: the access token
    :param text: the text to be translated
    :param destinationLanguage: the destination language
    :return: text in the destination Language
    '''

    translation_args = {
        'text': text,
        'to': destinationLanguage,
        'from': 'en'
        }

    headers={'Authorization': 'Bearer '+ token}
    translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
    translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)

    return translation_result.text

if __name__ == "__main__":
    token = getToken()

    translate(token, "Hello World", 'hi')

