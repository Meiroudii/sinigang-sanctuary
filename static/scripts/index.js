const initApp = () => {
    const hamburgerBtn = document.getElementById("hamburger-button");
    const mobileMenu = document.getElementById("mobile-menu");
    const messageSubmit = document.getElementById("messageSubmit");
    const textSubject = document.getElementById("subject");
    const textMessage = document.getElementById("message");

    const toggleMenu = () => {
        mobileMenu.classList.toggle('hidden')
        mobileMenu.classList.toggle('flex')
        hamburgerBtn.classList.toggle('toggle-btn')
    }

    // Mock Message System
    const submitAMessage = () => {
        if (textSubject.value && textMessage.value) {
            alert('Thank you for your message!');
        }
        else {
            alert('Please Enter the Required fields');
        }
    }

    hamburgerBtn.addEventListener('click', toggleMenu)
    mobileMenu.addEventListener('click', toggleMenu)
    messageSubmit.addEventListener('click', submitAMessage);
}

document.addEventListener('DOMContentLoaded', initApp);

