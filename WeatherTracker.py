import pyowm

owm = pyowm.OWM('b328f479c725976b77d42cbc59f09391')  # You MUST provide a valid API key


# Search for current weather
observation = owm.weather_at_coords(48.082778, -121.969722)
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
print(w.get_humidity())          
print(w.get_temperature('fahrenheit'))

print (" Get weather short status")
print (w.get_status() )                                   
print (" Get detailed weather status")
print( w.get_detailed_status() )     
print(w.get_wind())                     
