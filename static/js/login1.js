
$(document).ready(function() {

/*------------------------------------------------------------------------*/
$("#signup-form").dialog({
   autoOpen: false,
    modal:true,
   width:600
});
$("#sinup").click(function() {
   $("#signup-form").dialog("open");
   $(".holder").fadeTo("fast",0.2);
});
$("#signup-form").on('dialogclose',function(event){
    $(".holder").fadeTo("fast",1);
    $("#sinup").blur();
});


    $("#tosinup").click(function () {
        $("#sinup").click();

    });
/*-----------------------------------------------------------------------------*/
/*--------------------------------------------------------------------------------*/
$(function(){
  $("#signup-form").load("signup.html");});
/*---------------------------------------------------------------------------------*/

  $("#sub").click(function(){
	var usname=$("#uname").val();
	var pass=$("#pass").val();
        if((usname && pass)=="" || usname=="" || pass==""){
       /*$("#login_err").after("<p>Please fill all fields</p>");*/}
else{
	$("#login_err").load('login2.php',{"user":usname,"pass":pass});
}
});
});
