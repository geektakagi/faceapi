import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

SUBSCRIPTION_KEY = '51cad757b0184072bea8239825472ec2'
URI_BASE = 'https://westcentralus.api.cognitive.microsoft.com'

class FaceAPI:
    """get face information using Microsoft FaceAPI"""

    __headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    }

    __params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    face_id = ""
    __face_all = ""

    # constructor is require to upload face image path
    def __init__(self, image_path):
        try:
            # response = requests.request('POST', URI_BASE + '/face/v1.0/detect', json=body, data=None, headers=self.__headers, params=self.__params)
            response = requests.request("POST", URI_BASE + "/face/v1.0/detect?", params=self.__params, data=open(image_path, 'rb'), headers=self.__headers)

            if(response):
                self.__face_all = json.loads(response.text)[0]
                # self.__face_all = self.__face_all[0]
                # print (json.dumps(self.__face_all, sort_keys=True, indent=2))

                self.face_id = self.__face_all['faceId']

        except Exception as e:
            print('Error:')
            print(e)
