'use strict';

// const file = "audios/voyager1.mp3";
//const file = "audios/ansiedade.mp4";
const file = "circle";
var surfer, canvas;

// Init & load audio file
document.addEventListener('DOMContentLoaded', function() {
	surfer = new SoundController();
	surfer.Load(file);
//	surfer.LoadAndExamine(file);
	canvas = new ImageController();
	canvas.Load(file);
});

function playPause() {
	surfer.TogglePlay();
}
function speed(s) {
	if(s == '+') return surfer.Faster();
	if(s == '-') return surfer.Slower();
	return surfer.SetSpeed(s);
}

