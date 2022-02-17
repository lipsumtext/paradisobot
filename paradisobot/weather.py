from pyowm import OWM
from pyowm.commons import exceptions 

with open('owm_api.txt') as owm_api:
    api_key = owm_api.read().strip()
    owm = OWM(api_key)

mgr = owm.weather_manager()

def weather(city):
    try:
        obs = mgr.weather_at_place(city)
        w = obs.weather
        location = 'Weather at {}, {}: '.format(obs.location.name, obs.location.country)
        return location
    except exceptions.NotFoundError:
        return "Location not found"

print(weather('adnKmmeci'))
# print(w.detailed_status, w.temperature('celsius'), w.wind(), obs.location.name, obs.location.country)

