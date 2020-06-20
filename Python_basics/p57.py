import time
from imp import reload
import module1
print("program entering to sleeping mode")
time.sleep(30)
reload(module1)
time.sleep(30)
reload(module1)
print("This is the last line of program")
