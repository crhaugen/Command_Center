import pyowm

#PUT KEY BACK IN BEFORE RUNNING
owm = pyowm.OWM('ADD YOUR KEY')  # You MUST provide a valid API key


# Search for current weather, according to my location
observation = owm.weather_at_coords(48.082778, -121.969722) 
w = observation.get_weather()
print(w)                      # <Weather,
                              # status=Clouds>

# Weather details
print(w.get_humidity())          
print(w.get_temperature('fahrenheit'))

print (" Get weather short status")
print (w.get_status() )                                   
print (" Get detailed weather status")
print( w.get_detailed_status() )     
print(w.get_wind())                     
