class debug:
    def info(self, log):
        print("INFO:{}".format(log))

    def debug(self, log):
        print("DEBUG:{}".format(log))

debugger = debug()
