
from bs4 import BeautifulSoup
import browser_cookie3
import httpx

TARGET_URL = "https://www.boot.dev/lessons/92fb04e5-0a8b-44e4-b672-624e603646ac"
DOMAIN = "www.boot.dev"


def get_all_links():
    cookies = browser_cookie3.firefox(domain_name=DOMAIN)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        with httpx.Client(
            cookies=cookies,
            headers=headers,
            timeout=httpx.Timeout(60.0, connect=20.0)
        ) as client:
            print("Downloading page...")
            response = client.get(TARGET_URL)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html5lib")  # fallback parser
            print("Extracted links:")
            for tag in soup.find_all("a"):
                print(tag.get("href"))

    except Exception as e:
        print(f"Error: {e}")


get_all_links()
