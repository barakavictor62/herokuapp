function showus() {
var di=document.createElement("div");
di.id="passchange";
var div=document.createElement("form");
div.setAttribute('method',"post");
div.setAttribute('action',"index5.php");
div.setAttribute('enctype',"multipart/form-data");
var div1=document.createElement("input");
div1.type="file";
div1.name="upload"; 
div1.id="upload";
var div2=document.createElement("input");
div2.type="submit";
div2.name="submit2"; 
div2.id="up";
div2.value="Upload";
di.appendChild(div);
div.appendChild(div1);
div.appendChild(div2);
$("body").append(di);
alert(div);
}
function whenprocessed() {
<?php
$ssqlw=$conn->prepare("SELECT sum(words) AS words FROM WordCount");
$ssqlw->execute();
$resw=$ssqlw->fetch(PDO::FETCH_OBJ);
$gotw=$resw->words;
if(is_null($gotw)){
$gotw=0;
}
?>
var tot=+(<?php echo $gotw;?>);
var al=+(document.getElementById("words").value);
var total=tot+al;
if(total > 2000){
     var days=(total/2000).toFixed(0);
     document.getElementById("due").value=("Due in "+days+" days.");
     while (document.getElementById("due").value!=""){
     var j=confirm("Your request will be processed after "+days+" days.Proceed?");
        if(j==true){
             return true;
                   }
        else{
             return false;
            }
                 }}
else if(total<= 2000){
     document.getElementById("due").value=("Pending.Due in Tomorrow.");
     var r=confirm("Your request will be processed.Proceed?");
        if(r==true){
             return true;
                   }
        else{
             return false;
            }
                      }
                 }

