import requests


class Proxy:
    def __init__(self, instance):
        self.instance = instance
        self.response = None

    def proxy(self):
        object_instance = self.instance
        print("proxy actuando...")
        if object_instance.number % 2 == 0:
            self.response = requests.get(f"https://restcountries.eu/rest/v2/region/asia")
            return self.response.content
        else:
            self.response = requests.get(f"https://restcountries.eu/rest/v2/region/europe")
            return self.response.content
