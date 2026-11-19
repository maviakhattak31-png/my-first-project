import urllib.request
from datetime import datetime

with open("sites.txt") as f:
    urls = f.read().split()

for url in urls:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = urllib.request.urlopen(url, timeout=5)
        result = now + " " + url + " UP " + str(response.status)
    except Exception:
        result = now + " " + url + " DOWN"
    print(result)
    with open("log.txt", "a") as log:
        log.write(result + "\n")
