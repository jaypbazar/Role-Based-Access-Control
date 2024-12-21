// Populate the select dropdown with available parking lots
var parkingSpaceDropdown = document.getElementById("parkingSpace");

// Filter and add available lots to the dropdown
var availableLots = parkingLots.filter(lot => lot.status === "available");

if (availableLots.length > 0) {
    availableLots.forEach(lot => {
        var option = document.createElement("option");
        option.value = lot.name;
        option.textContent = lot.name;
        parkingSpaceDropdown.appendChild(option);
    });
} 
else {
    // Add a "No available parking lot" option if none are available
    var noOption = document.createElement("option");
    noOption.textContent = "No available parking lots";
    noOption.disabled = true;
    noOption.selected = true;
    parkingSpaceDropdown.appendChild(noOption);
}