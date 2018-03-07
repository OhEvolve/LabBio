
(function($) {
    $(function() {
        var selectField = $('#id_date_range'),
            verified = $('.AAAAAA');

        function toggleVerified(value) {
            if (value === 'Custom') {
                verified.show();
            } else {
                verified.hide();
            }
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });
    });
})(django.jQuery);
