
from datetime import datetime

now = datetime.now() # current date and time

time = now.strftime("%H:%M:%S")
print("year:", time)