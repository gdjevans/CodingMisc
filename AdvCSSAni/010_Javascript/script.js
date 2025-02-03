let text = document.querySelector('.text');
let spans = text.innerText.split('').map((letter, i) => {
   return `<span style="transition-delay:${i*40}ms; filter:hue-rotate(${i*30}deg)">${letter}</span>`
}).join('');

text.innerHTML = spans;

let parallaxText = document.getElementById('parallaxText');
let leaf = document.getElementById('leaf');
let hill1 = document.getElementById('hill1');
let hill4 = document.getElementById('hill4');
let hill5 = document.getElementById('hill5');

window.addEventListener('scroll', () => {
    let value = window.scrollY;

    parallaxText.style.marginTop = `${value * 2.5}px`;
    leaf.style.top = `${value * -1.5}px`;
    leaf.style.left = `${value * 1.5}px`;
    hill5.style.left = `${value * 1.5}px`;
    hill4.style.left = `${value * -1.5}px`;
    hill1.style.top = `${value * 1}px`;
})

let card = document.querySelector('.card');
let toggle = document.querySelector('.toggle');

toggle.addEventListener('click', () => {
    card.classList.toggle('active');
    // inspect the card
})

let colorfulText = document.querySelector('.colorfulText');

let htmlSpans = colorfulText.innerText.split('').map((letter, i) => {
    return `<span style= "animation-duration: ${Math.random() * 5}s; filter: hue-rotate(${i *50}deg">${letter}</span>`
}).join('');

colorfulText.innerHTML = htmlSpans;
