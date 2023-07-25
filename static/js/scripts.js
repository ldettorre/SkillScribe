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

    showCategorySelectElement();

    $(window).resize(function() {
        console.log("Changing width detected...")
        showCategorySelectElement();
    });

    $('#dropdown-selection').change(function() {
        var selection = $(this).val(); 
        var selectedCategory = document.getElementById(selection);
        selectedCategory.scrollIntoView();         
    });
});