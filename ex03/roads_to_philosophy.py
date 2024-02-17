import sys
import requests
from bs4 import BeautifulSoup


def format_wikipedia_url(search_term):
    base_url = "https://en.wikipedia.org/wiki/"
    return base_url + "_".join(search_term.split())


def find_first_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    for paragraph in (
        soup.find(id="mw-content-text").find("div").find_all("p", recursive=False)
    ):
        links = paragraph.find_all("a")
        for link in links:
            if link["href"].startswith("/wiki/") and not link["href"].startswith(
                "/wiki/Help:"
            ):
                return "https://en.wikipedia.org" + link["href"]
    return None


def follow_links_to_philosophy(search_term):
    visited_pages = []
    current_page = format_wikipedia_url(search_term)

    while True:
        try:
            response = requests.get(current_page)
            response.raise_for_status()

            if response.url:
                print(response.url.split("/")[-1].replace("_", " "))

            if response.url in visited_pages:
                print("It leads to an infinite loop!")
                break

            visited_pages.append(response.url)

            if "Philosophy" in response.url:
                print(f"{len(visited_pages)} roads from {search_term} to philosophy")
                break

            first_link = find_first_link(response.text)
            if not first_link:
                print("It leads to a dead end!")
                break

            current_page = first_link
        except Exception as e:
            print(f"An error occurred: {e}")
            break


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py 'search_term'")
    else:
        follow_links_to_philosophy(sys.argv[1])
