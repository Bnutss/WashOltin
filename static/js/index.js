function updateDateTime() {
    const currentDate = new Date();
    document.getElementById("current-date").textContent = currentDate.toLocaleDateString();
    document.getElementById("current-time").textContent = currentDate.toLocaleTimeString();
}

setInterval(updateDateTime, 1000);
updateDateTime();