const vehiclesContainer = document.getElementById("vehicles");
const vehicleList = document.getElementById("vehicleList");
const activeCount = document.getElementById("activeCount");

const vehicleTypes = [
    { type: "bus", name: "Bus", icon: "🚌", count: 7 },
    { type: "mini", name: "Minibus", icon: "🚐", count: 3 },
    { type: "truck", name: "Truck", icon: "🚛", count: 2 },
    { type: "motor", name: "Motorcycle", icon: "🏍️", count: 3 },
    { type: "car", name: "Home Car", icon: "🚙", count: 4 }
];

const vehicles = [];

let id = 1;

// Create 19 simulated vehicles
vehicleTypes.forEach(group => {

    for (let i = 0; i < group.count; i++) {

        const vehicle = {
            id: id++,
            type: group.type,
            name: group.name,
            icon: group.icon,

            // Random starting position
            x: 10 + Math.random() * 75,
            y: 10 + Math.random() * 75,

            // Random direction
            dx: (Math.random() - 0.5) * 0.08,
            dy: (Math.random() - 0.5) * 0.08,

            speed: 0.03 + Math.random() * 0.05
        };

        vehicles.push(vehicle);

        createVehicleMarker(vehicle);
        createVehicleList(vehicle);
    }
});


// ------------------------------------
// CREATE MAP VEHICLE
// ------------------------------------

function createVehicleMarker(vehicle) {

    const marker = document.createElement("div");

    marker.className = `vehicle ${vehicle.type}`;

    marker.id = `vehicle-${vehicle.id}`;

    marker.textContent = vehicle.icon;

    marker.title =
        `${vehicle.name} ${vehicle.id} — Simulated GPS`;

    vehiclesContainer.appendChild(marker);

    vehicle.marker = marker;
}


// ------------------------------------
// CREATE VEHICLE LIST
// ------------------------------------

function createVehicleList(vehicle) {

    const item = document.createElement("div");

    item.className = "vehicle-item";

    item.innerHTML = `
        <div class="vehicle-icon">${vehicle.icon}</div>

        <div class="vehicle-info">
            <strong>${vehicle.name} ${vehicle.id}</strong>
            <small>
                GPS • Moving
            </small>
        </div>
    `;

    vehicleList.appendChild(item);
}


// ------------------------------------
// MOVE VEHICLES
// ------------------------------------

function moveVehicles() {

    const map = document.querySelector(".map-container");

    if (!map) return;

    vehicles.forEach(vehicle => {

        vehicle.x += vehicle.dx * vehicle.speed * 10;
        vehicle.y += vehicle.dy * vehicle.speed * 10;

        // Bounce from map edges
        if (vehicle.x < 3 || vehicle.x > 94) {
            vehicle.dx *= -1;
        }

        if (vehicle.y < 3 || vehicle.y > 94) {
            vehicle.dy *= -1;
        }

        // Keep inside map
        vehicle.x = Math.max(3, Math.min(94, vehicle.x));
        vehicle.y = Math.max(3, Math.min(94, vehicle.y));

        vehicle.marker.style.left = `${vehicle.x}%`;
        vehicle.marker.style.top = `${vehicle.y}%`;
    });
}


// ------------------------------------
// INITIAL POSITION
// ------------------------------------

vehicles.forEach(vehicle => {

    vehicle.marker.style.left = `${vehicle.x}%`;
    vehicle.marker.style.top = `${vehicle.y}%`;
});


// ------------------------------------
// START GPS SIMULATION
// ------------------------------------

setInterval(moveVehicles, 100);


// ------------------------------------
// UPDATE ACTIVE COUNT
// ------------------------------------

activeCount.textContent = `${vehicles.length} Active`;


// ------------------------------------
// CONSOLE INFORMATION
// ------------------------------------

console.log("GUZO PLUS simulated GPS started.");
console.log(`Total simulated vehicles: ${vehicles.length}`);
console.log("Buses: 7");
console.log("Minibuses: 3");
console.log("Trucks: 2");
console.log("Motorcycles: 3");
console.log("Home Cars: 4");
