(function(context) {
    
    
    
})(DMP_CONTEXT.get());

jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
})