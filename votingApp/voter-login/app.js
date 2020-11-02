// ********** set date ************
const date = document.getElementById('date');
date.innerHTML = new Date().getFullYear();


const modalBtn = document.getElementById('modal-btn');
const modalOverlay = document.querySelector('.modal-overlay');
const closeBtn = document.querySelector('.close-btn');



modalBtn.addEventListener('click', function() {
    modalOverlay.classList.add('open-modal');
    console.log('Clicked button');
});

closeBtn.addEventListener('click', function () {
  modalOverlay.classList.remove('open-modal')  
})