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
/*
const modalBtn = document.getElementById('modal-btn');
const modalOverlay = document.querySelector('.modal-overlay');
const modalcloseBtn = document.querySelector('.modalclose-btn');



modalBtn.addEventListener('click', function() {
    modalOverlay.classList.add('open-modal');
    console.log('Clicked button');
});

modalcloseBtn.addEventListener('click', function () {
  modalOverlay.classList.remove('open-modal')  
});



//cast vote button
const clicked = document.getElementById('clicked');
clicked.addEventListener('click', function () {
  clicked.innerHTML = "Voted";
  clicked.style.backgroundColor = 'green';
  clicked.style.color = 'white';

  if (click == clicked.innerHTML);
  clicked.removeEventListener('click', function() {
  	clicked
  })
});




const clicked1 = document.getElementById('clicked1');
clicked1.addEventListener('click', function () {
  clicked1.innerHTML = "Voted";
  clicked1.style.backgroundColor = 'green';
  clicked1.style.color = 'white';
});
const clicked2 = document.getElementById('clicked2');
clicked.addEventListener('click', function () {
  clicked2.innerHTML = "Voted";
  clicked2.style.backgroundColor = 'green';
  clicked2.style.color = 'white';
});
const clicked3 = document.getElementById('clicked3');

clicked3.addEventListener('click', function () {
  clicked3.innerHTML = "Voted";
  clicked3.style.backgroundColor = 'green';
  clicked3.style.color = 'white';
});
// clicked2.addEventListener('click', function () {
//   clicked2.innerHTML = "voted";
//   clicked2.style.backgroundColor = 'green';
//   clicked2.style.color = 'white';
//   console.log('Clicked button');
// });


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