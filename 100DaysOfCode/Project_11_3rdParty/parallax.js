const imageElement = document.getElementById('main-image');
new simpleParallax(imageElement, {
	delay: .6,
	transition: 'cubic-bezier(0,0,0,1)'
});