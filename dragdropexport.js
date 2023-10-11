function allowDrop(ev) {
  ev.preventDefault();
}

function dragStart(ev) {
  console.log("Start Drag")
  console.log(ev);
  ev.dataTransfer.setData("text", ev.target.id);
  console.log(ev.target.id);
}

function dragDrop(ev) {
    console.log("Drag drop")
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  console.log(data)
  // ev.target.appendChild(document.getElementById(data));
  console.log(document.getElementById(data));
  ev.currentTarget.appendChild(document.getElementById(data));
}

function exportDataEmail(){
let cells = document.getElementsByClassName('pyramidbox');
console.log(cells.length)

let participant = document.getElementById("id").value;

let row0 = ["box", "imageName"];
let rows =[];
rows.push(row0);

for (var i = 0; i < cells.length; i++) {
  for(var j = 1; j<cells[i].childNodes.length; j++){
    let filename = cells[i].childNodes[j].src.split("/");
      console.log(filename)
    let row = [i+1, filename[filename.length-1]];
    console.log(row)
    rows.push(row);
  }
  }

let csvContent = "data:text/csv;charset=utf-8,";

rows.forEach(function(rowArray) {
    let line = rowArray.join(",");
    csvContent += line + "\r\n";
});

var encodedUri = encodeURI(csvContent);
var link = document.createElement("a");
var ref = "mailto:ninalutz@uw.edu" + "?subject=CSV&body=" + csvContent;
link.setAttribute("href", ref);
document.body.appendChild(link); // Required for FF
link.click();

exportData();

}

function exportVideoData(){
    let cells = document.getElementsByClassName('pyramidbox');

    let participant = document.getElementById("id").value;

    let row0 = ["box", "videoName"];
    let rows =[];
    rows.push(row0);

    for (var i = 0; i < cells.length; i++) {
      for(var j = 1; j<cells[i].childNodes.length; j++){
        console.log(cells[i].childNodes[j].id.split("drag")[1]);
        let row = [i+1, cells[i].childNodes[j].id.split("drag")[1]];
        rows.push(row);
      }
      }

    let csvContent = "data:text/csv;charset=utf-8,";

    rows.forEach(function(rowArray) {
        let line = rowArray.join(",");
        csvContent += line + "\r\n";
    });

    var encodedUri = encodeURI(csvContent);
    var link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", participant+".csv");
    document.body.appendChild(link); // Required for FF

    link.click(); // This will download the data file named "my_data.csv".
}   

function exportData(){
    let cells = document.getElementsByClassName('pyramidbox');
    console.log(cells.length)

    let participant = document.getElementById("id").value;

    let row0 = ["box", "imageName"];
    let rows =[];
    rows.push(row0);

    for (var i = 0; i < cells.length; i++) {
      for(var j = 1; j<cells[i].childNodes.length; j++){
        let filename = cells[i].childNodes[j].src.split("/");
          console.log(filename)
        let row = [i+1, filename[filename.length-1]];
        console.log(row)
        rows.push(row);
      }
      }

    let csvContent = "data:text/csv;charset=utf-8,";

    rows.forEach(function(rowArray) {
        let line = rowArray.join(",");
        csvContent += line + "\r\n";
    });

    var encodedUri = encodeURI(csvContent);
    var link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", participant+".csv");
    document.body.appendChild(link); // Required for FF

    link.click(); // This will download the data file named "my_data.csv".
}   