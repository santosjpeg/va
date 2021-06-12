from debug import Debug

import datetime
from datetime import datetime as dt
from utils import Utils

class Date:
    @staticmethod
    def tell_time():
        current_time = Utils.get_time()
        print("It is {}".format(current_time))

    @staticmethod
    def tell_day():
        current_day = Utils.get_day()
        print("Today's date is {}".format(current_day))

    @staticmethod
    def tell_day_of_week():
        day_of_week = dt.today().strftime('%A')
        print("Today is a {}".format(day_of_week))
