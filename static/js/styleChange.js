let els=document.getElementsByClassName("per");
for(let i=0;i<els.length;i++) {
    let d=parseFloat(els[i].innerHTML);
    console.log(d);
    if(d<0)
        els[i].style.color="red";
    else
        els[i].style.color="green";
    els[i].innerHTML="<strong>"+d+"%</strong>";
}