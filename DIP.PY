import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from piash import senayel
 
        senayel()
 
 
 
elif bit == "32bit":
 
        from fuck2 import senayel
 
 
        senayel()
 
