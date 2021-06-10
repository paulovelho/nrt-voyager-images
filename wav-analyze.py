import sys
import math
import numpy as np
import matplotlib.pyplot as plt

from pprint import pprint
from scipy.io import wavfile


def plot_wave(data, time=[]):
	if(len(time) > 0):
		plt.plot(time, data);
	else:
		plt.plot(data);
	plt.title('analyzing file {}.wav'.format(filename));
	plt.show();


def open_wav(file, time, start, end):
	sampleRate, data = wavfile.read('./wav/' + file + '.wav', 'r')

#	pprint(data);
	duration = len(data)/sampleRate
	time_plot = np.arange(0,duration,1/sampleRate)
	print('given duration: {} | estimated duration: {}'.format(time, duration));
	print('available points: {}/{}'.format(len(time_plot), len(data)))

	try:
		data = data[:, 0];
	except IndexError:
		print('only one channel found');

	plot_wave(data);
	data = scale_data(data);
	final_data = filter_data(data, time_plot, start, end);
	save_data(file, final_data);

def scale_data(arr):
	digits = 4
	pprint(arr);
	max_val = float(max(arr))
	print('scaling wave | normalizing it to {}'.format(max_val));
	new_data = [];
	for x in arr:
		val = round(x / max_val, digits);
		new_data.append(int(val*10000));
	return new_data;

def filter_data(data, times, start, end):
	arr = [];
	arr_int = [];
	print('filtering points ... (this may take some time)')
	for i in range(len(times)):
		t = int(times[i] * 1000);
		if(t < start): continue;
		if(t > end): continue;
		d = data[i];
		arr_int.append(d);
		arr.append(str(t) + '\t' + str(d));
	plot_wave(arr_int);
	return arr;

def save_data(file, arr):
	file_content = '\n'.join(arr);
	file_name = './data/' + file + '.txt';
	print('saving {} points on {}.'.format(len(arr), file_name))
	with open(file_name, "w") as f:
		f.write(file_content);

if __name__ == '__main__':
	filename = sys.argv[1];
	if len(sys.argv) < 3:
		print('Missing information to work with')
		print('Usage: python fix-json.py [file name (inside ./wav)] [time] [start] [end]')
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

	open_wav(filename, time, int(start), int(end))

