import time
import psutil
import simpleaudio as sa

# creating sound object
wave_obj = sa.WaveObject.from_wave_file("alert.wav")

# function to reproduce sound
def make_noice(sound_file):
	play_obj = wave_obj.play()
	play_obj.wait_done()
	
# creating multiconditional loop 
while True:
	battery = psutil.sensors_battery()
	percent = battery.percent
	plugged = battery.power_plugged
	# print(type(percent))
	# time.sleep(600)
	if percent > 80: # or percent < 20
		make_noice(wave_obj)		
		# play_obj.wait_done()
		time.sleep(180)
		if plugged:
			make_noice(wave_obj)
			time.sleep(180)
		else:	
	        	time.sleep(3600)
	elif percent < 20:
		make_noice(wave_obj)
		time.sleep(180)
		if plugged:
			time.sleep(1800)
		else:
			make_noice(wave_obj)
			time.sleep(180)

