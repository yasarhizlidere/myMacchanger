import subprocess
print("myMacchanger sarted")

subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether","00:11:22:33:44:55"])
subprocess.call(["ifconfig","eth0","up"])