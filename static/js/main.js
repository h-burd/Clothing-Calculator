var tempRng = document.getElementById('tempRng')
var tempLabel = document.getElementById('tempLabel')

var windRng = document.getElementById('windRng')
var windLabel = document.getElementById('windLabel')

tempRng.onchange = function changeVal(){
    tempLabel.innerHTML = tempRng.value + "°F";
}

windRng.onchange = function changeVal(){
    windLabel.innerHTML = windRng.value + " mph";
}