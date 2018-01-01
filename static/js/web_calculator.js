$( document ).ready(function() {
        var obj = {}, key;
        $(":input").change(function(){
                var web_cost = 0;
                obj[$(this).attr("name")]= $(this).val();

                $.each( obj, function( key, value ) {
                        web_cost+=Number(value);
                      });
                $(".website-price").text(web_cost);
        });
    });