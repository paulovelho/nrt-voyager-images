import sys
import json
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from pprint import pprint


def scale_data(arr, max_val):
	digits = 4
	new_data = [];
	for x in arr:
		val = round(x / max_val, digits);
		new_data.append(float(val));
	return new_data;

def parse_data(filename, peak, valley, fix):
	data = [];
	times = [];
	with open('data/' + filename + '.txt', "r") as file:
		for line in file:
			c = line.split('\t')
			times.append( int(c[0]) )
			data.append( int(c[1].rstrip("\n")) )

	wave_start = 0;
	wave_sizes = [];
	wave_arr = [];
	arr = [];

	for i in range(len(data)):
		d = data[i];
		if(wave_start == 0):
			if(d < valley):
				wave_start = i;
				wave_arr = [];
			else:
				continue;
		else:
			val = normalizeColor(d, peak, valley);
			wave_arr.append(d);
			if(d > peak):
				print('wave ending at {} with {} points'.format(i, len(wave_arr)));
				wave_start = 0;
				if(fix > 0):
					if(len(wave_arr) > fix): continue;
				wave_sizes.append(len(wave_arr))
				arr.append(wave_arr);
				arr.append(wave_arr);
				arr.append(wave_arr);

	# delete problematic nodes
#	del(arr[0]);
#	del(arr[len(arr)]);
	max_len = np.max([len(a) for a in arr])
	arr = np.asarray([np.pad(a, (0, max_len - len(a)), 'constant', constant_values=0) for a in arr])

	data = np.array(arr)

	pprint(data);

	plot_image(data);

def normalizeColor(c, peak, valley):
	c = c - valley;
	return c/peak;

def plot_image(data):
	data = data.transpose();

	print('plotting {} points'.format(len(data)))

#	data = np.split(np.array(data), 512)
#	pprint(data)
	plt.imshow(data, vmin = 0, vmax = 256, interpolation ='nearest')
	plt.show()


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print('Missing information to work with')
		print('Usage: python voyager.py [file name (inside ./data)] [peaks] [valleys]')
		exit()
	filename = sys.argv[1];
	try:
		peaks = sys.argv[2];
		valleys = sys.argv[3];
	except IndexError:
		print('Index Error!');

	try:
		calibration_fix = sys.argv[4];
	except IndexError:
		calibration_fix = 0;

	parse_data(filename, float(peaks), float(valleys), float(calibration_fix));

