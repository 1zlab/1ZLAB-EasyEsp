
from libs import pyboard
pyb = pyboard.Pyboard('/dev/ttyUSB1')
pyb.enter_raw_repl()
res = pyb.exec_("""
import os
os.listdir()
""")

print(res)

pyb.exit_raw_repl()
