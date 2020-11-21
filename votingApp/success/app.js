const toggleBtn = document.querySelector('.nav-toggle');
const sidebar = document.querySelector('.sidebar');
const closeBtn = document.querySelector('.close-btn');


toggleBtn.addEventListener("click", function () {
    sidebar.classList.toggle('show-sidebar');
});

closeBtn.addEventListener('click', function () {
    sidebar.classList.remove('show-sidebar');
});


/*
===================== modal ===============
*/

var buttons = document.querySelectorAll("button");
for(button in buttons) {
	buttons[button].onclick = function(){
        var blueButton = document.querySelectorAll(".green")[0];
    	if(this.className == "grey") {
            if( blueButton ) blueButton.className = "grey";
            this.className = "green";
        }
    }
}



// Get the button that opens the modal
var btn = document.querySelectorAll("button.modal-button");

// All page modals
var modals = document.querySelectorAll('.modal');

// Get the <span> element that closes the modal
var spans = document.getElementsByClassName("close");

// When the user clicks the button, open the modal
for (var i = 0; i < btn.length; i++) {
 btn[i].onclick = function(e) {
    e.preventDefault();
    modal = document.querySelector(e.target.getAttribute("href"));
    modal.style.display = "block";
 }
}

// When the user clicks on <span> (x), close the modal
for (var i = 0; i < spans.length; i++) {
 spans[i].onclick = function() {
    for (var index in modals) {
      if (typeof modals[index].style !== 'undefined') modals[index].style.display = "none";    
    }
 }
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
     for (var index in modals) {
      if (typeof modals[index].style !== 'undefined') modals[index].style.display = "none";    
     }
    }
}