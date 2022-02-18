import requests
import os

def weather(api_key, city):
    try:
         w_data = requests.get(("https://api.openweathermap.org/data" +
                                "/2.5/find?q={CITY}&appid={API_KEY}&units=metric").format(CITY=city, API_KEY=api_key)).json()["list"][0]
         location = 'Weather at {}, {} right now:'.format(w_data["name"], w_data["sys"]["country"])
         status = 'Status: {}'.format(w_data["weather"][0]["description"].title())
         temp = ('Temperature: {}\u00b0C ({}\u00b0C' +
                 ' max / {}\u00b0C min)').format(w_data["main"]["temp"], w_data["main"]["temp_max"], w_data["main"]["temp_min"])
         winds = 'Winds: {} m/s (from {}\u00b0)'.format(w_data["wind"]["speed"], w_data["wind"]["deg"])
         humidity = 'Humidity: {}%'.format(w_data["main"]["humidity"]) 
         return '{}\n\n{}\n{}\n{}\n{}'.format(location, status, temp, winds, humidity) 
    except IndexError:
        return 'Location not found'

'''
owm_api_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(owm_api_dir + '/owm_api.txt', 'r') as owm_api:
    api_key = owm_api.read().strip()
    # owm = OWM(api_key)
print(weather(api_key, 'manila'))
'''
