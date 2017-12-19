$(document).ready(function () {
    $("#logout").click(function () {
        window.location.href="./backend/logout.php";
    });
    function calculate() {
        alert($("#words").val());
    }
    $("#words").change(function () {
        var words = $("#words").val();
        var cost = words* 0.8;
        $("#cost").val("$"+cost);
    })
});