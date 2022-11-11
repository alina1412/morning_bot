import httpx

from morning_bot.fetchers import logging
from ..config import Config

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Openweather:
    city = "Moscow"
    openweather_id = Config.WEATHER_ID

    @staticmethod
    async def get_answer():
        try:
            data = await Openweather.get_data()
            return Openweather.make_response(data)
        except Exception as exc:
            # logger.debug(exc)
            ...

    @staticmethod
    async def get_data():
        url = (
            "http://api.openweathermap.org" + f"/data/2.5/weather?q={Openweather.city}"
        )
        params = {"units": "metric", "appid": Openweather.openweather_id}

        async with httpx.AsyncClient() as client:
            resp = await client.get(url, params=params)
            data = resp.json()

            if data and "main" in data:
                return data
            print("weather not found")
            return None

    @staticmethod
    def make_response(data):
        temp = data.get("main", {}).get("temp", None)
        if temp is None:
            return {"type_text": "Sorry, an error had occurred"}
        return {
            "type_text": f"Temperature in {Openweather.city} now: "
            + str(round(temp))
            + " °C"
        }
