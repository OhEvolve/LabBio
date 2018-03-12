
String.prototype.format = function () {
  var i = 0, args = arguments;
  return this.replace(/{}/g, function () {
    return typeof args[i] != 'undefined' ? args[i++] : '';
  });
};



(function($) {
    $(function() {

        console.log("here");

        var fieldTemplate = '#id_step_set-{}-{}'
            stepTemplate  = '#id_step_set-{}-date_range'
            myfields = ['start_date','end_date']
            total = $('#id_step_set-TOTAL_FORMS');
            entryTemplate = '#step_set-{} .field-{}'
            fixed_total = 5;
        

        function toggleFields(fields,index,template,state) {
             console.log(index)
             console.log(state)
             if (state === 'Custom') {
                for (ii in fields) {
                    $(template.format(index,fields[ii])).show();
                }
            } else {
                for (ii in fields) {
                    $(template.format(index,fields[ii])).hide();
                }
            }
        }
        

        // show/hide on load based on pervious value of selectField
        for (i = 0; i < fixed_total; i++) {
            toggleFields(myfields,i,entryTemplate,$(stepTemplate.format(i)).val())
        }

        // Instances the variable i
        function callback(myfields,entryTemplate,stepTemplate,i) {
            return function() {
                toggleFields(myfields,i,entryTemplate,$(stepTemplate.format(i)).val())
            }
        }

        // show/hide on change
        for (i = 0; i < fixed_total; i++) {
            $(stepTemplate.format(i)).change(callback(myfields,entryTemplate,stepTemplate,i));
        };

        total.format('val()',function() {
            console.log("Changes!");
        });
    });

})(django.jQuery);








