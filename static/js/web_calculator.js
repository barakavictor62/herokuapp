$( document ).ready(function() {
        var web_cost = 0;
        var obj = {}, key;
        $("input[type=radio]").click(function(){
                obj[$(this).attr("name")]= $(this).val();

                 for (key in obj) {
                        if (obj.hasOwnProperty(key)) {
                            alert(key + " = " + user[key]);
                        }
                }
        });
    });