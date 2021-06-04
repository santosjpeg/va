from va import va
from draw import newline

def main():
    bot = va()
    response = input("Enter: ")

    while(response != 'bye'):
        bot.reply(response)
        newline()

        response = input("Enter: ")

if __name__ == '__main__':
    main()
