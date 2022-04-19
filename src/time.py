import time
def getTime():
            t = time.localtime()
            current_time = int(time.strftime("%H"+"%M", t))
            return current_time
print(getTime())