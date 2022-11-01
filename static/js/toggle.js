const inv=document.querySelector('.Inventory')
function myFunction() {
  var x = document.getElementById("subs");
  if (x.style.display === "none") {
    x.style.display = "block";
    
    inv.classList.remove('right');
    inv.classList.add('down');
  } else {
    x.style.display = "none";
    
    inv.classList.add('right');
    inv.classList.remove('down');
  }
}