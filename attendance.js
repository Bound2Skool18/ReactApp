function calculatePay() {
    // Fixed hourly rate
    const hourlyRate = 14.72;

    // Get input values
    const employeeName = document.getElementById("employeeName").value;
    const daysWorked = parseInt(document.getElementById("daysWorked").value);
    const clockIn = new Date("2000-01-01 " + document.getElementById("clockIn").value);
    const clockOut = new Date("2000-01-01 " + document.getElementById("clockOut").value);

    // Validate inputs
    if (employeeName.trim() === "") {
        alert("Please enter the employee's name.");
        return;
    }

    if (isNaN(daysWorked) || daysWorked < 1 || daysWorked > 5) {
        alert("Please enter a valid number of days worked (between 1 and 5).");
        return;
    }

    if (isNaN(clockIn.getTime()) || isNaN(clockOut.getTime())) {
        alert("Please enter valid clock-in and clock-out times.");
        return;
    }

    // Calculate hours worked
    const hoursWorked = (clockOut - clockIn) / (1000 * 60 * 60);

    // Calculate total pay
    const totalPay = hourlyRate * hoursWorked * daysWorked;

    // Display the result
    document.getElementById("result").innerHTML = `${employeeName}, Total Pay: $${totalPay.toFixed(2)}, Hours Worked: ${hoursWorked.toFixed(2)} hours`;

    // Calculate total weekly hours
    calculateWeeklyHours(daysWorked);
}

function calculateWeeklyHours(daysWorked) {
    // Default clock-in and clock-out times
    const defaultClockInTime = new Date("2000-01-01 09:00");
    const defaultClockOutTime = new Date("2000-01-01 17:00");

    // Calculate total weekly hours based on days worked
    let totalWeeklyHours = 0;
    for (let i = 1; i <= daysWorked; i++) {
        const clockIn = new Date(defaultClockInTime);
        const clockOut = new Date(defaultClockOutTime);
        totalWeeklyHours += (clockOut - clockIn) / (1000 * 60 * 60);
    }

    // Display the total weekly hours
    document.getElementById("result").innerHTML += `<br>Total Weekly Hours: ${totalWeeklyHours.toFixed(2)} hours`;
}
