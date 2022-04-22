from site_openweathermap import Openweather


class TemperatureManager:

    def get_morning_data(self) -> str:
        ans = Openweather.get_answer()
        if self.isvalid(ans):
            text = ans        
        return text # "Warm"

    def isvalid(self, ans):
        return True