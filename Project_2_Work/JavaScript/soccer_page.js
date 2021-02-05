function opentopic(evt, cityName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("city");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" w3-red", "");
      console.log(tablinks[i].innerHTML)
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " w3-red";
  }



function openinstruction(evt, soccerStep, buttons_to_uncolour, segements_to_hide) {
    var i, x, tablinks;
    x = document.getElementsByClassName(segements_to_hide);
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    tablinks_strike = document.getElementsByClassName(buttons_to_uncolour);
    for (i = 0; i < x.length; i++) {
      tablinks_strike[i].className = tablinks_strike[i].className.replace(" w3-red", "");
    }
    document.getElementById(soccerStep).style.display = "block";
    evt.currentTarget.className += " w3-red";
  }
