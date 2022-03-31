import time
import pyscreenshot


def sleeptime(hour, min, sec):
  return hour * 3600 + min * 60 + sec
num = 1
second = sleeptime(0, 0, 5)
while 1 == 1:
  time.sleep(second)
  image = pyscreenshot.grab()
  image.save('images/' + '%d' %num + ".png")
  num = num + 1

# 这是隔5秒执行一次
