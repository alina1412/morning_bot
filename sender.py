from config import Config
import requests


class Sender:
    def __init__(self):
        self.BOT_TOKEN = Config.BOT_TOKEN

    def send_data(self, data, person):
        for opt_sender in (TextSender, PictureSender):
            try:
                opt_sender().send(data, person)
            except:
                raise BaseException


class TextSender(Sender):
    # def __init__(self):
    #     super().__init__()
 
    def send(self, data, person):
        if "type_text" not in data:
            return
        print("sending text", data, self.BOT_TOKEN)
        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"
        params = {'chat_id': person, 
                  'text': 'Morning!\n' + data["type_text"]}
        requests.post(url, params=params)


class PictureSender(Sender):
    # def __init__(self):
    #     super().__init__()
       
    def send(self, data, person):
        if "type_picture_path" not in data:
            return
        default_caption=""
        if "default_caption" in data:
            default_caption = data["default_caption"]

        image_path = data["type_picture_path"]
        print("sending picture path", data, self.BOT_TOKEN)

        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendPhoto"
        params = {'chat_id': person, 'caption': 'Morning!\n' + default_caption, 
                "media_type": "photo"}
         
        # image_name = os.path.basename("matrix.jpg")
        with open(image_path, "rb") as pic_file:
            files={"photo": pic_file}
            requests.post(url, params=params, files=files)



     
