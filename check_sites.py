import urllib.request

urls = ["http://example.com", "http://google.com", "http://thissitedoesnotexist12345.com"]

for url in urls:
    try:
        response = urllib.request.urlopen(url, timeout=5)
        print(url, "is UP, status", response.status)
    except Exception:
        print(url, "is DOWN")
