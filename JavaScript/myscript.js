

var myBall = document.getElementById("ball");
var loc = 200;

setInterval("myFunction()", 200);

function myFunction() 
{
    loc += 10;
    myBall.style.top = loc;
}
