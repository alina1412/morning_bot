from os import path

import pytest
import requests

from morning_bot.config import Config
from morning_bot.fetchers import site_openweathermap

dest_with_name = path.join(Config.TMP_DIR, "randname")


print(dest_with_name)

weather_app_id = site_openweathermap.Openweather().openweather_id
print(weather_app_id)


@pytest.mark.my
def test_get_weather_data():
    assert weather_app_id is not None
    url = (
        "http://api.openweathermap.org"
        + f"/data/2.5/weather?q={site_openweathermap.Openweather.city}"
    )
    params = {
        "units": "metric",
        "appid": weather_app_id,
    }
    resp = requests.get(url, params=params)
    assert resp.ok is True


# pixabay is banned
# def test_get_pic_data():
#     url = "https://pixabay.com/api/"
#     params = {
#         "key": Config.PIC_KEY,
#         "q": "morning",
#         "safesearch": "true",
#         "per_page": 20,
#     }
#     resp = requests.get(url, params=params)

#     assert resp.ok is True
#     data = resp.json()
# print()


# test_get_data()
# test_get_pic_data()
