const modal = document.getElementById('prompt-window');
const closeButtons = modal.querySelectorAll('.close-modal-button');

modal.style.display = 'block';

closeButtons.forEach(element => {
  element.addEventListener('click', event => {
    modal.style.display = 'none';
  });
});
