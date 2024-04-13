document.addEventListener('DOMContentLoaded', function() {
    var successMessage = sessionStorage.getItem('success_message');
    if (successMessage) {
        var successBanner = document.createElement('div');
        successBanner.classList.add('success-message');
        successBanner.textContent = successMessage;
        document.body.appendChild(successBanner);
        // Clear the success message from session storage
        sessionStorage.removeItem('success_message');
        // Close the banner after 5 seconds
        setTimeout(function() {
            successBanner.remove();
        }, 5000);
    }
});