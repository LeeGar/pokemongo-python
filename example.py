import time
import requests
import json

from skiplagged import Skiplagged


if __name__ == '__main__':
    client = Skiplagged()
    
    #bounds = (
  #          (40.76356269219236, -73.98657795715332), # Lower left lat, lng
   #           (40.7854671345488, -73.95812508392333) # Upper right lat, lng
    #          ) # Central park, New York City
    #bounds = client.get_bounds_for_address('13290 SW Davies Rd Beaverton, OR 97008')

    def get_bounds_for_lat_long(self, lat, lon, offset=0.003):
        return (
                (lat - offset, lon - offset),
                (lat + offset, lon + offset),
                )
    
    while 1:
      try:
          # Log in with a Google or Pokemon Trainer Club account
          print client.login_with_google('', '')
          #print client.login_with_pokemon_trainer('USERNAME', 'PASSWORD')
          
          # Get specific Pokemon Go API endpoint
          print client.get_specific_api_endpoint()
          
          # Get profile
          print client.get_profile()
          
          # get current lat long
          latLon = json.loads(requests.get('https://pradar.herokuapp.com/current').content)
          print 'latLong!', latLon['lat'], latLon['long']
          bounds = get_bounds_for_lat_long(None, latLon['lat'], latLon['long'])
          print 'BOUNDS!', bounds
          # Find pokemon
          for pokemon in client.find_pokemon(bounds):
              print pokemon
      except Exception as e:
          print "exception:", e
          time.sleep(1)
            