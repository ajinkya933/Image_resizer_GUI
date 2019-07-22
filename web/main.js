function generateQRCode() {
	// Get data input from the server
	var data = document.getElementById("data").value
	// 
	eel.dummy(data)(function(ret) {console.log(ret)})
	//eel.dummy("this is eel")(function(ret) {console.log(ret)})
}

function setImage(base64) {
	document.getElementById("qr").src = base64
}
