function maker() {
    window.location.href = "#main2";
}

let selectedTemplate = null;

function selectTemplate(templateId) {
    if (selectedTemplate) {
        selectedTemplate.classList.remove("selected");
    }

    selectedTemplate = document.querySelector(`.template-card:nth-child(${templateId})`);
    selectedTemplate.classList.add("selected");

    localStorage.setItem("selectedTemplate", templateId);
}

function nextPage() {
    if (selectedTemplate) {
        window.location.href = "maker/";
    } else {
        alertMessageShow("Please select a template to proceed.");
    }
}






function alertMessageShow(text){
  
    let alertText = document.getElementById("alert-text")
    alertText.innerHTML = text;
    
    let alertBox = document.getElementById("alert-box");
    alertBox.style.display = "flex";
    
  }
  
  
  let alertButton = document.querySelector(".alert-button")
  alertButton.addEventListener("click", function() {
    let alertBox = document.getElementById("alert-box");
    alertBox.style.display = "none";
  });
  


let templates = document.querySelectorAll(".alltemplates > div");
templates.forEach(elem => {
    elem.addEventListener("click",function(){
        scrollToSection("footer");
    })
})


function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({
        behavior: 'smooth'
      });

      if (sectionId == "footer"){
            let btn1 = document.getElementById("btn1");
            btn1.classList.add("btn1Ani");
            
            // setTimeout(function(){
            //     let btn1 = document.getElementById("btn1");
            //     btn1.classList.remove("btn1Ani");
            // },12000)

            // btn1.style.boxShadow = "0px 5px 10px 0 var(--button-hover), 0px -5px 10px 0 var(--button-hover)";
      }

    }
  }



