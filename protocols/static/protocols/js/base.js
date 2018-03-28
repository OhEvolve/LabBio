
(function($) {
    $(function() {

        var selectField = $('#id_IO_template'),

            input_id = $('#input_set-group');
            output_id = $('#output_set-group');

        function toggleVerified(value) {
            console.log(value)
            if (value === 'Custom') {
                input_id.show();
                output_id.show();
            } else {
                input_id.hide();
                output_id.hide();
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
