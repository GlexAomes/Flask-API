API = 'http://127.0.0.1:5000/'; //change accordingly if not testing

/*
Basic function that will do some error checking and call our
API to update an element with the result.
*/
function call_API(endpoint) {
    value = document.getElementById(endpoint + "-num").value
    var num = parseInt(value);

    if (!num) {
        document.getElementById(endpoint + '-result').innerHTML = "\"" + value + "\" is not a number.";
        document.getElementById(endpoint + '-result').removeAttribute('hidden');
        return;
    }

    //Need to do error checking for num before calling API
    //Forced to do so anyway after allowing CORS, which for some reason disabled catch_all_404s

    if (num < 0) {
        document.getElementById(endpoint + '-result').innerHTML = value + " is < 0.";
        document.getElementById(endpoint + '-result').removeAttribute('hidden');
        return;
    }

    //But I will not error check for > 951 because witty joke.
    //It will however, tell console about status 500.

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        var response = this.responseText;
        if (!response) {
            return;
        }
        var json = JSON.parse(response)
        result = undefined
        if (json.result) {
            result = json.result;
        } else {
            result = json.message;
        }
        document.getElementById(endpoint + '-result').innerHTML = "Result: " + result;
        document.getElementById(endpoint + '-result').removeAttribute('hidden');
    };
    xhttp.open("GET", API + endpoint + '/' + num, true);
    xhttp.send();
}