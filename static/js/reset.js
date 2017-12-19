$(document).ready(function () {
    $("#reset-form").submit(function (event) {
        event.preventDefault();
        var $form = $(this),
            email=$("#inputEmail").val(),
            url = $form.attr("action");
        var $posting = $.post( url, { inputEmail:email } );
        $posting.done(function (data) {
            $(".mssg").remove();
            $(data).insertAfter("#instruction");
            });
    })
});
