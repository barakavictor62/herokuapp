$( document ).ready(function() {
        var web_cost = 0;
        $("input[type=radio]").click(function(){
            web_cost += Number($(this).val());
            $(".website-price").text(web_cost);
        });
    });