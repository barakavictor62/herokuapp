$( document ).ready(function() {
        var web_cost = 0;
        var obj = {}, key;
        $("input[type=radio]").click(function(){
                obj[$(this).attr("name")]= $(this).val();

                $.each( obj, function( key, value ) {
                        alert( key + ": " + value );
                      });
        });
    });