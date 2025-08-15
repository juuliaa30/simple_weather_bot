import requests

def get_weather():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": "53.15,29.2333"}

    headers = {
        "x-rapidapi-key": "f1c62e4c5emsh6ff044012f1d34ap1ba3c8jsn0b995fdb0f9a",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()['current']['temp_c'], response.json()['current']['feelslike_c']