import time
import sys

def countdown(t):
   time_start = time.time() + t
   minutes = int(t/60)#int(time_start.strftime("%M"))
   seconds = seconds = int(time_start - time.time()) - minutes * 60#int(time_start.strftime("%S"))
   while time_start > time.time():
      try:
         sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
         sys.stdout.flush()
         time.sleep(1)
         seconds = int(time_start - time.time()) - minutes * 60
         #print(seconds)
         if seconds <= -1:
            if minutes == 0:
               print("\nTime's up")
               break
            minutes -= 1
            seconds = 59
      except KeyboardInterrupt, e:
         break

#countdown(120)
#countdown(70)
countdown(1801)