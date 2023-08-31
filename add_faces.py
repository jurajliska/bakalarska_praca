#Tento skript sluzi na pridanie viacerych tvari naraz do databazy. Obrazky s tvarami su vlozene do priecinka newfaces.
#Z kazdej tvare je spraveny encoding, ktory je odoslany webovej aplikacii, ktora ho ulozi do databazy.

import face_recognition
import os.path
import json
import requests

if __name__ == '__main__':

    for img_file in os.listdir("newfaces"):
        full_file_path = os.path.join("newfaces", img_file)
        image = face_recognition.load_image_file(full_file_path)
        face_bounding_boxes = face_recognition.face_locations(image)

        if len(face_bounding_boxes) != 1:
            print("Image {} can`t add: {}".format(img_file, "Didn`t find a face." if len(face_bounding_boxes) < 1 else
                                                            "Found more than one face."))
        else:
            face_encoding = face_recognition.face_encodings(image)[0].tolist()
            name = os.path.splitext(img_file)[0]
            new_face_encoding = {name: face_encoding}
            url = "https://face-app.azurewebsites.net/addface"
            data = json.dumps(new_face_encoding)
            headers = {'Content-type': 'application/json'}
            r = requests.post(url, data=data, headers=headers)
            print(r.text)

    print("Faces added.")

    url = "https://face-app.azurewebsites.net/knnupdate"
    r = requests.get(url)
    print(r.text)
