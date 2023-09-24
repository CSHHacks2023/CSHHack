document.addEventListener("DOMContentLoaded", function () {
    const carbonSpan = document.getElementById("carbon");

    const carbonCounter = document.querySelector(".carbon-counter");




    // Initialize the carbon footprint value
    let carbonFootprint = 0;
    function updateCarbonDisplay() {
        carbonSpan.innerText = carbonFootprint;
    }

    const ecoFriendlyStoreButton = document.querySelector(".button5");
    const driveButton = document.querySelector(".button6");

    const ecoFriendlyButton2= document.querySelector(".button7");
    const driveButton2 = document.querySelector(".button8");

    const ecoFriendlyButton3 = document.querySelector(".button9");
    const driveButton3 = document.querySelector(".button10");

    const ecoFriendlyButton4 = document.querySelector(".button11");
    const driveButton4 = document.querySelector(".button12");

    ecoFriendlyStoreButton.addEventListener("click", function () {
        carbonFootprint -= 1; // Decrement the carbon footprint
        updateCarbonDisplay();
    });

    driveButton.addEventListener("click", function () {
        carbonFootprint += 1; // Increment the carbon footprint
        updateCarbonDisplay();
    });

    ecoFriendlyButton2.addEventListener("click", function () {
        carbonFootprint -= 1; // Decrement the carbon footprint
        updateCarbonDisplay();
    });


    driveButton2.addEventListener("click", function () {
        carbonFootprint += 1; // Increment the carbon footprint
        updateCarbonDisplay();
    });

    ecoFriendlyButton3.addEventListener("click", function () {
        carbonFootprint -= 1; // Decrement the carbon footprint
        updateCarbonDisplay();
    });

    driveButton3.addEventListener("click", function () {
        carbonFootprint += 1; // Increment the carbon footprint
        updateCarbonDisplay();
    });

    ecoFriendlyButton4.addEventListener("click", function () {
        carbonFootprint -= 1; // Decrement the carbon footprint
        updateCarbonDisplay();
    });

    driveButton4.addEventListener("click", function () {
        carbonFootprint += 1; // Increment the carbon footprint
        updateCarbonDisplay();
    });

    function updateCarbonDisplay() {
        carbonSpan.innerText = carbonFootprint;

        // Check if carbonFootprint is 10 or more, and change background color
        if (carbonFootprint >= 10) {
            carbonCounter.style.backgroundColor = "#FF3333"; // Red color
        } else {
            carbonCounter.style.backgroundColor = ""; // Reset to default color
        }
    }
});
