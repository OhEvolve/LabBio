


(function($) {

    String.prototype.format = function () {
      var i = 0, args = arguments;
      return this.replace(/{}/g, function () {
        return typeof args[i] != 'undefined' ? args[i++] : '';
      });
    };


    $(function() {

        var fieldTemplate = '#id_step_set-{}-{}',
            stepTemplate  = '#id_step_set-{}-name';
            
            // standard field fields
            fieldDict = {'Mix': ['temperature','temperature_units'],
                         'Incubate': ['time','time_units','temperature','temperature_units'],
                         'Centrifuge': ['speed','speed_units','temperature','temperature_units'],
                         'Decant':['action'],
                         'Thermocycle':[''],
                         'Resuspend': ['temperature','temperature_units'],
                         'Transfer':['container'],
                         'Operate':['']};

            entryTemplate = '#step_set-{} .field-{}',

            // special field hiding
            nested_fieldDict = {'Thermocycle': ['thermocyclestep'],
                'Operate':['operatestep'],
                'Mix':['addedliquid','addedsolid','addedbiologic','addedcell'],
                'Resuspend':['addedliquid','addedsolid','addedbiologic','addedcell']},
            nestedTemplate = '#step_set-{}-{}_set-group'

            total = $('#id_step_set-TOTAL_FORMS'),
            fixed_total = 5;
        

        function toggleFields(index,state) {
             for (key in fieldDict) {
                    for (ii in fieldDict[key]) {
                        $(entryTemplate.format(index,fieldDict[key][ii])).hide();
                    }
            }
            for (key in nested_fieldDict) {
                    for (ii in nested_fieldDict[key]) {
                        $(nestedTemplate.format(index,nested_fieldDict[key][ii])).hide();
                    }
            }
            for (ii in fieldDict[state]) {
                $(entryTemplate.format(index,fieldDict[state][ii])).show();
            }
            for (ii in nested_fieldDict[state]) {
                $(nestedTemplate.format(index,nested_fieldDict[state][ii])).show();
            }
        }
        

        // show/hide on load based on pervious value of selectField
        for (i = 0; i < total.val(); i++) {
            toggleFields(i,$(stepTemplate.format(i)).val())
        }

        // Instances the variable i
        function callback(stepTemplate,i) {
            return function() {
                toggleFields(i,$(stepTemplate.format(i)).val())
            }
        }

        // show/hide on change
        for (i = 0; i < total.val(); i++) {
            $(stepTemplate.format(i)).change(callback(stepTemplate,i));
        };

        $(document).on('formset:added', function(a,b,c) {
            var rows = total.val() - 1;
            toggleFields(rows,$(stepTemplate.format(rows)).val());
            $(stepTemplate.format(rows)).change(callback(stepTemplate,rows));
        });

        $(document).on('formset:removed', function(a,b,c) {
            for (i = 0; i < total.val(); i++) {
                toggleFields(i,$(stepTemplate.format(i)).val());
                $(stepTemplate.format(i)).change(callback(stepTemplate,i));
            };
        });

    });

}(django.jQuery));









