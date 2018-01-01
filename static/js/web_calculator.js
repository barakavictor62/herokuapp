$( document ).ready(function() {
        var web_cost = 0;
        var obj = {};
        $("input[type=radio]").click(function(){
                obj[$(this).attr("name")]= $(this).val();
                 alert(JSON.stringify(obj));
        });
    });