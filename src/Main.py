from va import va

def main():
    bot = va()
    while(True):
        response = input("Enter: ")
        if response == 'bye':
            break
        else:
            bot.reply(response)

if __name__ == '__main__':
    main()
