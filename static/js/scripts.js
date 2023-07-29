$(document).ready(function() {
    function showCategorySelectElement() {
        if ($(window).width() <= 768) {
            document.getElementById('category-column').hidden = true
            document.getElementById('category-dropdown').hidden = false
        }
        else{
            document.getElementById('category-column').hidden = false
            document.getElementById('category-dropdown').hidden = true
            
        }
    }  

    $('#dropdown-selection').change(function() {
        var selection = $(this).val(); 
        var selectedCategory = document.getElementById(selection);
        selectedCategory.scrollIntoView();         
    });

    $("#id_situation").on("input", function(){
        var situationInput = document.getElementById('id_situation');
        var situationLimit = document.getElementById('situation-limit');
        var inputLength = situationInput.value.length;
        situationLimit.innerHTML = inputLength;  
    });

    showCategorySelectElement();

    $(window).resize(function() {
        showCategorySelectElement();
    });

    
});