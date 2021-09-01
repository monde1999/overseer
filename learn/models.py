from django.db import models
import math

class Location:
  def __init__(self, latitude,longitude):
    self.latitude = latitude
    self.longitude = longitude

def getDistance(location1,location2):
  lat1Rad = location1.latitude * math.pi / 180
  lat2Rad = location2.latitude * math.pi / 180
  R = 6371e3
  latDiffRad = (location2.latitude - location1.latitude) * math.pi /180
  lonDiffRad = (location2.longitude - location1.longitude) * math.pi / 180
  a = math.sin(latDiffRad/2)**2 + math.cos(lat1Rad) * math.cos(lat2Rad) * math.sin(lonDiffRad/2)**2
  c = 2 * math.atan2(a**0.5, (1-a)**0.5)
  return R * c

class Monitor:
    def __init__(self, location):
      self.latitude = location.latitude
      self.longitude = location.longitude
      self.square_radius = 10 # default
      self.user_locations_current={}
      self.user_locations_previous={}
      self.user_locations_next={}
    
    def refreshMonitor():
      self.user_locations_previous = self.user_locations_current
      self.user_locations_current = self.user_locations_next
      self.user_locations_next = {}
    
    def addLocation(user_id,location):
      self.user_locations_next[user_id] = location
    
    def isThereATraffic():
      vehicle_count = 0
      moving_count = 0
      distance_threshold = 3 # to be changed
      movement_threshold = .7
      # for all elements in current_locs
      # if same user id exists in previous, increment vehicle count, get distance
      # if distance > threshold increment moving_count
      # return moving_count / vehicle_count >= .7 

      for k, v in self.user_locations_current.items():
        prev_location = self.user_locations_previous.get(k)
        if prev_location:
          vehicle_count+=1
          if getDistance(prev_location, v) >= distance_threshold:
            moving_count+=1
      return moving_count / vehicle_count >= movement_threshold
    
    def getDistance(location1,location2):
      lat1Rad = location1.latitude * math.pi / 180
      lat2Rad = location2.latitude * math.pi / 180
      R = 6371e3
      latDiffRad = (location2.latitude - location1.latitude) * math.pi /180
      lonDiffRad = (location2.longitude - location1.longitude) * math.pi / 180
      a = math.sin(latDiffRad/2)**2 + math.cos(lat1Rad) * math.cos(lat2Rad) * math.sin(lonDiffRad/2)**2
      c = 2 * math.atan2(a**0.5, (1-a)**0.5)
      return R * c

class BehaviorAnalyzer:
    def start(self):  # async
        print('ba has started...')