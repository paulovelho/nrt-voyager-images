"use strict";

class SoundController {

	constructor() {
		this.wavesurfer = null;
		this.container = document.querySelector('#waveform');
		this.speed = 1;
		this.Initialize();
	}

	Initialize() {
		this.wavesurfer = WaveSurfer.create({
				container: this.container,
				waveColor: '#F00',
				progressColor: '#000',
				scrollParent: true,
		});

		let slider = document.querySelector('[data-action="zoom"]');
		slider.max = 9000;
		slider.min = this.wavesurfer.params.minPxPerSec;
		slider.value = slider.max;
		slider.addEventListener('input', (evt) => {
			const value = evt.target.value;
			debug('setting zoom to ' + value);
			this.wavesurfer.zoom(Number(value));
		});
		this.wavesurfer.zoom(slider.value);
		this.SetSpeed(0.5);


		this.wavesurfer.setHeight(200);
	}

	OnProgress(t) {
	}

	LoadWithPeaks(audio, peaks) {
		return new Promise((resolve, reject) => {
			this.wavesurfer.load(audio, peaks);
			console.info(this.wavesurfer);
			this.wavesurfer.on('audioprocess', (t) => this.OnProgress(t));
			this.wavesurfer.on('error', (e) => {
				console.error(e);
				reject();
			});
			this.wavesurfer.on('ready', resolve);
			resolve();
		});
	}

	LoadAndExamine(file) {
		const audio = 'audios/' + file + '.mp3';
		return new Promise((resolve, reject) => {
			this.wavesurfer.load(audio);
			this.wavesurfer.on('ready', () => {
				console.info(this.wavesurfer);
				resolve();
			});

			this.wavesurfer.on('error', (e) => {
				console.error(e);
				reject();
			});
		});
	}

	Load(file) {
		const json = 'peaks/' + file + '.json';
		const audio = 'audios/' + file + '.mp3';

		return new Promise((resolve, reject) => {
			fetch(json)
				.then(response => {
					if (!response.ok) { reject("HTTP error " + response.status); }
					return response.json();
				})
				.then(peaks => {
					this.LoadWithPeaks(audio, peaks.data)
						.then(resolve).catch(reject);
				})
				.catch((e) => { reject(e); });
		});
	}

	TogglePlay() {
		this.wavesurfer.playPause();
	}

	UpdateSpeed() {
		this.speed = this.speed.toFixed(2);
		debug("speed at " + this.speed);
		this.wavesurfer.setPlaybackRate(this.speed);
	}
	SetSpeed(s) {
		this.speed = s;
		this.UpdateSpeed();
	}
	GetSpeed() {
		return this.speed;
	}
	Faster() {
		this.speed = +this.speed + 0.1;
		if(this.speed > 1) this.speed = 1;
		this.UpdateSpeed();
	}
	Slower() {
		this.speed -= 0.1;
		if(this.speed <= 0) this.speed = 0.10;
		this.UpdateSpeed();
	}

}
