import sys
import json
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from pprint import pprint


def plot(data):
#	nrows, ncols = 768, 1024
#	data = data.reshape((nrows, ncols))

	print('plotting {} points'.format(len(data)))

#	data = np.split(np.array(data), 512)
#	pprint(data)
	plt.imshow(data, vmin = 0, vmax = 256, interpolation ='nearest')
	plt.show()







def fix_json(filename, time, start, end):
	times = []
	data = []
	with open('data/' + filename, "r") as file:
		for line in file:
			c = line.split('\t')
			times.append( float(c[0]) )
			data.append( float(c[1].rstrip("\n")) )

	data = scale_data(data)
	soundFile([i for i in data], time, start, end)
	imageFile(data, times, time, start, end)

def scale_data(arr):
	print('scaling wave')
	digits = 4
	max_val = float(max(arr))
	new_data = []
	for x in arr:
		new_data.append(round(x / max_val, digits))

	return new_data

def soundFile(arr, time, start, end):
	json_content = {}
	json_content["time"] = time
	json_content["scale"] = len(arr) / time
	json_content["img_start"] = start
	json_content["img_end"] = end
	# we don't need a too much detailed array to show
	del arr[::2]
	del arr[::2]
	json_content["data"] = arr
	json_content["points"] = len(arr)

	file_content = json.dumps(json_content, separators=(',', ':'))

	name = 'peaks/' + filename.split('.')[0] + '.json'
	print('\n------------------------------------') 
	print('-- generating wavesurfer file: ' + name + ' --')
	print('------------------------------------\n') 

	with open(name, "w") as f:
		f.write(file_content)

def imageFile(data, times, time, start, end):
	arr = [];
	valid_time = end - start;
	wave_length = 9;

	print('analyzing data from wave of {}, starting at {} and ending at {}'.format(time, start, end))

	wave_start = 0;
	wave_end = end;
	wave_arr = [];
	waves = 0;

	wave_size = [];

	print('times: {} '.format(len(times)))

	for i in range(len(times)):
		t = int(times[i]*1000)
		if(t <= start): continue
		if(t > end): continue

		if(wave_start == 0):
			wave_start = int(t);
			wave_end = t + wave_length;
			if(wave_end > end): continue
			wave_arr = [];
			print('wave starting at {}; will end at {}'.format(t, wave_end));

		d = normalizeColor(data[i])
		wave_arr.append(d);
		if(t == wave_end):
			print('wave ending at {} with {} points'.format(t, len(wave_arr)));
			wave_size.append(len(wave_arr))
			wave_start = 0;
			arr.append(wave_arr);
			waves = waves + 1;

	wave_avg = math.floor( sum(wave_size) / len(wave_size) )
	max_wave = np.max([len(a) for a in arr])


	print('had {} waves with an average of {} and maximum of {}'.format(waves, wave_avg, max_wave))
	plot(arr)


def normalizeColor(c):
	# color = between(-1 and 1)
	c = c + 1; # color = between(0 and 2)
	return int(round((256 * c) / 2))

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print('Missing information to work with')
		print('Usage: python fix-json.py [file name (inside ./data)] [time] [start] [end]')
		exit()
	filename = sys.argv[1]
	time = sys.argv[2]
	try:
		start = sys.argv[3]
	except IndexError:
		start = 0
	try:
		end = sys.argv[4]
	except IndexError:
		end = time

	fix_json(filename, int(time), int(start), int(end))

