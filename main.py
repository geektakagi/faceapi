import json
from faceapi import FaceAPI


if __name__ == '__main__':
    my_face = FaceAPI('https://scontent-nrt1-1.xx.fbcdn.net/v/t1.0-9/17498557_435197880145834_6401476424887113095_n.jpg?oh=42b2d4013c951bf7ddb1edf35e83a680&oe=59FDC246')

    print(my_face.face_id)
    # print(json.dumps(my_face.face_all, sort_keys=True, indent=2))
