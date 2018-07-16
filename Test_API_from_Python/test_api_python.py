import requests


def main():
    # my code here
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    for key, value in response.json().items():
        print (key, value)

    return 0

if __name__ == "__main__":
    main()