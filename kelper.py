C = 1 / 100
earthRadius = 6378
distance = 35786 + earthRadius

period = C * (distance ** 1.5)
print(str(round(period)) + "s")
print(str(round(period/60/60)) + "hrs")