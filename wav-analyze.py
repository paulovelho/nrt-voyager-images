import sys
import math
import statistics
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


def imbfix(data):
	number_of_scans = 512;
	offset = 0;
	scan_line_width = 3197;
	image_data = [];

	for scan in range(number_of_scans):
		chunk = [_m for _m in data[int(offset):int(offset) + scan_line_width]]
		if len(chunk) != scan_line_width:
			chunk = np.zeros(scan_line_width)
			offset_exceeded = True
		image_data.append(chunk)
		offset += scan_line_width

	return image_data;


def open_wav(file, time, start, end):
	sampleRate, data = wavfile.read('./wav/' + file + '.wav', 'r')

	duration = len(data)/sampleRate
	time_plot = np.arange(0,duration,1/sampleRate)
	print('given duration: {} | estimated duration: {}'.format(time, duration));
	print('available points: {}/{}'.format(len(time_plot), len(data)))

	plot_wave(data);
	final_data = save_data(file, data, time_plot, start, end);


def save_data(file, data, times, start, end):
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

	file_content = '\n'.join(arr);
	file_name = './data/' + file + '.txt';
	print('saving {} points on {}.'.format(len(arr), file_name))
	with open(file_name, "w") as f:
		f.write(file_content);

	return arr_int;

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
