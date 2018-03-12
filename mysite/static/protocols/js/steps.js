
(function($) {
    $(function() {


        console.log("here");
        var selectField = $('#id_date_range'),
            verified = $('.AAAAAA');

        function toggleVerified(value) {
            if (value === 'Custom') {
                console.log("inside")
                verified.show();

            } else {
                verified.hide();
            }
        }
        
        console.log("is3")

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });

    });
})(django.jQuery);
