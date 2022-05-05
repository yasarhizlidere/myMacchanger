import subprocess
print("myMacchanger sarted")
interface = "eth0"
mac_adress = "00:33:66:33:78:65"

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_adress])
subprocess.call(["ifconfig",interface,"up"])