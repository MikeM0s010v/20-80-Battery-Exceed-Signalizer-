import time
import psutil
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("alert.wav")

while True:
	battery = psutil.sensors_battery()
	percent = battery.percent
	plugged = battery.power_plugged
	# print(type(percent))
	# time.sleep(600)
	if percent > 80: # or percent < 20
		play_obj = wave_obj.play()
		play_obj.wait_done()		
		# play_obj.wait_done()
		time.sleep(180)
		if plugged:
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(180)
		else:	
	        	time.sleep(3600)
	elif percent < 20:
		play_obj = wave_obj.play()
		play_obj.wait_done()
		time.sleep(180)
		if plugged:
			time.sleep(1800)
		else:
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(180)

