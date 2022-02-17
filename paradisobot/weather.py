from pyowm import OWM

with open('owm_api.txt') as owm_api:
    api_key = owm_api.read().strip()
    owm = OWM(api_key)
mgr = owm.weather_manager()

obs = mgr.weather_at_place('diliman')
w = obs.weather

print(w.detailed_status, w.temperature('celsius'), w.wind(), obs.location.name, obs.location.country)

