import requests
import json
import time


def main():
    # my code here
    url = " http://api.luftdaten.info/v1/push-sensor-data/"
    header = {
        'Content-Type': "application/json",
        'X-Pin': "1",
        'X-Sensor': "esp8266-11221763",
        'Cache-Control': "no-cache",
        'Postman-Token': "66f54d1c-4813-40c5-7467-3e104bc07603"
        }
    payload = "{\"software_version\": \"your_version\", \"sensordatavalues\":[{\"value_type\":\"P1\",\"value\":\"5.00\"},{\"value_type\":\"P2\",\"value\":\"5.00\"}]}"
    while True:
        response = requests.request("POST", url, data = payload, headers = header)
        print(response.status_code)
        time.sleep(60)
    
    print(response.status_code)

    for key, value in response.json().items():
        print (key, value)

    return 0

if __name__ == "__main__":
    main()