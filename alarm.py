import time
import psutil
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("alert.wav")

while True:
	battery = psutil.sensors_battery()
	percent = battery.percent
	# print(type(percent))
	
	if percent > 80 or percent < 20:
		play_obj = wave_obj.play()
		play_obj.wait_done()		
	time.sleep(666)
