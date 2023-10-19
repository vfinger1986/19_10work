import time


class SolveDT:
    def curtime(fn):
        def wrapper(self):
            print("*****************")
            fn(self)
            print("*****************")

        return wrapper

    @curtime
    def mytime(self):
        dt = time.gmtime()
        print(dt.tm_hour + 3, ":", dt.tm_min)


dt = SolveDT()
dt.mytime()
