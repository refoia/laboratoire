import requests
from bs4 import BeautifulSoup




def search(query):
  results = []
  query = query.replace(" ", "+")
  URL = f"https://www.google.com/search?q={query}"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  for item in soup.find_all("div", class_="g"):
    link = item.find("a").get("href")
    title = item.find("h3").text
    results.append({"title": title, "link": link})
  return results

query = input("Enter a search query: ")
results = search(query)
for result in results:
  print(result["title"])
  print(result["link"])
  print()
