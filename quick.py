import browser_cookie3
from bs4 import BeautifulSoup
import httpx

COMMAND_PREFIX = "bootdev run"
TARGET_URL = "https://www.boot.dev/lessons/92fb04e5-0a8b-44e4-b672-624e603646ac"
DOMAIN = "www.boot.dev"


def get_command():
    cookies = browser_cookie3.firefox(domain_name=DOMAIN)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        with httpx.Client(
            cookies=cookies,
            headers=headers,
            # generous timeout for slow net
            timeout=httpx.Timeout(60.0, connect=20.0)
        ) as client:
            print("Fetching full page...")
            response = client.get(TARGET_URL)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            matches = soup.find_all("a")
            for tag in matches:
                print(tag.get("href"))

    except httpx.RequestError as ex:
        print("Request failed:", ex)
    except httpx.TimeoutException as ex:
        print("Request timed out!")


get_command()
