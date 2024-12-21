// Coordinates of your campus
var campusLat = 13.406040212295862;
var campusLon = 123.37548833100324;

// Initialize the map
var map = L.map('campusMap').setView([13.405517911030056, 123.37713024219663], 19);

// Tile layer using OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    minZoom: 18,
    maxZoom: 21,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Add parking lot rectangles
parkingLots.forEach(lot => {
    var color;
    if (lot.status === "available") {
        color = "#34ff12"; // Green for available
    } else if (lot.status === "reserved") {
        color = "#7db7ff"; // Blue for reserved
    } else if (lot.status === "occupied") {
        color = "#ff5858"; // Red for occupied
    }
    
    // Add the rectangle to the map
    L.rectangle(lot.coords, { color: color, weight: 1 }).addTo(map)
        .bindPopup(`${lot.name}: ${lot.status.charAt(0).toUpperCase() + lot.status.slice(1)}`);
});