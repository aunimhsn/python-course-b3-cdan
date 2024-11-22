
KMH_TO_MPH = 1.609

speed_kmh = float(input("Veuillez entrer une vitesse en km/h : ")) 
speed_mph = speed_kmh / KMH_TO_MPH

print(f'{speed_kmh} km/h = {speed_mph:.2f} mph')