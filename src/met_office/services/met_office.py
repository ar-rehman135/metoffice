url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/ranked/England.txt'
import requests

class Met_Office_Data:
    def get_data(self):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            return data






