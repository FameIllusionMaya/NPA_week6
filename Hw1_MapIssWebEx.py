import urllib.parse
import requests
import json


while True:
    location = input("Input location : ")
    if location[0] == '/':
        location = location[1::]
        key = "3H1rrUwZUU7Qvg6GtOXSvA8dxbxPlIMQ"
        main_api = "https://www.mapquestapi.com/geocoding/v1/address?"
        url = main_api + urllib.parse.urlencode({"key":key, "location":location})
        res = requests.get(url)
        result = res.json()
        lat_lng = result["results"][0]["locations"][0]["latLng"]

        main_api = "http://api.open-notify.org/iss-pass.json?"
        url = main_api + urllib.parse.urlencode({"lat":lat_lng["lat"], "lon":lat_lng["lng"]})
        res = requests.get(url)
        result = res.json()

        text1, text2 = '', ''
        for i in result["response"]:
            text1 += str(i["risetime"]) + " "
            text2 += str(i["duration"]) + " "

        message1 = "Latitude and Longtitude are " + str(lat_lng["lat"]) + " and " + str(lat_lng["lng"])
        message2 = "Amount pass : " + str(result["request"]["passes"]) + "\n" + "Rise time are " + text1 + "\n" + "Duration are " + text2
        print(message1)
        print(message2)

        access_token = "YjNlZDk0Y2EtNTMxYy00ZTJmLWJiYTktMTkyNjc3OGMwMTcyZTEyODE1Y2UtZjU3_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f"
        room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3"
        url = 'https://webexapis.com/v1/messages'
        message = message1 + "\n" + message2
        url = 'https://webexapis.com/v1/messages'
        headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
        }
        params = {'roomId': room_id, 'markdown': message}
        res = requests.post(url, headers=headers, json=params)
