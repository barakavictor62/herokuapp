$( document ).ready(function() {
        var web_cost = 0;
        var obj = {}, key;
        $("input[type=radio]").click(function(){
                obj[$(this).attr("name")]= $(this).val();
                 alert(JSON.stringify(obj));

                 for (key in obj) {
                        if (user.hasOwnProperty(key)) {
                            alert(key + " = " + user[key]);
                        }
                }
        });
    });