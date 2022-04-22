import requests
from config import Config


class Openweather:
    city = "Moscow"
    openweather_id = Config.WEATHER_ID

    @staticmethod
    def get_answer():
        data = Openweather.get_data()
        return Openweather.return_data(data)

    @staticmethod
    def get_data():
        url = ("http://api.openweathermap.org" + 
              f"/data/2.5/weather?q={Openweather.city}")
        params = {"units": "metric", "appid": Openweather.openweather_id}
        data = requests.get(url, params=params).json()
        if data and "main" in data:
            return data
        print("weather not found")
        return None

    @staticmethod
    def return_data(data):
        return {"type_text": f"Temperature in {Openweather.city} now: " 
                + str(round(data["main"]["temp"])) + " *C"}
        # return {"type_text": "Warm"}

# print(Openweather.get_answer())
