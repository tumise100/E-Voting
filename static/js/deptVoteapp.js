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
// const clicked2 = document.getElementById('clicked-2');
// const clicked3 = document.getElementById('clicked-3');
// const clicked4 = document.getElementById('clicked-4');

clicked.addEventListener('click', function () {
  clicked.innerHTML = "voted";
  clicked.style.backgroundColor = 'green';
  clicked.style.color = 'white';
  console.log('Clicked button');
});
// clicked2.addEventListener('click', function () {
//   clicked2.innerHTML = "voted";
//   clicked2.style.backgroundColor = 'green';
//   clicked2.style.color = 'white';
//   console.log('Clicked button');
// });

