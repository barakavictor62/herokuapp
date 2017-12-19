$("#passchange").css("display","none");
$(document).ready(function($) {
$("#passchange").dialog({
   autoOpen: false
});
$("#foto").click(function() {
   $("#passchange").dialog("open");
});
$("#passchange").on('dialogclose',function(event){
$("#foto").blur();
});
});
   $("#dialog").css("display","none");
$(document).ready(function() {
   $("#datepik").click(function(){
 $("#datepik").datepicker();
});
});
  $("#test2").css("display","none");
$(document).ready(function() {
$("#cdp").click(function(){
var xhtp=$("#password").val();
var xhtp2=$("#password1").val();
var xhtp3=$("#password2").val();
if(xhtp != "" && xhtp2 != "" && xhtp3 != ""){
$("#test2").load('myacc.php',{"password":xhtp,"password1":xhtp2,"password2":xhtp3});
}
else if(xhtp == "" || xhtp2 == "" || xhtp3 == ""){
$("#test2").css("display","none");
}
});
});
$(document).ready(function($){
$("#dialog").dialog({
   autoOpen: false
});
$("#chaa").click(function() {
   $("#dialog").dialog("open");
});
$("#dialog").on('dialogclose',function(event){
$("#chaa").blur();
});
});
