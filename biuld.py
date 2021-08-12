import platform
from platform import node
from os import system

os = platform.system()
if os == 'Linux':
    currentdir = os.getcwd()
    cmd = 'sudo echo "{}/build/dps_startup.sh &" >> /etc/rc.local'.format(currentdir)
    print("program builded")

elif os == 'Windows':
    user = node()
    user_1 = user.replace("-PC","")
    cmd = 'copy build/dist/background.exe "C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\background.exe"'.format(user_1)
    system(cmd)
    print("program builded")
        
elif os == 'Darwin':
    print("your os not defind")
else:
    print("operating system not detected")

