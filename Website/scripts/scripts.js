// make requests when button is clicked

// get the button
var buttonAll = document.getElementById("btnAll");

// add event listener

buttonAll.addEventListener("click", function() {
    // get http://localhost:8000/company/all/report

    // response includes a file as binary data

    // create a new XMLHttpRequest object

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://localhost:8000/company/all/report", true);
    xhr.responseType = "blob";

    xhr.onload = function() {
        if (xhr.status === 200) {
            // create a new blob object
            var blob = new Blob([xhr.response], { type: "application/pdf" });

            // create a new link element
            var link = document.createElement("a");

            // set the href and download attributes
            link.href = window.URL.createObjectURL(blob);
            link.download = "report.pdf";

            // append the link to the document
            document.body.appendChild(link);

            // dispatch a click event on the link
            link.click();

            // remove the link from the document
            document.body.removeChild(link);
        }
    };

    xhr.send();

});
