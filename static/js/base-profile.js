$(document).ready(function() {
    $('#menu-toggle').click(function (e) {
      e.preventDefault();
    $('#wrapper').toggleClass('menuDisplayed');
    $("#page-content-wrapper").toggleClass("col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 col-lg-11 ");
    });

    $("#id_article_cost").val("$"+(($("#id_word_count").val())*0.016).toFixed(2));
    $("#sidenav").height($(".profiler").height());

    $("#id_word_count").change(function () {
        var words = $("#id_word_count").val();
        var cost = words* 0.016;
        $("#id_article_cost").val("$"+cost.toFixed(2));
    });

    $(".mytab").click(function (event) {
        event.preventDefault();
        $(this).siblings().find("a").removeClass("active");
        $(this).find("a").addClass("active");
        $("."+$(this).attr("id")).css({"display":"block"}).siblings().hide();
    });
    $("#close-btn").click(function(){
        $("#sidenav").width(0).children().css( "display","none") ;
    });
    $("#navigate").click(function() {
        $("#sidenav").css("display","flex").width(250).children().css( "display","block") ;
    });

});
