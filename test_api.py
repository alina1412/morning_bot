import os
import sys
import httpx
import requests
import pytest


address = ("C:\\Users\\Алина\\AppData\\Local\\" +
           "GitHubDesktop\\git_projects\\morning_bot")

sys.path.append(address)
import config

from fetchers import site_openweathermap
dest_with_name = os.path.join(config.Config.TMP_DIR, "randname")


print(dest_with_name)


def test_get_weather_data():
    url = ("http://api.openweathermap.org" +
           f"/data/2.5/weather?q={site_openweathermap.Openweather.city}")
    params = {"units": "metric",
              "appid": site_openweathermap.Openweather.openweather_id}
    resp = requests.get(url, params=params)
    assert resp.ok is True


# pixabay is banned
def test_get_pic_data():
    url = 'https://pixabay.com/api/'
    params = {"key": config.Config.PIC_KEY, "q": "morning",
                "safesearch": "true", "per_page": 20}
    resp = requests.get(url, params=params)
  
    assert resp.ok is True
    data = resp.json()
    # print()

# test_get_data()
# test_get_pic_data()
