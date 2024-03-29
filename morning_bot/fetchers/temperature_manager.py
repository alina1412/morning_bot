from morning_bot.fetchers.site_openweathermap import Openweather


class TemperatureManager:
    async def get_morning_data(self) -> dict:
        ans = await Openweather.get_answer()
        if self.isvalid(ans):
            return ans
        return {}

    def isvalid(self, data) -> bool:
        # {'type_text': 'Temperature in Moscow now: 8 *C'}
        return "type_text" in data
