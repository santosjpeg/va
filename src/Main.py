from va import va
from draw import drawing 

def main():
    bot = va()
    response = input("Enter: ")

    while(response != 'bye'):
        bot.reply(response)
        drawing.newline()
        response = input("Enter: ")

if __name__ == '__main__':
    main()
