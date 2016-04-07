from util import constant
import requests

# def get_text():
#     '''
#     Getting the text from the menu image
#     :return: Nothing!
#     '''
#
#     # URL to hit for getting text from the menu image
#     URL = constant.OCR_BASE_URL
#
#     # parameters needed by the API to get text
#     payload = {
#         'apikey': constant.OCR_API_KEY,
#         'url': constant.OCR_MENU_URL,
#     }
#
#     print 'Hitting the API'
#     # Hitting the API with needed headers and parameters
#     response = requests.post(URL, data=payload)
#
#     print response.text

def ocr_space_url(url, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()


def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


# if __name__ == '__main__':
    # get_text()
print 'file'
print ocr_space_file(filename='/Users/manishdwibedy/PycharmProjects/Top-Dishes-Zomato/data/menu.jpg')

# print 'URL'
# print ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg')

print 'Done'

# curl https://api.ocr.space/Parse/Image --data "apikey=helloworld&isOverlayRequired=false&url=http://i.imgur.com/31d5L5y.jpg"