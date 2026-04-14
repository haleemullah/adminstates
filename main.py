import requests
import json

def api_lookup(code):
    # URL taken from free api lookup site via Google
    url = "https://rawcdn.githack.com/kamikazechaser/administrative-divisions-db/master/api/" + code + ".json"
    return url

if __name__ == "__main__":

    country = input("2 digit ISO country code? ")
    print("")

    url = api_lookup(code=country.upper())
    payload = {}
    headers = {}    

    with open("countrymapping.json", "r") as f:
        data = json.load(f)
        full_name = data.get(country)

    # print(full_name)

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        admin_divisions = len(json.loads(response.text))
        print("{0} has {1} administrative divisions / provinces / states etc.".format(full_name, admin_divisions), "\n")
        print(response.text, "\n")
    except:
        print("2 digit country code is invalid. Try again.","\n")

# EOF