import win32crypt
import os
encrypted_data = open("C:\\Users\\{}\\AppData\\Roaming\\MySQL\\Workbench\\workbench_user_data.dat".format(os.getlogin()), "rb").read()
clear_data = win32crypt.CryptUnprotectData(encrypted_data, None, None, None, 0)
print(clear_data)