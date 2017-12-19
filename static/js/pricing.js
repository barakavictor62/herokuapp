$(document).ready(function () {
    /*$(window).scroll(function () {
        if($(window).scrollTop()>340){
            $(".navbar-default").css({"background-color":"#fff","box-shadow": "0 5px 3px 0 slategray"});
            $(".go-gray>a, .logo").css({"color":"gray"});

        }
        else{
            $(".navbar-default").css({"background-color":"transparent","box-shadow": "none"});
        }
    });*/
    $("#content-price").click(function () {
       $(".content-price-list").css({"display":"block"});
       $(".web-price-list").css({"display":"none"});
    });
    $("#web-price").click(function () {
        $(".web-price-list").css({"display":"block"});
        $(".content-price-list").css({"display":"none"});
    });
});