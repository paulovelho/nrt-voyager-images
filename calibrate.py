import sys
import json
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from pprint import pprint


def plot_wave(wave):
	plt.plot(wave);
	plt.title('analyzing file {}.wav'.format(filename));
	plt.show();


def parse_data(filename, peak):
	data = [];
	times = [];
	with open('data/' + filename + '.txt', "r") as file:
		for line in file:
			c = line.split('\t')
			times.append( int(c[0]) )
			data.append( float(c[1].rstrip("\n")) )

	timestamp = '';
	wave_sizes = [];
	wave_times = [];
	wave_arr = [];
	arr = [];

	valley = np.min(data);

	for i in range(len(data)):
		d = data[i];
		t = times[i];
		if( d > peak ):
			if( len(wave_arr) > 100 ):
				timestamp = timestamp + '-' + str(t);
				wave_times.append(timestamp);
				print('wave {} goes from {} with {} points'.format(len(arr), timestamp, len(wave_arr)));
				print('wave ending at {} with {} points'.format(i, len(wave_arr)));
				wave_sizes.append(len(wave_arr))
				arr.append(wave_arr);
				arr.append(wave_arr);
			wave_arr = [];
			timestamp = ''
		else:
			wave_arr.append(d);

	del(arr[0]);

	wave_avg = math.floor( sum(wave_sizes) / len(wave_sizes) )
	max_len = np.max([len(a) for a in arr])
	print('had {} waves with an avg of {} points and a max of {}'.format(len(arr), wave_avg, max_len));

	arr = np.asarray([np.pad(a, (0, max_len - len(a)), 'constant', constant_values=0) for a in arr])
	print('after conversion, there are {} waves'.format(len(arr)));

	analyze(arr, wave_times);
#	plot_image(arr);


def analyze(data, times):

	print('wave 0 has {} points'.format(len(data[0])));

	max_wave = 0;
	max_wave_index = -1;
	for i in range(len(data)):
		wave = data[i];
		if(len(wave) > max_wave):
			max_wave = len(wave);
			max_wave_index = i;

	print('biggest wave is {}, at {}, with {}'.format(max_wave_index, times[max_wave_index], len(data[max_wave_index])))
	max_len = np.max([a for a in data[max_wave_index]])
	print('max = {} (peak: {})'.format(max_len, peaks));

	plot_wave(data[max_wave_index]);


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Missing information to work with')
		print('Usage: python voyager.py [file name (inside ./data)] [peaks] [valleys]')
		exit()
	filename = sys.argv[1]
	try:
		peaks = sys.argv[2]
	except IndexError:
		print('Index Error!');

	parse_data(filename, float(peaks))

