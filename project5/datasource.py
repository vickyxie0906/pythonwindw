import requests
api_key="c017ac798470580402a9cebf01171858"
cityName="Taipei"

def get_forcast_data(cityName):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={cityName},tw&appid={api_key}&lang=zh_tw&units=metric"

    response = requests.get(url=url)

    if response.ok:
        print("下載成功")
        return response.json()["list"]
    else:
        print("下載失敗")
