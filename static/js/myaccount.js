$(document).ready(function () {
    $("#logoutbtn").click(function () {
        window.location.href="./backend/logout.php";
    });

    $("#dialog").dialog({
        autoOpen: false,
        modal: true,
        height: 300,
        width: 350,
        buttons:[
            {
                text:"cancel",
                style:"background-color:orange; color: white; font-weight:700;height:40px;",
                click:function () {
                    $(this).dialog("close");
                }
            },
            {
                text:"Submit",
                style:"background-color:#337ab7; color: white; font-weight:700;height:40px;",
                click:function () {
                    $(this).dialog("close");
            }
            }
            ]
    });
    $("#iniatePassChange").click(function () {
        $("#dialog").dialog("open");
    });

});
