function openPlayerConfig() {
    playerConfigOverlayElement.style.display = 'block';
    backdropElement.style.display = 'block';
}

function closePlayerConfig() {
    playerConfigOverlayElement.style.display = 'none';
    backdropElement.style.display = 'none';
}

function savePlayerConfig(event) {
    event.preventDefault();
    const formdata = new FormData(event.target);
    const enteredPlayername = formdata.get('playername').trim();

    if (!enteredPlayername ){
        errorsOutputElement.textContent = 'Please enter a valid name!';
        return;
    }
}