"use strict";

class ImageController {

	constructor() {
		this.canvas = document.getElementById("voyager-img");
		this.arrDimension = 0;
		this.width = 512;
		this.height = 0;
		this.Initialize();
	}

	Initialize() {
	}

	SetArrDimension(size) {
		this.arrDimension = size;
		this.height = this.arrDimension / 2;
	}

}
