from src.app.app import *
import os

if __name__ == "__main__":
    DeleteDriverFolder()
    time.sleep(10)

    os.system("pip uninstall webdriver-manager -y")
    os.system("pip install webdriver-manager")
    time.sleep(10)
    RobotClass()