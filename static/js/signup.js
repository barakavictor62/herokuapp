$(document).ready(function () {
    $("#signup-form").submit(function (event) {
        event.preventDefault();
        var $form = $(this),
            fname = $("#inputFirstname").val(),
            lname = $("#inputLastname").val(),
            email = $("#inputEmail").val(),
            username=$("#inputUsername").val(),
            password = $("#inputPassword").val(),
            url = $form.attr("action");
        var $posting = $.post(
            url,
            {
                inputFirstname: fname,
                inputLastname: lname,
                inputUsername: username,
                inputEmail: email,
                inputPassword: password
            }
            );
        $posting.done(function (data) {
            if(data === "success") {
                window.location.href = "../login.php";
            }
            else {
                $("#inner-inner-form").css({"text-align":"center", "display":"block"});

            }
        })
    })
});