$(document).ready(function () {
    $("#login-form").submit(function (event) {
        event.preventDefault();
        var $form = $(this),
            user=$("#user").val(),
            pass = $("#pass").val(),
            url = $form.attr("action");
        var $posting = $.post( url, { user: user, pass: pass } );
        $posting.done(function (data) {
            if(data == "index3.php") {
                window.location.href = "../" + data;
            }
            else {
                $("#inner-inner-form").css({"text-align":"center", "display":"block"});

            }
        })
    })
});