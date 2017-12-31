$( document ).ready(function() {
        $("input[type=radio]").click(function(){
            var web_cost = +($(this).val());
            $(".website-price").val(web_cost);
        });
    });