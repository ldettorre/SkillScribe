$(document).ready(function() {
    
    // Commented out the category-dropdown related code as it is currently under
    // review for a better UI experience.
    function showCategorySelectElement() {
        if ($(window).width() <= 768) {
            document.getElementById('category-column').hidden = true
            // document.getElementById('category-dropdown').hidden = false
        }
        else{
            document.getElementById('category-column').hidden = false
        //     document.getElementById('category-dropdown').hidden = true
        }
    }  

    // $('#dropdown-selection').change(function() {
    //     var selection = $(this).val(); 
    //     var selectedCategory = document.getElementById(selection);
    //     selectedCategory.scrollIntoView();
    // });


    showCategorySelectElement();

    $(window).resize(function() {
        showCategorySelectElement();
    });

    
});