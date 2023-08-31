# Tento skript sluzi na identifikaciu tvari. Na obraze z webkamery je z kazdej tvare spraveny encoding. Tieto encodingy
# su odoslane webovej aplikacii, ktora ich porovna s encodingmi v databaze. Aplikacia vrati mená, ktorými sú pomenované
# tvare na obraze. po ukonceni porogramu je vypisany zoznam identifikovanych tvari.

import face_recognition
import cv2
import json
import requests


if __name__ == "__main__":
    video_capture = cv2.VideoCapture(0)

    face_locations = []
    face_encodings = []
    process_this_frame = True
    predictions = []
    matches = 0
    are_here = []
    while True:
        ret, frame = video_capture.read()

        rgb_frame = frame[:, :, ::-1]

        if process_this_frame:
            matches = 0
            encodings = []
            predictions = []
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            if len(face_locations) != 0:
                for encoding in face_encodings:
                    encodings.append(encoding.tolist())
                jeson = {
                    "encodings": encodings
                }
                data = json.dumps(jeson)
#                url = "http://127.0.0.1:5000/getnames"
                url = "https://face-app.azurewebsites.net/getnames"
#                url = "https://face-app-evo.azurewebsites.net/getnames"
                headers = {'Content-type': 'application/json'}
                r = requests.post(url, data=data, headers=headers)
                predictions = r.json().get("result")
                matches = r.json().get("matches")

        process_this_frame = not process_this_frame
        """
        for name, (top, right, bottom, left) in predictions:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
        """
        for (top, right, bottom, left), name in zip(face_locations, predictions):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        cv2.putText(frame, "[Q]: Exit", (530, 470), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)
#        print("Rozpoynanych: " + str(matches))
        cv2.imshow('Video', frame)

        if len(predictions) > 0:
            for name in predictions:
                if name not in are_here and 'Unknown' not in name:
                    are_here.append(name)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    print("Are here: ")
    for nm in are_here:
        print(nm)
