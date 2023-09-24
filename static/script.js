document.addEventListener("DOMContentLoaded", function () {
    const driveButton = document.getElementById("drive");
    const carbonSpan = document.getElementById("carbon");

    // Add event listeners for the game options
    driveButton.addEventListener("click", function () {
        // Send a POST request to update the carbon footprint
        fetch('/update_footprint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                option: 'drive',
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Update the carbon footprint display
            carbonSpan.innerText = data.carbon_footprint;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
