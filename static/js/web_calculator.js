$( document ).ready(function() {
        $("input[type=radio]").click(function(){
            alert($(this).val());
        });
    });