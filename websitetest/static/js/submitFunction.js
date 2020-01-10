function submitFunction() {
    var _getlyrics =    document.getElementById("submitLyric").value
d3.json('/_getlyrics')

var xhr = new XMLHttpRequest();
xhr.open("POST", '/_getlyrics', true);
xhr.setRequestHeader('Content-Type', 'application/json');
response=xhr.send(JSON.stringify({
    value: _getlyrics
}));

}


