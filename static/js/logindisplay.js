/**
 * Created by baraka62 on 5/22/2017.
 */
$(document).ready(function () {
    $(window).scroll(function () {
        if($(window).scrollTop()>565){
            $(".navbar-default").css({"background-color": "#2c3e50"});
            $(".go-gray>a, .logo").css({"color":"#fff"});
        }
        else{
            $(".navbar-default").css({"background-color":"transparent"});
            $(".go-gray>a, .logo").css({"color":"#fff"});

        }
    });
    $("#loginbtn").click(function () {
        window.location.href="login.php";
    });
    $(".signupbtn").click(function(){
        window.location.href="signup.php";
    });

});
