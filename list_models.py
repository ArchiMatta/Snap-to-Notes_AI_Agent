from google.genai import Client

client = Client(api_key="AIzaSyDwb5s6Pbpbv20N9Cmjey9AHpJy0BJoBjA")

for m in client.models.list():
    print(m.name)