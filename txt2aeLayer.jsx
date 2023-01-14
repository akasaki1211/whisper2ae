// open subtitle txt file
var fileName = File.openDialog("Select subtitles txt file");
var fileObj = new File(fileName);

// get current selected layer
var selTxtLayer = false;
var selLayer = app.project.activeItem.selectedLayers;
if (selLayer != ""){
    selLayer = selLayer[0];
    selLayer.selected = false;
    if (selLayer instanceof TextLayer) {
        selTxtLayer = true;
    }
}

// open file
var data, txtLayer;
if (fileObj.open("r")){

	while(!fileObj.eof){
		data = fileObj.readln().split(/\t/);
        
        // duplicate or new create
        if (selTxtLayer) {
            txtLayer = selLayer.duplicate();
        } else {
            txtLayer = app.project.activeItem.layers.addText(data[2]);
        }

        // set text properties
        txtLayer.property("Source Text").setValue(data[2]);
        txtLayer.startTime = parseFloat(data[0]);
        txtLayer.outPoint = parseFloat(data[1]);
	}

	fileObj.close();
}