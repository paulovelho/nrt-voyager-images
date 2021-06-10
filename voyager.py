import sys
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

def parse_data(filename, peak):
	data = [];
	times = [];
	with open('data/' + filename + '.txt', "r") as file:
		for line in file:
			c = line.split('\t')
			times.append( int(c[0]) )
			data.append( int(c[1].rstrip("\n")) )

	wave_sizes = [];
	wave_arr = [];
	arr = [];

	valley = np.min(data);

	for i in range(len(data)):
		d = data[i];
		if( d > peak ):
			if( len(wave_arr) > 100 ):
				print('wave ending at {} with {} points'.format(i, len(wave_arr)));
				wave_sizes.append(len(wave_arr))
				arr.append(wave_arr);
				arr.append(wave_arr);
			wave_arr = [];
		else:
			val = normalizeColor(d, peak, valley);
			wave_arr.append(val);

	del(arr[0]);

	max_len = np.max([len(a) for a in arr])
	arr = np.asarray([np.pad(a, (0, max_len - len(a)), 'constant', constant_values=0) for a in arr])

	data = np.array(arr)

	pprint(data);

	plot_image(data);

def normalizeColor(c, peak, valley):
	c = c - valley;
	c = c / peak * 100;
	return c;

def plot_image(data):
	data = data.transpose();

	print('plotting {} points'.format(len(data)))

	plt.imshow(data, vmin = 0, vmax = 256, interpolation ='nearest', cmap=colormap)
	plt.show()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Missing information to work with')
		print('Usage: python voyager.py [file name (inside ./data)] [peaks] [color]')
		exit()
	filename = sys.argv[1];
	try:
		peaks = sys.argv[2];
	except IndexError:
		print('Index Error!');



################### AVAILABLE CMAPS:
# cmap='RdBu_r'
# cmap='Greys'
# https://matplotlib.org/stable/gallery/color/colormap_reference.html
	try:
		colormap = sys.argv[3];
	except IndexError:
		colormap = 'Greys';

	parse_data(filename, float(peaks));

