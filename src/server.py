from va import va
from utils import Utils

class Server:
    is_running = False

    def start(self):
        self.is_running = True
        bot = va()
        while True:
            response = input("Enter: ")
            if response == "Bye" or response == "bye":
                break
            clean_response = bot.process(response)
            bot.respond(clean_response)
            Utils.new_line()
        self.is_running = False
    
    def get_is_running(self):
        return self.is_running
