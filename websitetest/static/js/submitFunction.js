
function submitFunction() {
    var _getlyrics =    document.getElementById("submitlyric").value;
   
   

    var 

var xhr = new XMLHttpRequest();
xhr.open("POST", 'http://127.0.0.1:5000/_getlyrics', true);
xhr.setRequestHeader('Content-Type', 'application/json');
response=xhr.send(JSON.stringify({
    value: _getlyrics
}))};




