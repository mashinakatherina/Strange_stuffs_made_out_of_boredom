import subprocess

results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii", "ignore")
results = results.replace("\r", "")
ls = results.split("\n")
ls = ls[4:]
ssids = []
i = 0

while i < len(ls):
    if i % 5 == 0:
        ssids.append(ls[i])
    i += 1

i = 0
while i < len(ssids):
    print(ssids[i])
    i += 1
