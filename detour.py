from math import sin, cos, asin, radians, sqrt

# Implementing the haversine formula
def distance(point1, point2):

  lat1 = point1[0]
  lon1 = point1[1]
  
  lat2 = point2[0]
  lon2 = point2[1]

  lon1, lon2, lat1, lat2 = map(radians, [lon1, lon2, lat1, lat2])

  longitudeDist = lon2 - lon1
  latitudeDist = lat2 -lat1
  
  # Haversine formula
  a = sin(longitudeDist/2)**2 + cos(lat1) * cos(lat2) * sin(longitudeDist/2)**2
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
    shorterDist = "ACDB"
  else:
    shorterDist = "CABD"

  print("The total detour distance for ACDB detour is = " + str(ACDB))
  print("The total detour distance for CABD detour is = " + str(CABD))
  print("The shorter detour is the " + shorterDist + " route.")

def main():
  #[latitude, longitude]
  A = [32,-76]
  B = [33,-75]
  C = [34,-74]
  D = [35,-73]

  detour(A,B,C,D)

main()