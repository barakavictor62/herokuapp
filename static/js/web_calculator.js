$( document ).ready(function() {
        $("input[type=radio]").click(function(){
            var web_cost += Number($(this).val());
            $(".website-price").text(web_cost);
        });
    });