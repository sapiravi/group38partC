// document.addEventListener("DOMContentLoaded", function () {
//     var loginForm = document.getElementById("loginForm");
//     var IDInput = document.getElementById("IDInput");
//     var passwordInput = document.getElementById("passwordInput");
//     var errorMessage = document.getElementById("errorMessage");
//
//     loginForm.addEventListener("submit", function (event) {
//         event.preventDefault();
//
//
//         if (IDInput.value === "123456789" && passwordInput.value === "123456") {
//
//             window.location.href = "HomePage.html";
//         } else {
//
//             errorMessage.style.display = "block";
//         }
//     });
// });
//
// document.addEventListener("DOMContentLoaded", function () {
//     var loginForm = document.getElementById("loginForm");
//     var IDInput = document.getElementById("IDInput");
//     var passwordInput = document.getElementById("passwordInput");
//     var errorMessage = document.getElementById("errorMessage");
//
//     loginForm.addEventListener("submit", function (event) {
//         event.preventDefault();
//
//         // Get form data
//         var formData = new FormData();
//         formData.append('id', IDInput.value);
//         formData.append('password', passwordInput.value);
//
//         // Send AJAX request to Flask server
//         var xhr = new XMLHttpRequest();
//         xhr.open('POST', '/Login');
//         xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
//         xhr.onload = function () {
//             if (xhr.status === 200) {
//                 // Successful login, redirect to home page
//                 window.location.href = "/HomePage";
//             } else {
//                 // Failed login, display error message
//                 errorMessage.innerText = "Invalid username or password";
//                 errorMessage.style.display = "block";
//             }
//         };
//         xhr.send(new URLSearchParams(formData));
//     });
// });