from w1thermsensor import W1ThermSensor


sensor = W1ThermSensor()
water_temperature = sensor.get_temperature()
print("water-temperature:{0:.3f}".format(water_temperature))