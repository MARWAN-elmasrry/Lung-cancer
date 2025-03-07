const results = document.getElementById("results");
const lung_img = document.getElementById("lung-img");
const animated_background = document.querySelector(".animated-background");
const lungPaths = document.querySelectorAll(".lung path"); 
const bronchi = document.querySelector(".bronchi"); 
const CheckBtn = document.getElementById("CheckBtn")

const test = () => {
    console.log("clicked")    

     // Get Age first
    let age = parseInt(document.querySelector('input[name="Age"]').value, 10) || 0;

    let gender = document.querySelector('select[name="Gender"]').value

    // Now include Gender and Age in the features array
    let features = [gender, age]; 

    // Add Checkbox values (Convert to 1 or 2)
    document.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
        features.push(checkbox.checked ? 2 : 1);
        console.log(features)
    });



    // Send Data to Backend
    fetch("http://127.0.0.1:4000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ features }), // Correct format
    })
    .then(response => response.json())
    .then(result => {
        // Display Prediction
        document.getElementById("results").innerText = `Prediction: ${result.message}`;

        // Handle UI Changes Based on Result
        if (result.lung_cancer === 1) { // Assuming 1 means lung cancer
            animated_background.style = "background: linear-gradient(45deg, #ff9999, #ff6666, #ff3333, rgb(194, 46, 46)); background-size: 300% 300%; animation: gradientAnimation 8s ease infinite;";
            results.style = "font-size: 30px; color:white;";
            results.innerHTML = "Sorry, you have Lung Cancer";
            lung_img.src = "./imgs/bad.png";

            lungPaths.forEach(path => {
                path.setAttribute("fill", "#FF6666"); 
                path.setAttribute("stroke", "#CC0000"); 
            });

            bronchi.setAttribute("stroke", "#990000");

            CheckBtn.style.background = "#CC0000";
            CheckBtn.style.color = "#FFFFFF"; 
            CheckBtn.style.border = "2px solid #990000";
            CheckBtn.innerHTML = "Another Check";
        } else {
            results.style = "font-size: 30px; color:black;";
            results.innerHTML = "You don't have Lung Cancer";
            lung_img.src = "./imgs/good.png";
        }
    })
    .catch(error => console.error("Error:", error.message));
    
}