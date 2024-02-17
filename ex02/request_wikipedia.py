import requests
import json
import dewiki
import sys


def remove_html_tags(text):
    tag = False
    quote = False
    out = ""

    for char in text:
        if char == "<" and not quote:
            tag = True
        elif char == ">" and not quote:
            tag = False
        elif (char == '"' or char == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + char

    return out


def search_wikipedia(search_query):
    if not search_query:
        print("Erreur : Aucun terme de recherche fourni.")
        return

    try:
        response = requests.get(
            f"https://fr.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={search_query}"
        )
        response.raise_for_status()

        results = response.json()["query"]["search"]
        if not results:
            print("Aucun résultat trouvé.")
            return

        page_id = results[0]["pageid"]
        page_response = requests.get(
            f"https://fr.wikipedia.org/w/api.php?action=parse&format=json&pageid={page_id}&prop=text"
        )
        page_response.raise_for_status()

        wiki_text = page_response.json()["parse"]["text"]["*"]
        plain_text = dewiki.from_string(wiki_text)
        plain_text = remove_html_tags(plain_text)

        file_name = f"{search_query.replace(' ', '_')}.wiki"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(plain_text)

    except requests.RequestException as e:
        print(f"Erreur de requête : {e}")


if __name__ == "__main__":
    search_term = sys.argv[1] if len(sys.argv) > 1 else None
    search_wikipedia(search_term)
