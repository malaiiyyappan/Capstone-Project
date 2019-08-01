import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests
import pandas as pd
from geopy.geocoders import Nominatim
import re

uber_model = pickle.load(open('model.pkl', 'rb'))
lyft_model = pickle.load(open('lyft.pkl', 'rb'))

a = np.zeros(shape=(1,52))
uber = pd.DataFrame(a,columns = ['distance', 'temp/f', 'cloud cover', 'pressure', 'rain' ,'humidity', 'wind', 'day_Monday', 'day_Saturday', 'day_Sunday',
           'day_Thursday', 'day_Tuesday', 'day_Wednesday', 'source_Beacon Hill',
           'source_Boston University', 'source_Fenway',
           'source_Financial District', 'source_Haymarket Square',
           'source_North End', 'source_North Station',
           'source_Northeastern University', 'source_South Station',
           'source_Theatre District', 'source_West End', 'hour_1', 'hour_2',
           'hour_3', 'hour_4', 'hour_5', 'hour_6', 'hour_7', 'hour_8', 'hour_9',
           'hour_10', 'hour_11', 'hour_12', 'hour_13', 'hour_14', 'hour_15',
           'hour_16', 'hour_17', 'hour_18', 'hour_19', 'hour_20', 'hour_21',
           'hour_22', 'hour_23', 'name_Black SUV', 'name_UberPool', 'name_UberX',
           'name_UberXL', 'name_WAV'])

lyft = pd.DataFrame(a,columns =['distance', 'temp/f', 'cloud cover', 'pressure',
       'rain', 'humidity', 'wind', 'day_Monday', 'day_Saturday', 'day_Sunday',
       'day_Thursday', 'day_Tuesday', 'day_Wednesday', 'source_Beacon Hill',
       'source_Boston University', 'source_Fenway',
       'source_Financial District', 'source_Haymarket Square',
       'source_North End', 'source_North Station',
       'source_Northeastern University', 'source_South Station',
       'source_Theatre District', 'source_West End', 'hour_1', 'hour_2',
       'hour_3', 'hour_4', 'hour_5', 'hour_6', 'hour_7', 'hour_8', 'hour_9',
       'hour_10', 'hour_11', 'hour_12', 'hour_13', 'hour_14', 'hour_15',
       'hour_16', 'hour_17', 'hour_18', 'hour_19', 'hour_20', 'hour_21',
       'hour_22', 'hour_23', 'name_Lux Black', 'name_Lux Black XL',
       'name_Lyft', 'name_Lyft XL', 'name_Shared'])

def get_coord_lat(place):
    geolocator = Nominatim(user_agent='myapplication',timeout=None)
    location = geolocator.geocode(place)
    if location != None:
        return location.raw['lat']

def get_coord_lon(place):
    geolocator = Nominatim(user_agent='myapplication',timeout=None)
    location = geolocator.geocode(place)
    if location != None:
        return location.raw['lon']



def give_day(X,day):

    if day == 'Monday':
        X['day_Monday'] = 1

    elif day == 'Tuesday':
        X['day_Tuesday'] = 1

    elif day == 'Wednesday':
        X['day_Wednesday'] = 1

    elif day == 'Thursday':
        X['day_Thursday'] = 1

    elif day == 'Saturday':
        X['day_Saturday'] = 1

    elif day == 'Sunday':
        X['day_Sunday'] = 1
    
    else:
        X.loc[:,['day_Monday', 'day_Saturday', 'day_Sunday','day_Thursday', 'day_Tuesday', 'day_Wednesday']] = 0
            
    return X

def give_hour(X,hour):
    
    if hour == 1:
            X['hour_1'] = 1

    elif hour == 2:
            X['hour_2'] = 1

    elif hour == 3:
            X['hour_3'] = 1    

    elif hour == 4:
            X['hour_4'] = 1  

    elif hour == 5:
            X['hour_5'] = 1     

    elif hour == 6:
            X['hour_6'] = 1     

    elif hour == 7:
            X['hour_7'] = 1 

    elif hour == 8:
            X['hour_8'] = 1         

    elif hour == 9:
            X['hour_9'] = 1        

    elif hour == 10:
            X['hour_10'] = 1         

    elif hour == 11:
            X['hour_11'] = 1 

    elif hour == 12:
            X['hour_12'] = 1  

    elif hour == 13:
            X['hour_13'] = 1 

    elif hour == 14:
            X['hour_14'] = 1 

    elif hour == 15:
            X['hour_15'] = 1 

    elif hour == 16:
            X['hour_16'] = 1 

    elif hour == 17:
            X['hour_17'] = 1 

    elif hour == 18:
            X['hour_18'] = 1 

    elif hour == 19:
            X['hour_19'] = 1 

    elif hour == 20:
            X['hour_20'] = 1 

    elif hour == 21:
            X['hour_21'] = 1 

    elif hour == 22:
            X['hour_22'] = 1 

    elif hour == 23:
            X['hour_23'] = 1 
            
    else:
        X.loc[:,['hour_1', 'hour_2',
           'hour_3', 'hour_4', 'hour_5', 'hour_6', 'hour_7', 'hour_8', 'hour_9',
           'hour_10', 'hour_11', 'hour_12', 'hour_13', 'hour_14', 'hour_15',
           'hour_16', 'hour_17', 'hour_18', 'hour_19', 'hour_20', 'hour_21',
           'hour_22', 'hour_23']] = 0       

    return X

def give_source(X, source):


    if source == 'Beacon Hill':
            X['source_Beacon Hill'] = 1

    elif source == 'Boston University':
            X['source_Boston University'] = 1

    elif source == 'Fenway':
            X['source_Fenway'] = 1    

    elif source == 'Financial District':
            X['source_Financial District'] = 1    

    elif source == 'Haymarket Square':
            X['source_Haymarket Square'] = 1  

    elif source == 'North End':
            X['source_North End'] = 1        

    elif source == 'North Station':
            X['source_North Station'] = 1       

    elif source == 'Northeastern University':
            X['source_Northeastern University'] = 1

    elif source == 'South Station':
            X['source_South Station'] = 1        

    elif source == 'Theatre District':
            X['source_Theatre District'] = 1       

    elif source == 'West End':
            X['source_West End'] = 1  
    else:
         X.loc[:,['source_Beacon Hill',
           'source_Boston University', 'source_Fenway',
           'source_Financial District', 'source_Haymarket Square',
           'source_North End', 'source_North Station',
           'source_Northeastern University', 'source_South Station',
           'source_Theatre District', 'source_West End']] = 0

    return X

def give_name_uber(X, name):


    if name == 'Black Luxury':
            X['name_Black SUV'] = 1
            

    elif name == 'Shared':
            X['name_UberPool'] = 1
            

    elif name == 'Normal':
            X['name_UberX'] = 1  
            

    elif name == 'Large':
            X['name_UberXL'] = 1 
            

    elif name == 'WAV':
            X['name_WAV'] = 1
            
    #elif name == 'Large Luxury':
             #X.loc[:,['name_Black SUV', 'name_UberPool', 'name_UberX','name_UberXL', 'name_WAV']] = None 
    
    else :
         X.loc[:,['name_Black SUV', 'name_UberPool', 'name_UberX','name_UberXL', 'name_WAV']] = 0 

    return X

def give_name_lyft(X, name):

    if name == 'Black Luxury':
            X['name_Lux Black'] = 1

    elif name == 'Shared':
            X['name_Shared'] =1

    elif name == 'Normal':
            X['name_Lyft'] = 1

    elif name == 'Large':
            X['name_Lyft XL'] = 1
            
    elif name == 'Large Luxury': 
            X['name_Lux Black XL'] = 1
            
    #elif name == 'WAV':
          # X.loc[:,['name_Lux Black', 'name_Lux Black XL','name_Lyft', 'name_Lyft XL', 'name_Shared']] = None
            
    else :
         X.loc[:,['name_Lux Black', 'name_Lux Black XL','name_Lyft', 'name_Lyft XL', 'name_Shared']] = 0


    return X




def final_input_uber(X, distance, temp,cloud_cover, pressure, rain, humidity,wind,day,source,hour,name):
        
    X['distance'] = distance
    X['temp/f'] = temp
    X['cloud cover'] = cloud_cover
    X['pressure'] = pressure
    X['rain'] = rain
    X['humidity'] = humidity
    X['wind'] = wind
    give_day(X,day)
    give_hour(X,hour)
    give_source(X,source)
    give_name_uber(X,name)

    return X

def final_input_lyft(X, distance, temp,cloud_cover, pressure, rain, humidity,wind,day,source,hour,name):
        
    X['distance'] = distance
    X['temp/f'] = temp
    X['cloud cover'] = cloud_cover
    X['pressure'] = pressure
    X['rain'] = rain
    X['humidity'] = humidity
    X['wind'] = wind
    give_day(X,day)
    give_hour(X,hour)
    give_source(X,source)
    give_name_lyft(X,name)

    return X

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    
    '''
    For rendering results on HTML GUI
    '''
    
    #Getting the coordinates of both the start and end location
    
    o_lat = request.form['source'] + ",Boston, MA, USA"
    o_lon = request.form['source']+ ",Boston, MA, USA"
    
    origin_lat = get_coord_lat(o_lat)
    origin_lon = get_coord_lon(o_lon)
    
    
    d_lat = request.form['destination']+ ",Boston, MA, USA"
    d_lon = request.form['destination']+ ",Boston, MA, USA"
    
    destination_lat = get_coord_lat(d_lat)
    destination_lon = get_coord_lon(d_lon)
    
    #distance calculator

    google_api_key = ''
    google_dist = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+origin_lat+','+origin_lon +'&destinations='+destination_lat+','+destination_lon+'&key='+google_api_key)
    json_google_object = google_dist.json()
    
    
    #Attaining the weather data at the starting point of the journey
    
    lat = origin_lat
    lon = origin_lon
    key = ''
    r = requests.get('https://api.darksky.net/forecast/'+key+'/'+lat+','+lon)
    json_object = r.json()
    
    
    google_distance = json_google_object['rows'][0]['elements'][0]['distance']['text']
    #str_distance = google_distance.replace('mi', '')
    #print('google_distance: [{}]'.format(google_distance))
    str_distance = re.sub(r'((mi)|(ft))', '',google_distance).strip()
    #print('str_distance: [{}]'.format(str_distance))
    distance = float(str_distance)
    name = request.form['type']        
    temp = json_object['currently']['temperature']
    cloud_cover =  json_object['currently']['cloudCover']
    pressure =  json_object['currently']['pressure']
    rain =  json_object['currently']['precipProbability']
    humidity = json_object['currently']['humidity']
    wind = json_object['currently']['windSpeed']
    source = request.form['source']
    timing_series = pd.Series(json_object['currently']['time'])
    timing_series[0] = pd.to_datetime(timing_series[0],unit ='s')
    timing_eastern = timing_series.dt.tz_localize('utc').dt.tz_convert('US/Eastern')
    timing_series_1 = pd.Series(timing_eastern)
    hour_1 = timing_series_1.dt.hour
    day_1 = timing_series_1.dt.day_name()
    day = day_1[0]
    hour = hour_1[0]
    final_time = timing_series_1[0]
    


    uber_final_features = final_input_uber(uber,distance,temp,cloud_cover, pressure, rain, humidity,wind,day,source,hour,name)
    
    lyft_final_features = final_input_lyft(lyft,distance,temp,cloud_cover, pressure, rain, humidity,wind,day,source,hour,name)
    
    uber_features = np.array(uber_final_features.iloc[0,:]).reshape(1,-1)
    
    lyft_features = np.array(lyft_final_features.iloc[0,:]).reshape(1,-1)
    
    uber_prediction = uber_model.predict(uber_features)
    
    lyft_prediction = lyft_model.predict(lyft_features)

    uber_output = round(uber_prediction[0],2)
    
    lyft_output = round(lyft_prediction[0],2)
    
    distance_output = round(distance,2)
    
    source_output = request.form['source']
    
    destination_output = request.form['destination']
    
    car_type = request.form['type']
    
    def suggest(uber_output, lyft_output):
        if uber_output < lyft_output:
            return('We suggest you take an Uber!')
        
        else:
            return('We suggest you take a Lyft!')
    

    return render_template('predict.html', journey_text = 'The journey from {} to {} in a {} vehicle.'.format(source_output,destination_output,car_type), 
                           prediction_text='The price of your Uber ride is $ {}'.format(uber_output) , 
                           prediction_text_1 = 'The price of your Lyft ride is $ {}'.format(lyft_output), 
                           distance_text = 'The distance we are talking about is {} miles.'.format(distance_output),
                          suggestion_text = suggest(uber_output, lyft_output))

    
    print(lyft_prediction)
    print(uber_prediction)


if __name__ == "__main__":
    app.run(debug=True, port =5050)
    
    
