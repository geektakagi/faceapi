import json
from faceapi import FaceAPI


if __name__ == '__main__':
    image_path = input('画像パス: ')
    my_face = FaceAPI(image_path)

    print(my_face.face_id)
    # print(json.dumps(my_face.face_all, sort_keys=True, indent=2))
