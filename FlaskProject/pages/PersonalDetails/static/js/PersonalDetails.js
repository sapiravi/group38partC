function toggleEditMode() {
    var editButton = document.getElementById('editButton');
    var saveButton = document.getElementById('saveButton');
    var valueElements = document.querySelectorAll('.value');

    if (editButton.textContent === 'Edit Details') {
        valueElements.forEach(function(element) {
            element.contentEditable = 'true';
            element.classList.add('editable');
        });
        editButton.textContent = 'Cancel';
        saveButton.style.display = 'inline-block';
    } else {
        // No need to reload the page, just revert changes made in edit mode
        valueElements.forEach(function(element) {
            element.contentEditable = 'false';
            element.classList.remove('editable');
        });
        editButton.textContent = 'Edit Details';
        saveButton.style.display = 'none';
    }
}

// Add event listener to the Edit button
document.getElementById('editButton').addEventListener('click', function() {
    toggleEditMode();
});

// Add event listener to the Save button
document.getElementById('saveButton').addEventListener('click', function(event) {
    event.preventDefault();

    // Gather data from the form
    var id = document.getElementById('id').textContent;
    var phone = document.getElementById('phoneNumber').textContent;
    var email = document.getElementById('emailAddress').textContent;
    var gender = document.getElementById('gender').textContent;
    var firstname = document.getElementById('firstName').textContent;
    var lastname = document.getElementById('lastName').textContent;
    var birthdate = document.getElementById('birthdate').textContent;

    // Send a POST request to update personal details
    fetch('/update_personal_details', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: id,
            phone: phone,
            email: email,
            gender: gender,
            firstname: firstname,
            lastname: lastname,
            birthdate: birthdate
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // If the response from the server was ok, update the user interface
        location.reload(); // Alternatively, you can update only the dynamic parts of the interface by updating only the changing details
    })
    .catch(error => {
        console.error('There was an error!', error);
    });
});
