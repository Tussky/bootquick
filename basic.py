import browser_cookie3
import requests

cj = browser_cookie3.firefox(domain_name="boot.dev")
response = requests.get(
    "https://www.boot.dev/lessons/e33ed517-42ab-4cfb-a5a6-3660777c9815", cookies=cj)
print(response.text)
