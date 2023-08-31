import urllib.request
import json
import face_recognition
import cv2


if __name__ == "__main__":
    video_capture = cv2.VideoCapture(0)

    face_locations = []
    face_encodings = []
    clear_name = ""

    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]

        if process_this_frame:
            clear_name = ""
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            if len(face_locations) != 0:
                face_encoding = face_encodings[0]
                data = {
                    "Inputs": {
                        "input1":
                            [
                                {
                                    'Col1': str(face_encoding[0]),
                                    'Col2': str(face_encoding[1]),
                                    'Col3': str(face_encoding[2]),
                                    'Col4': str(face_encoding[3]),
                                    'Col5': str(face_encoding[4]),
                                    'Col6': str(face_encoding[5]),
                                    'Col7': str(face_encoding[6]),
                                    'Col8': str(face_encoding[7]),
                                    'Col9': str(face_encoding[8]),
                                    'Col10': str(face_encoding[9]),
                                    'Col11': str(face_encoding[10]),
                                    'Col12': str(face_encoding[11]),
                                    'Col13': str(face_encoding[12]),
                                    'Col14': str(face_encoding[13]),
                                    'Col15': str(face_encoding[14]),
                                    'Col16': str(face_encoding[15]),
                                    'Col17': str(face_encoding[16]),
                                    'Col18': str(face_encoding[17]),
                                    'Col19': str(face_encoding[18]),
                                    'Col20': str(face_encoding[19]),
                                    'Col21': str(face_encoding[20]),
                                    'Col22': str(face_encoding[21]),
                                    'Col23': str(face_encoding[22]),
                                    'Col24': str(face_encoding[23]),
                                    'Col25': str(face_encoding[24]),
                                    'Col26': str(face_encoding[25]),
                                    'Col27': str(face_encoding[26]),
                                    'Col28': str(face_encoding[27]),
                                    'Col29': str(face_encoding[28]),
                                    'Col30': str(face_encoding[29]),
                                    'Col31': str(face_encoding[30]),
                                    'Col32': str(face_encoding[31]),
                                    'Col33': str(face_encoding[32]),
                                    'Col34': str(face_encoding[33]),
                                    'Col35': str(face_encoding[34]),
                                    'Col36': str(face_encoding[35]),
                                    'Col37': str(face_encoding[36]),
                                    'Col38': str(face_encoding[37]),
                                    'Col39': str(face_encoding[38]),
                                    'Col40': str(face_encoding[39]),
                                    'Col41': str(face_encoding[40]),
                                    'Col42': str(face_encoding[41]),
                                    'Col43': str(face_encoding[42]),
                                    'Col44': str(face_encoding[43]),
                                    'Col45': str(face_encoding[44]),
                                    'Col46': str(face_encoding[45]),
                                    'Col47': str(face_encoding[46]),
                                    'Col48': str(face_encoding[47]),
                                    'Col49': str(face_encoding[48]),
                                    'Col50': str(face_encoding[49]),
                                    'Col51': str(face_encoding[50]),
                                    'Col52': str(face_encoding[51]),
                                    'Col53': str(face_encoding[52]),
                                    'Col54': str(face_encoding[53]),
                                    'Col55': str(face_encoding[54]),
                                    'Col56': str(face_encoding[55]),
                                    'Col57': str(face_encoding[56]),
                                    'Col58': str(face_encoding[57]),
                                    'Col59': str(face_encoding[58]),
                                    'Col60': str(face_encoding[59]),
                                    'Col61': str(face_encoding[60]),
                                    'Col62': str(face_encoding[61]),
                                    'Col63': str(face_encoding[62]),
                                    'Col64': str(face_encoding[63]),
                                    'Col65': str(face_encoding[64]),
                                    'Col66': str(face_encoding[65]),
                                    'Col67': str(face_encoding[66]),
                                    'Col68': str(face_encoding[67]),
                                    'Col69': str(face_encoding[68]),
                                    'Col70': str(face_encoding[69]),
                                    'Col71': str(face_encoding[70]),
                                    'Col72': str(face_encoding[71]),
                                    'Col73': str(face_encoding[72]),
                                    'Col74': str(face_encoding[73]),
                                    'Col75': str(face_encoding[74]),
                                    'Col76': str(face_encoding[75]),
                                    'Col77': str(face_encoding[76]),
                                    'Col78': str(face_encoding[77]),
                                    'Col79': str(face_encoding[78]),
                                    'Col80': str(face_encoding[79]),
                                    'Col81': str(face_encoding[80]),
                                    'Col82': str(face_encoding[81]),
                                    'Col83': str(face_encoding[82]),
                                    'Col84': str(face_encoding[83]),
                                    'Col85': str(face_encoding[84]),
                                    'Col86': str(face_encoding[85]),
                                    'Col87': str(face_encoding[86]),
                                    'Col88': str(face_encoding[87]),
                                    'Col89': str(face_encoding[88]),
                                    'Col90': str(face_encoding[89]),
                                    'Col91': str(face_encoding[90]),
                                    'Col92': str(face_encoding[91]),
                                    'Col93': str(face_encoding[92]),
                                    'Col94': str(face_encoding[93]),
                                    'Col95': str(face_encoding[94]),
                                    'Col96': str(face_encoding[95]),
                                    'Col97': str(face_encoding[96]),
                                    'Col98': str(face_encoding[97]),
                                    'Col99': str(face_encoding[98]),
                                    'Col100': str(face_encoding[99]),
                                    'Col101': str(face_encoding[100]),
                                    'Col102': str(face_encoding[101]),
                                    'Col103': str(face_encoding[102]),
                                    'Col104': str(face_encoding[103]),
                                    'Col105': str(face_encoding[104]),
                                    'Col106': str(face_encoding[105]),
                                    'Col107': str(face_encoding[106]),
                                    'Col108': str(face_encoding[107]),
                                    'Col109': str(face_encoding[108]),
                                    'Col110': str(face_encoding[109]),
                                    'Col111': str(face_encoding[110]),
                                    'Col112': str(face_encoding[111]),
                                    'Col113': str(face_encoding[112]),
                                    'Col114': str(face_encoding[113]),
                                    'Col115': str(face_encoding[114]),
                                    'Col116': str(face_encoding[115]),
                                    'Col117': str(face_encoding[116]),
                                    'Col118': str(face_encoding[117]),
                                    'Col119': str(face_encoding[118]),
                                    'Col120': str(face_encoding[119]),
                                    'Col121': str(face_encoding[120]),
                                    'Col122': str(face_encoding[121]),
                                    'Col123': str(face_encoding[122]),
                                    'Col124': str(face_encoding[123]),
                                    'Col125': str(face_encoding[124]),
                                    'Col126': str(face_encoding[125]),
                                    'Col127': str(face_encoding[126]),
                                    'Col128': str(face_encoding[127]),
                                }
                            ],
                    },
                    "GlobalParameters": {
                    }
                }

                body = str.encode(json.dumps(data))

                url = 'https://ussouthcentral.services.azureml.net/workspaces/6e99d3e58a3a4a8a9318ffd27eaf6e25/services/027396b45a264d2484836528b3acfa9a/execute?api-version=2.0&format=swagger'
                api_key = 'm07zEuv0qmi7aT1DLaOBz3FcYywIvz+UQyTcJpjyCh+RnhwLB7gRCkAYD6EZ2XzICuXLsTwXkCe4yWQZxtpNoA=='  # Replace this with the API key for the web service
                headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

                req = urllib.request.Request(url, body, headers)

                try:
                    response = urllib.request.urlopen(req)

                    result = response.read().decode('utf-8')
                    name = result.split(":")
                    clear_name = name[3].split('"')[1]
#                    print(clear_name)

                except urllib.request.ftperrors as error:
                    print("The request failed with status code: " + str(error.code))
                    print(error.info())
                    print(json.loads(error.read().decode("utf8", 'ignore')))

        process_this_frame = not process_this_frame
        if len(face_locations) != 0:
            face_loc_nula = face_locations[0]
            cv2.rectangle(frame, (face_loc_nula[3], face_loc_nula[0]), (face_loc_nula[1], face_loc_nula[2]), (0, 0, 255), 2)
            cv2.rectangle(frame, (face_loc_nula[3], face_loc_nula[2] - 20), (face_loc_nula[1], face_loc_nula[2]), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, clear_name, (face_loc_nula[3] + 6, face_loc_nula[2] - 6), font, 0.5, (255, 255, 255), 1)
        """
        for top, right, bottom, left in face_locations:
            print(right)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, clear_name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
        """
        cv2.putText(frame, "[Q]: Exit", (530, 470), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
