document.addEventListener("DOMContentLoaded", function () {
    const driveButton = document.getElementById("drive");
    const carbonSpan = document.getElementById("carbon");

    // Initialize the carbon footprint value
    let carbonFootprint = 0;

    // Add event listeners for the game options
    driveButton.addEventListener("click", function () {
        // Update the carbon footprint
        carbonFootprint += 1; // Increment by 1 for demonstration purposes
        // Update the carbon footprint display
        carbonSpan.innerText = carbonFootprint;
    });
});
