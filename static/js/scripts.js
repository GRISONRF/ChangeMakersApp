var aboutUs = {
    "Education": " <ul><li>Bachelor's degree in Business Administration - 2015</li><li>Complete Javascript & jQuery course with bonus Vue JS intro - Udemy</il><li>Full Stack course - Codecademy </li><li>Python - NuCamp Bootcamp</li> <li>Frontend - NuCamp Bootcamp</li> </ul> ",
    "Work experience": "From 2010 to 2019, I've had numerous work and intern experiences related to business and/or marketing.<br><br> I worked in a Bank, in a Investment Institute and in 2 Governmental Institutions. <br><br> In 2016 I had my own small business, and among many other tasks, I was responsible for creating business plans, arranging financing, reviewing sales, developing marketing strategies, overseeing daily activities, and identifying business opportunities. ",
    "Programming": "I\'m still in the beginning of my journey as a programmer, and so far I only have basic projects to show, such as: <ul><li>This website (JS)</li><li>Self-Service machine (JS)</li><li>T-shirts e-commerce (JS)</li><li>War game (Python)</li><li>Coin toss game (Python)</li></ul>"
  };
  
  var unseletectedColor = "#646872";
  var seletectedColor = "#2A2D34";
  var aboutUsTabs = document.getElementsByClassName("single-tab");
  
  for (var a = 0; a < aboutUsTabs.length; a++) {
    aboutUsTabs[a].onclick = function(){
      var clickedValue = this.innerHTML;
      document.getElementById("box-text").innerHTML = aboutUs[clickedValue]
  
      for (var b = 0; b < aboutUsTabs.length; b++) {
        aboutUsTabs[b].style["background-color"] = unseletectedColor;
        aboutUsTabs[b].style["font-weight"] = "normal"
      }
  
      this.style["background-color"] = seletectedColor;
      this.style["font-weight"] = "bold";
    }
  }
  