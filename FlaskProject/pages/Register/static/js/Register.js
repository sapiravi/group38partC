window.onload = function() {
    let form = document.querySelector('#registerForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        console.log("Form submitted");
        let isValid = validateForm();

        if (isValid) {
            console.log("Validation passed");
            window.location.href = "Login.html"; // Change to appropriate route for Login page
        }
    });
};

function validateForm() {
    console.log("Validating form");

    let id = document.querySelector('input[name="id"]').value;
    let firstName = document.querySelector('input[name="first_name"]').value;
    let lastName = document.querySelector('input[name="last_name"]').value;
    let phone = document.querySelector('input[name="phone"]').value;
    let email = document.querySelector('input[name="email"]').value;
    let password = document.querySelector('input[name="password"]').value;

    if (id.length !== 9 || isNaN(id)) {
        alert("Please enter a valid ID with 9 digits only.");
        return false;
    }

    if (!/^[a-zA-Z]+$/.test(firstName) || !/^[a-zA-Z]+$/.test(lastName)) {
        alert("First and last names should contain only letters.");
        return false;
    }

    if (!/^0\d{9}$/.test(phone)) {
        alert("Please enter a valid phone number starting with 0 and containing 10 digits.");
        return false;
    }

    if (!/^[\w.-]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,}$/.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    if (password.length < 6) {
        alert("Password should be at least 6 characters long.");
        return false;
    }

    return true;
}
// document.addEventListener('DOMContentLoaded', function() {
//     var form = document.getElementById('registration-form');
//     var passwordInput = document.getElementById('password');
//     var confirmPasswordInput = document.getElementById('confirm-password');
//
//     form.addEventListener('submit', function(event) {
//         if (passwordInput.value.length < 6) {
//             alert("Password should be at least 6 characters long.");
//             event.preventDefault(); // Prevent form submission
//         } else if (passwordInput.value !== confirmPasswordInput.value) {
//             alert("Passwords do not match.");
//             event.preventDefault(); // Prevent form submission
//         }
//     });
// });

window.onload = function() {
    let form = document.querySelector('#registerForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        console.log("Form submitted");
        let isValid = validateForm();

        if (isValid) {
            console.log("Validation passed");
            // No redirection here, let Flask handle it
        }
    });
};