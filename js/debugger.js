
function debug(str, data) {
	console.info(str, data);
	doLog(str);
}

function doLog(data) {
	console.info("log: ", data);
	let logScr = $("#log");
	logScr.append(">> " + data + "<br/>");
}

function startLog(title) {
	let logScr = $("#log");
	logScr.append("==============[" + title + "]==============><br/>");	
}

function endLog() {
	let logScr = $("#log");
	if(logScr.length == 0) return;
	logScr.append("___________________________________________________________<br/><br/>");
	logScr.scrollTop(logScr[0].scrollHeight);
}
