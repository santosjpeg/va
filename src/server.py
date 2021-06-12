import speech_recognition as sr

from va import va
from utils import Utils
from debug import Debug

class Server:
    is_running = False

    def start(self):
        self.is_running = True
        bot = va()
        while True:
            Debug.info("STARTING SERVER...")
            Debug.info("Running SpeechRecognition library version {}".format(sr.__version__))

            response = input("Enter: ")
            if response == "Bye" or response == "bye":
                break
            clean_response = bot.process(response)
            bot.respond(clean_response)
            Utils.new_line()

        Debug.info("CLOSING SERVER...")
        self.is_running = False
    
    def get_is_running(self):
        return self.is_running
