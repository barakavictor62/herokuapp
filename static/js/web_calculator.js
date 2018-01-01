$( document ).ready(function() {
        var obj = {}, key;
        $(":input,input[type=select]").change(function(){
                var web_cost = 0;
                var el_value = 0;
                switch($(this).attr("name")){
                        case "responsive":
                                el_value = 250;
                                break;
                        case "page-numbers":
                                el_value = ($(this).val())*10;
                                break;
                        default:
                                el_value = $(this).val();
                }
                obj[$(this).attr("name")]= el_value;
                $.each( obj, function( key, value ) {
                        web_cost+=Number(value);
                      });
                $(".website-price").text(web_cost.toFixed(2));
        });
    });