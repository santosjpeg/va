from va import va

class Server:
    is_running = False

    def start(self):
        self.is_running = True

        bot = va()
        response = input("Enter: ") 
        while response != "Bye" or response != "bye":
            cleaned_response = bot.clean(response)
            bot.respond(cleaned_response)

            response = input("Enter: ")

    def get_is_running(self):
        return self.is_running

