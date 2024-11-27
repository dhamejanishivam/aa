import requests

url = "https://api.telegram.org/bot8113534372:AAF2DahT2CQYToSvG7Z_VMZ_-0BmweybX5I/sendMessage"
chat_id = "1293804795"
message1 = ""




class Main:
    def __init__(self,message) -> None:
        global message1
        message1 = message

        url = "https://api.telegram.org/bot8113534372:AAF2DahT2CQYToSvG7Z_VMZ_-0BmweybX5I/sendMessage"
        chat_id = "1293804795"
        message = message1

        # Send location, link, and device details to Telegram bot
        self.response = requests.post(
            url,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "chat_id": chat_id,
                "text": message1
            }
        )

        self.check()
        

    def check(self):
        # Check if the request was successful
        if self.response.status_code == 200:
            print(str("Message sent successfully."))
        else:
            # return str(f"Failed to send message. Status code: {response.status_code}")
            print(str(f"Failed to send message. Status code: "))

if __name__ == "__main__":
    a = Main("Your custom message here")
    # print(a)