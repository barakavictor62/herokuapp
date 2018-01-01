$( document ).ready(function() {
        var web_cost = 0;
        var obj = [];
        $("input[type=radio]").click(function(){
                var name = $(this).attr("name");
                var hel_val = $(this).val();
                var clicked_element = {name_el:name, el_hel_val:hel_val};
                 obj.push(clicked_element);
                 alert(obj);
        });
    });