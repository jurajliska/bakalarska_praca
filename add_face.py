#Tento skript sluzi na pridanie tvare do databazy pomocou webkamery. Z tvare na obraze je spraveny encoding, ktroy je
#odoslany webovej aplikacii, ktora ho ulozi do databazy.

import face_recognition
import json
import requests
import cv2

new_face_encoding = {}
video_capture = cv2.VideoCapture(0)

"""
known_face_encodings = {}
ja_image = face_recognition.load_image_file("ja.jpg")
known_face_encodings["Juraj Liska"] = (face_recognition.face_encodings(ja_image)[0]).tolist()

fejs1_image = face_recognition.load_image_file("fejs1.jpg")
known_face_encodings["Zena Jeden"] = (face_recognition.face_encodings(fejs1_image)[0]).tolist()
"""
"""fejs2_image = face_recognition.load_image_file("fejs2.jpg")
#known_face_encodings["Mendes"] = (face_recognition.face_encodings(fejs2_image)[0]).tolist()

#fejs3_image = face_recognition.load_image_file("fejs3.jpg")
#known_face_encodings["Zena Dva"] = (face_recognition.face_encodings(fejs3_image)[0]).tolist()


#collection.insert_one(known_face_encodings)
#collection.drop()

#x = collection.find_one()
#x = collection.find_one({}, {"_id": 0})
#print(x)"""
if __name__ == '__main__':
    name = input("Enter name:")

    face_locations = []
    face_encoding = []
    lenght = 0
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)
            lenght = len(face_locations)
        process_this_frame = not process_this_frame

        for top, right, bottom, left in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.putText(frame, "[Q]: Exit", (530, 470), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)
        cv2.putText(frame, "[SPACE]: Add face", (10, 470), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)
        cv2.imshow('Video', frame)

        k = cv2.waitKey(1)
        if k == 32:
            if lenght == 1:
                new_face_encoding[name] = (face_encoding[0]).tolist()
                url = "https://face-app.azurewebsites.net/addface"
#                url = "https://face-app-evo.azurewebsites.net/addface"
                data = json.dumps(new_face_encoding)
                headers = {'Content-type': 'application/json'}
                r = requests.post(url, data=data, headers=headers)
                print(r.text)
                url = "https://face-app.azurewebsites.net/knnupdate"
#                url = "https://face-app-evo.azurewebsites.net/knnupdate"
                r = requests.get(url)
                print(r.text)
                break

        if k & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

    print(new_face_encoding)
