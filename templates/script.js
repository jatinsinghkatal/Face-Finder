// Get the form and button elements
const form = document.getElementById("upload-form");
const button = document.getElementById('submit-button');

// Prevent form submission and reload
button.addEventListener('click', async (event) => {
    event.preventDefault(); // Prevent any default action
    
    const fileInput = document.getElementById("image-file");
    const preview = document.getElementById("image-preview");
    const matchedImage = document.getElementById("matched-image");
    const resultDiv = document.getElementById("result");
    const progressContainer = document.getElementById("progress-container");
    const progressBar = document.getElementById("progress-bar");

    // Show "Finding a match..." message and reset matched image display
    resultDiv.innerHTML = "Finding a match..."; // Set initial message
    matchedImage.style.display = "none"; // Hide matched image initially

    // Show progress bar and reset it
    progressContainer.style.display = "block";
    progressBar.style.width = "0%";

    // Incrementally animate the progress bar
    let progress = 0;
    const interval = setInterval(() => {
        progress = Math.min(progress + 1, 90); // Keep it below 90% until response is received
        progressBar.style.width = progress + "%";
    }, 200);

    // Preview the uploaded image
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (event) {
            preview.src = event.target.result;
            preview.style.display = "block";  // Show preview
        };
        reader.readAsDataURL(file);
    }

    const formData = new FormData();
    formData.append("image", file);

    try {
        console.log("Uploading image...");

        // Send the image to the backend (Flask)
        const response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData,
        });

        // Stop progress animation
        clearInterval(interval);
        progressBar.style.width = "100%"; // Complete the progress bar

        // Handle server response
        const data = await response.json();
        console.log("Server Response:", data);  // Log the response from Flask

        // Update the result based on response
        if (response.ok) {
            if (data.matchFound) {
                resultDiv.innerHTML = `Match found: ${data.matchedImage}`;
                matchedImage.src = `http://127.0.0.1:5000${data.imageUrl}`;
                matchedImage.style.display = "block";
            } else {
                resultDiv.innerHTML = "No match found.";
                matchedImage.style.display = "none";
            }
        } else {
            resultDiv.innerHTML = `${data.error || data.message}`;
        }
    } catch (error) {
        console.error("Error during image upload:", error);
        resultDiv.innerHTML = "Error occurred during the upload.";
    } finally {
        // Hide progress bar after completion
        progressContainer.style.display = "none";
    }
});
