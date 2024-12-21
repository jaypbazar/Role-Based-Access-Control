document.addEventListener('DOMContentLoaded', function() {
    // Get form and time input elements
    const bookingForm = document.querySelector('form[action="/booking"]');
    const reservationDateInput = document.getElementById('reservationDate');
    const startTimeInput = document.getElementById('startTime');
    const endTimeInput = document.getElementById('endTime');
    const parkingSpaceSelect = document.getElementById('parkingSpace');
    const createReservationButton = bookingForm.querySelector('button[type="submit"]');
    const errorContainer = document.createElement('div');
    errorContainer.classList.add('text-danger', 'my-2', 'col-12', 'text-center');

    // Function to show validation error inline
    function showValidationError(message) {
        errorContainer.textContent = message;
        endTimeInput.parentNode.parentNode.insertBefore(errorContainer, endTimeInput.parentNode.nextSibling);
    }

    // Function to check parking lot availability and button state
    function checkParkingLotAvailability() {
        // Disable create button if no parking lots are available
        if (parkingSpaceSelect.options.length <= 1) {  // 1 accounts for the initial default/placeholder option
            createReservationButton.disabled = true;
            createReservationButton.classList.add('disabled');
            showValidationError("Unable to add reservations at the moment.");
        } else {
            createReservationButton.disabled = false;
            createReservationButton.classList.remove('disabled');
            // Clear any previous error message about parking lots
            if (errorContainer.textContent.includes("No parking lots available")) {
                errorContainer.textContent = '';
            }
        }
    }

    // Check parking lot availability when the page loads
    checkParkingLotAvailability();

    // Add form submission validation
    bookingForm.addEventListener('submit', function(event) {
        // Parse reservation date, start and end times
        const reservationDate = new Date(reservationDateInput.value);
        const startTime = new Date(`${reservationDate.toISOString().split('T')[0]}T${startTimeInput.value}`);
        const endTime = new Date(`${reservationDate.toISOString().split('T')[0]}T${endTimeInput.value}`);

        // Get current date
        const currentDate = new Date();

        // Calculate time difference in milliseconds
        const timeDifference = endTime.getTime() - startTime.getTime();

        // Check if reservation date is before current date
        if (reservationDate < currentDate) {
            event.preventDefault();
            showValidationError("Reservation date cannot be in the past.");
        }
        // Check if reservation is less than 30 minutes
        else if (timeDifference < 30 * 60 * 1000) {
            event.preventDefault();
            showValidationError("Reservation time must be at least 30 minutes.");
        } else {
            // Clear any previous error message
            errorContainer.textContent = '';
        }
    });

    // Optionally, add an event listener to recheck availability if parking lots are dynamically populated
    const observer = new MutationObserver(checkParkingLotAvailability);
    observer.observe(parkingSpaceSelect, { childList: true });
});