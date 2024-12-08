import requests

response = requests.get("https://jsonplaceholder.typicode.com/photos/1")

#print(response)
photos = response.json()
#print(photos)
print(f"Here is the title {photos['title']}, and the url {photos['thumbnailUrl']}")