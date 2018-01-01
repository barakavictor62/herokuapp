$( document ).ready(function() {
        var web_cost = 0;
        var obj = [];
        $("input[type=radio]").click(function(){
                var name = $(this).attr("name");
                var hel_val = $(this).val();
                 obj.push({name_el:name,
                         el_hel_val:hel_val
                        });
                 alert(JSON.stringify(obj));
        });
    });