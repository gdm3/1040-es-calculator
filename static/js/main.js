var currentlyHovered = "none"



function hoverEffect(hovered){
  console.log("Hovered ", hovered)
  currentlyHovered = hovered
  //Create currently hovered obj
  informationBox = document.getElementById("Information-" + hovered)
  var rect = informationBox.getBoundingClientRect();
  console.log(rect.top, rect.right, rect.bottom, rect.left);
  informationHover = document.getElementById("information-hover")
  if(hovered == "QuartIncome"){
    informationHover.style.top = rect.top - 90 + "px"
    informationHover.style.left = rect.left - 115 + "px"
    informationHover.style.height = 70 + "px"
  }
  else if(hovered == "OthTaxes"){
    informationHover.style.top = rect.top - 130 + "px"
    informationHover.style.left = rect.left - 115 + "px"
    informationHover.style.height = 110 +"px";
  }
  else{
    informationHover.style.top = rect.top - 150 + "px"
    informationHover.style.left = rect.left - 115 + "px"
    informationHover.style.height = 130 +"px";
  }
  informationHover.style.visibility = "visible"
  informationHover.style.opacity = 1
  textInside = document.getElementById("text-inside")
  header = document.getElementById("text-header")
  if(hovered == "QuartIncome"){
    header.innerText = "Quarterly Income"
    textInside.innerText = "The amount of revenue you generated this quarter, not including deductions."
  }
  else if(hovered == "QuartDeduction"){
    header.innerText = "Quarterly Deduction"
    textInside.innerText = "Expenses that you incurred during the quarter. If you spent less than $3,462.50, you are eligible for the standard deduction. This means that the IRS will assume that you spent $3,462.50 regardless of whether you did or not."
  }
  else if(hovered == "AltMinTax"){
    header.innerText = "Alternative Minimum Tax"
    textInside.innerText = "Usually not applicable. This was a tax introduced to ensure that wealthy Americans pay their fair share of taxes. If you made less than $130,000 this quarter, you will not have to pay this in a vast majority of cases."
  }
  else if(hovered == "Credits"){
    header.innerText = "Tax Credits"
    textInside.innerText = "These are credits given to Americans to help alleviate tax bills or give a refund on taxes. The most common ones are the child tax credit and the earned income tax credit. Please do research to see if you are eligible for any tax credits."
  }
  else if(hovered == "OthTaxes"){
    header.innerText = "Other Taxes"
    textInside.innerText = "If you entered any tax amount into line 8 through 12 or lines 14 through 17z on IRS tax Form 1040 Schedule 2, please enter that amount here. Most people will not have any other taxes."
  }
  else if(hovered == "IncTaxWith"){
    header.innerText = "Withheld Income Tax"
    textInside.innerText = "Amount of taxes already withheld this quarter. Most commonly from a W-2 job, however may be applicable if you have already made other estimated tax payments this quarter. If you are unsure, enter 0."
  }
  if(window.screen.width < 751){
    setTimeout(function(){
      informationHover = document.getElementById("information-hover")
      informationHover.style.opacity = 0
      informationHover.style.top = -1000 + "px"
      informationHover.style.left = -1000 + "px"
    }, 5000);
  }
}

function sidebarOpen(){
  sidebar = document.getElementById("sidebar")
  if(window.screen.width > 751){
    if(sidebar.style.left == "0px"){
      sidebar.style.left = -100 + "px"
    }
    else{
      sidebar.style.left = 0 + "px"
    }
  }
  else{
    if(sidebar.style.left == "0px"){
      sidebar.style.left = -200 + "px"
      console.log("i ran")
    }
    else{
      sidebar.style.left = 0 + "px"
    }
  }
  
}

function leaveHover(hovered){
  console.log("Left hovered", hovered)
  currentlyHovered = "none"
  informationHover = document.getElementById("information-hover")
  informationHover.style.opacity = 0
  setTimeout(function(){
    informationHover = document.getElementById("information-hover")
    informationHover.style.top = -1000 + "px"
    informationHover.style.left = -1000 + "px"
  }, 190)
  
}



window.addEventListener('load', function() {
  document.getElementById("ham-menu").addEventListener("click", sidebarOpen, false);
  let QuartIncome = document.getElementById("Information-QuartIncome")
  let QuartDeduction = document.getElementById("Information-QuartDeduction")
  let AltMinTax = document.getElementById("Information-AltMinTax")
  let Credits = document.getElementById("Information-Credits")
  let OthTaxes = document.getElementById("Information-OthTaxes")
  let IncTaxWith = document.getElementById("Information-IncTaxWith")
  if(window.screen.width > 751){
    QuartIncome.addEventListener("mouseover", (event) => {hoverEffect("QuartIncome")}); 
    QuartDeduction.addEventListener("mouseover", (event) => {hoverEffect("QuartDeduction")}); 
    AltMinTax.addEventListener("mouseover", (event) => {hoverEffect("AltMinTax")}); 
    Credits.addEventListener("mouseover", (event) => {hoverEffect("Credits")}); 
    OthTaxes.addEventListener("mouseover", (event) => {hoverEffect("OthTaxes")}); 
    IncTaxWith.addEventListener("mouseover", (event) => {hoverEffect("IncTaxWith")});
  
  
    QuartIncome.addEventListener("mouseout", (event) => {leaveHover("QuartIncome")}); 
    QuartDeduction.addEventListener("mouseout", (event) => {leaveHover("QuartDeduction")}); 
    AltMinTax.addEventListener("mouseout", (event) => {leaveHover("AltMinTax")}); 
    Credits.addEventListener("mouseout", (event) => {leaveHover("Credits")}); 
    OthTaxes.addEventListener("mouseout", (event) => {leaveHover("OthTaxes")}); 
    IncTaxWith.addEventListener("mouseout", (event) => {leaveHover("IncTaxWith")}); 
  }
  else{
    QuartIncome.innerHTML = ""
    QuartDeduction.innerHTML = ""
    AltMinTax.innerHTML= ""
    Credits.innerHTML = ""
    IncTaxWith.innerHTML = ""
    OthTaxes.innerHTML = ""
    console.log("jsduijsidj")
    QuartIncome.addEventListener("click", (event) => {hoverEffect("QuartIncome")}); 
    QuartDeduction.addEventListener("click", (event) => {hoverEffect("QuartDeduction")}); 
    AltMinTax.addEventListener("click", (event) => {hoverEffect("AltMinTax")}); 
    Credits.addEventListener("click", (event) => {hoverEffect("Credits")}); 
    OthTaxes.addEventListener("click", (event) => {hoverEffect("OthTaxes")}); 
    IncTaxWith.addEventListener("click", (event) => {hoverEffect("IncTaxWith")});
  }
  
})


function postAjax(){
  let QuartIncome = document.getElementById("QuartIncome").value
  let QuartDeduction = document.getElementById("QuartDeduction").value
  let AltMinTax = document.getElementById("AltMinTax").value
  let Credits = document.getElementById("Credits").value  
  let OthTaxes = document.getElementById("OthTaxes").value
  let IncTaxWith = document.getElementById("IncTaxWith").value
  let filingStatus = document.getElementById("select-filing").value
  console.log(filingStatus) //single or married
  console.log(QuartIncome, QuartDeduction, AltMinTax, Credits, OthTaxes, IncTaxWith)
  var server_data = [
    {"QuartIncome":QuartIncome},
    {"QuartDeduction":QuartDeduction},
    {"AltMinTax":AltMinTax},
    {"Credits":Credits},
    {"OthTaxes":OthTaxes},
    {"IncTaxWith":IncTaxWith},
    {"Status":filingStatus},
  ]
  $.ajax({
    type: "POST",
    url: "/taxes",
    data: JSON.stringify(server_data),
    contentType: "application/json",
    dataType: 'json',
    success: function(result) {
      console.log("Result:");
      console.log(result);
      tempOutput = document.getElementById("output")
      tempOutput.value = result.processed
    } 
  });
}
