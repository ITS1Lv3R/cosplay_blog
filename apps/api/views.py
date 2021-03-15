import json

import requests


access_token = '7c0aad1c7c0aad1c7c0aad1c4b7c7a1c0677c0a7c0aad1c228ec5f03919612511b0b4d1'
'https: // api.vk.com / method / METHOD_NAME?PARAMETERS & access_token = ACCESS_TOKEN & v = V'

response = requests.get(f'https://api.vk.com/method/photos.get?owner_id=55878884&album_id=249734649&rev=0&access_token={access_token}&v=5.130')
decoder_json = json.loads(response.text)
# text = decoder_json['response']['items'][1]['sizes']
print(decoder_json)
