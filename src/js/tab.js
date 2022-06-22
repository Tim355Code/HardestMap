opentab=(tabName)=>{
  let x = document.getElementsByClassName("tab");
  let y = document.getElementsByClassName("tabButton");
  let z = document.getElementsByClassName("Bli");
  for (var i = 0; i < x.length; i++) {
    x[i].style.display = "none";
    y[i].style.fontWeight = "100";
    z[i].style.borderBottom = "0px";
  }
  document.getElementById(tabName).style.display = "block";  
  document.getElementById("but"+tabName).style.fontWeight = "bold";
  document.getElementById(tabName+"but").style.borderBottom = "2px solid #CC2500";
}