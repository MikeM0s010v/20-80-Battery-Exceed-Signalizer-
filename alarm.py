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
	if percent > 80:
		if plugged == False:
			pass
		else:
			make_noice(wave_obj)
			time.sleep(20)		
		
	elif percent < 20:
		if plugged:
			pass
		else:
			make_noice(wave_obj)
			time.sleep(20)
