import urllib.request

url = "http://example.com"

try:
    response = urllib.request.urlopen(url, timeout=5)
    print(url, "is UP, status", response.status)
except Exception:
    print(url, "is DOWN")
