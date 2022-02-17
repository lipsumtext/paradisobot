from pyowm import OWM
from pyowm.commons import exceptions 

with open('owm_api.txt', 'r') as owm_api:
    api_key = owm_api.read().strip()
    owm = OWM(api_key)

mgr = owm.weather_manager()

def weather(city):
    try:
        obs = mgr.weather_at_place(city)
        w = obs.weather
        location = 'Weather at {}, {} right now: '.format(obs.location.name, obs.location.country)
        status = 'Status: {}'.format(w.detailed_status.title())
        ctemp = w.temperature('celsius')
        ftemp = w.temperature('fahrenheit')
        temp = ('Temperature: {}\u00b0C / {}\u00b0F ({}\u00b0C max / ' + 
                '{}\u00b0 min)').format(ctemp['temp'], ftemp['temp'], ctemp['temp_max'], ctemp['temp_min'])
        winds = 'Winds: {} m/s (from {}\u00b0)'.format(w.wind()['speed'], w.wind()['deg'])
        return location + '\n\n' + status + '\n' + temp + '\n' + winds
    except exceptions.NotFoundError:
        return "Location not found"

print(weather('manila'))
# print(w.detailed_status, w.temperature('celsius'), w.wind(), obs.location.name, obs.location.country)

