let fistBtn = document.getElementById('1');
let secondBtn = document.getElementById('2');
let thirdBtn = document.getElementById('3');

fistBtn.addEventListener('click', () => {
    fistBtn.classList.add('highlight');
    secondBtn.classList.remove('highlight');
    thirdBtn.classList.remove('highlight');
});

secondBtn.addEventListener('click', () => {
    secondBtn.classList.add('highlight');
    fistBtn.classList.remove('highlight');
    thirdBtn.classList.remove('highlight');
});

thirdBtn.addEventListener('click', () => {
    thirdBtn.classList.add('highlight');
    secondBtn.classList.remove('highlight');
    fistBtn.classList.remove('highlight');
});