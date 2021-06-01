"use strict";

class ImageController {

	constructor() {
		this.canvas = document.getElementById("voyager-img");
		this.context = this.canvas.getContext('2d');
		this.arr;
		this.width = 512;
		this.height = 384;
		this.pixelSize = 2;

		this.fileName;
		this.files;
		this.pixelsMs;

		this.Initialize();
	}

	Initialize() {
	}

	SetStartAndEnd(start, end) {
		return this;
	}

	AjaxJson(filename) {
		return new Promise((resolve, reject) => {
			$.ajax({
				url: filename + '.json',
				dataType: "json",
				mimeType: "textPlain"
			}).done( (data) => {
				resolve(data);
			});
		});
	}

	Load(file) {
		const json = 'peaks/img-' + file;
		this.fileName = json;
		this.AjaxJson(json)
			.then((data) => {
				console.info('got ', data);
				this.files = data.files;
				this.pixelsMs = data.px_per_ms;
				this.PrintFile(1);
			});
	}

	testPrint() {
		this.PrintPixelAt(0, 4, 4);
	}

	PrintFile(n) {
		this.AjaxJson(this.fileName + '-' + n)
			.then(data => {
				this.arr = data.data;
				console.info(this.arr);
				this.PrintItAll();
			});
	}

	PrintItAll() {
		console.info(this.arr);
		let w, h = 0;
		this.arr.map((data, i) => {
			w = Math.floor(i / this.height);
			h = i - (w * this.height); 
			console.info(`printing ${data} on h${h}w${w}`);
			this.PrintPixelAt(data, h, w);
		});
	}

	GetColor(color) {
		return `rgb(${color}, ${color}, ${color})`;
	}

	PrintPixelAt(color, h, w) {
		color = this.GetColor(color);
		this.context.fillStyle = color;
		this.context.fillRect(w, h, this.pixelSize, this.pixelSize);
	}

}
