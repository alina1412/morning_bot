import os
import sys
import requests

address = ("C:\\Users\\Алина\\AppData\\Local\\" +
           "GitHubDesktop\\git_projects\\morning_bot")

sys.path.append(address)
import config
# import tg_chats
from fetchers import site_openweathermap
dest_with_name = os.path.join(config.Config.TMP_DIR, "randname")

config.Config.PIC_KEY
print(dest_with_name)


def get_data():
    url = ("http://api.openweathermap.org" +
           f"/data/2.5/weather?q={site_openweathermap.Openweather.city}")
    params = {"units": "metric",
              "appid": site_openweathermap.Openweather.openweather_id}
    resp = requests.get(url, params=params)
    assert resp.ok is True


get_data()
