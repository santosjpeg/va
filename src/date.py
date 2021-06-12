from debug import Debug

import datetime
from datetime import datetime as dt

class Date:
    @staticmethod
    def tell_time(user_input):
        current_time = dt.today()
        current_hour = current_time.hour
        current_minute = current_time.minute 

        final_time = "{}:{} {}".format(current_hour if current_hour < 12 else current_hour - 12,
                "0{}".format(current_minute) if current_minute < 10 else current_minute,
                "A.M." if current_hour < 12 else "P.M.")

        print("It is currently {}".format(final_time))

    @staticmethod
    def tell_timezone(user_input):
        pass
