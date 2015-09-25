from math import sin, cos, asin, radians, sqrt

# Implementing the haversine formula
def distance(point1, point2):

  lat1 = point1[0]
  lon1 = point1[1]
  
  lat2 = point2[0]
  lon2 = point2[1]

  lon1, lon2, lat1, lat2 = map(radians, [lon1, lon2, lat1, lat2])

  longitude_dist = lon2 - lon1
  latitude_dist = lat2 -lat1
  
  # Haversine formula
  a = sin(longitude_dist/2)**2 + cos(lat1) * cos(lat2) * sin(longitude_dist/2)**2
  c = 2 * asin(sqrt(a)) 
  r = 3956 # Earth's radius in miles
  return c * r

def detour(A,B,C,D):

  #Is ACDB shorter or is CABD?

  #ACDB:
  # A-->C + C-->D + D-->B
  ACDB = distance(A,C) + distance(C,D) + distance(D,B)

  #CABD
  # C-->A + A-->B + B-->D
  CABD = distance(C,A) + distance(A,B) + distance(B,D)

  if ACDB < CABD:
    shorter_dist = "ACDB"
  else:
    shorter_dist = "CABD"

  print("The total detour distance for ACDB detour is = " + str(ACDB))
  print("The total detour distance for CABD detour is = " + str(CABD))
  print("The shorter detour is the " + shorter_dist + " route.")

def main():
  #[latitude, longitude]
  A = [32,-76]
  B = [33,-75]
  C = [34,-74]
  D = [35,-73]

  detour(A,B,C,D)

main()