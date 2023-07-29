$(document).ready(function() {
// Here I get the textarea which received input 
    // and dynamically update the relevant counter.
    var addEntryForm = document.getElementById("add-entry-form");
    addEntryForm.addEventListener("input", function(event){
        var fieldInputted = event.target.id;
        var chosenInput = document.getElementById(fieldInputted.toString());
        var inputLimit = fieldInputted.toString().substring(3)+"-limit";
        var inputLimitSpan = document.getElementById(inputLimit); 
        
        var inputLength = chosenInput.value.length;
        inputLimitSpan.innerHTML = inputLength;
    });
});