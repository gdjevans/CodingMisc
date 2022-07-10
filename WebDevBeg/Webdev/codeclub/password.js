function checkPassword() {
    //Capture the user entered password from our input element.
    var passwordBoxObject = document.getElementById('passwordBox');
    var passwordEntered = passwordBoxObject.value;
    //Check if the password is correct
    var sitePassword = "codeclub";
    if (passwordEntered == sitePassword) {
        // Allow navigation
        console.log('Allow');
        window.location.assign('members.html');
    } else {
        //block navigation
        console.log('Block');
        //Adding a new style rule to the incorrect-password element
        document.getElementById('incorrect-password').style.color = 'red';
        // Adding text to the incorrect password element
        document.getElementById('incorrect-password').innerHTML = 'Incorrect Password. Please try again.';   
    }

}