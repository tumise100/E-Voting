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