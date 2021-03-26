var list;

function init(){
    list = document.getElementById("lotList");
    priceLowtoHigh();
}

function priceLowtoHigh(){
    let switching, i, b, shouldSwitch;
    switching = true;
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        b = list.getElementsByTagName("LI");
        // Loop through all list items:
        for (i = 0; i < (b.length - 1); i++) {
          // Start by saying there should be no switching:
          shouldSwitch = false;
          /* Check if the next item should
          switch place with the current item: */
          if (parseInt(b[i].getAttribute("data-price")) > parseInt(b[i + 1].getAttribute("data-price"))) {
            /* If next item is alphabetically lower than current item,
            mark as a switch and break the loop: */
            shouldSwitch = true;
            break;
          }
        }
        if (shouldSwitch) {
          /* If a switch has been marked, make the switch
          and mark the switch as done: */
          b[i].parentNode.insertBefore(b[i + 1], b[i]);
          switching = true;
        }
      }
}
function priceHightoLow(){
    let switching, i, b, shouldSwitch;
    switching = true;
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        b = list.getElementsByTagName("LI");
        // Loop through all list items:
        for (i = 0; i < (b.length - 1); i++) {
          // Start by saying there should be no switching:
          shouldSwitch = false;
          /* Check if the next item should
          switch place with the current item: */
          if (parseInt(b[i].getAttribute("data-price")) < parseInt(b[i + 1].getAttribute("data-price"))) {
            /* If next item is alphabetically lower than current item,
            mark as a switch and break the loop: */
            shouldSwitch = true;
            break;
          }
        }
        if (shouldSwitch) {
          /* If a switch has been marked, make the switch
          and mark the switch as done: */
          b[i].parentNode.insertBefore(b[i + 1], b[i]);
          switching = true;
        }
      }

}
function distanceShort(){
    let switching, i, b, shouldSwitch;
    switching = true;
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        b = list.getElementsByTagName("LI");
        // Loop through all list items:
        for (i = 0; i < (b.length - 1); i++) {
          // Start by saying there should be no switching:
          shouldSwitch = false;
          /* Check if the next item should
          switch place with the current item: */
          if (parseInt(b[i].getAttribute("data-distance")) > parseInt(b[i + 1].getAttribute("data-distance"))) {
            /* If next item is alphabetically lower than current item,
            mark as a switch and break the loop: */
            shouldSwitch = true;
            break;
          }
        }
        if (shouldSwitch) {
          /* If a switch has been marked, make the switch
          and mark the switch as done: */
          b[i].parentNode.insertBefore(b[i + 1], b[i]);
          switching = true;
        }
      }

}
function distanceLong(){
    let switching, i, b, shouldSwitch;
    switching = true;
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        b = list.getElementsByTagName("LI");
        // Loop through all list items:
        for (i = 0; i < (b.length - 1); i++) {
          // Start by saying there should be no switching:
          shouldSwitch = false;
          /* Check if the next item should
          switch place with the current item: */
          if (parseInt(b[i].getAttribute("data-distance")) > parseInt(b[i + 1].getAttribute("data-distance"))) {
            /* If next item is alphabetically lower than current item,
            mark as a switch and break the loop: */
            shouldSwitch = true;
            break;
          }
        }
        if (shouldSwitch) {
          /* If a switch has been marked, make the switch
          and mark the switch as done: */
          b[i].parentNode.insertBefore(b[i + 1], b[i]);
          switching = true;
        }
      }

}
function tailgates(){
    let b = list.getElementsByTagName("LI");
    for(let i = 0; i < b.length; i++){
        if(b[i].hasAttribute("data-tailgate")){
            b[i].style.display = "block";
        }
        else{
            b[i].style.display = "none"
        }
    }

}
function noTailgates(){
    let b = list.getElementsByTagName("LI");
    for(let i = 0; i < b.length; i++){
        if(b[i].hasAttribute("data-tailgate")){
            b[i].style.display = "none";
        }
        else{
            b[i].style.display = "block"
        }
    }

}
function anyTailgates(){

    let b = list.getElementsByTagName("LI");
    for(let i = 0; i < b.length; i++){
        b[i].style.display = "block";
        

    }

}