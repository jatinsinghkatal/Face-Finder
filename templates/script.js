const form = document.getElementById("upload-form");

form.addEventListener("submit", async function (e) {
    e.preventDefault();  // Prevent the form from submitting the traditional way

    const fileInput = document.getElementById("image-file");
    const preview = document.getElementById("image-preview");
    const matchedImage = document.getElementById("matched-image");
    const resultDiv = document.getElementById("result");

    // Preview the uploaded image
    const file = fileInput.files[0];
    const reader = new FileReader();
    reader.onload = function (event) {
        preview.src = event.target.result;
        preview.style.display = "block";  // Show preview
        matchedImage.style.display = "none";  // Hide matched image initially
        resultDiv.innerHTML = "";  // Reset result
    };
    reader.readAsDataURL(file);

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    try {
        console.log("Uploading image...");

        // Send the image to the backend (Flask)
        const response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData,
        });

        // Handle server response
        const data = await response.json();
        console.log("Server Response:", data);  // Log the response from Flask

        // If the upload is successful, display the result
        if (response.ok) {
            if (data.matchFound) {
                resultDiv.innerHTML = `Match found: ${data.matchedImage}`;
                
                // Display the matched image
                matchedImage.src = `http://127.0.0.1:5000${data.imageUrl}`;
                matchedImage.style.display = "block"; // Show the matched image
            } else {
                resultDiv.innerHTML = "No match found.";
                matchedImage.style.display = "none"; // Hide the matched image if no match
            }
        } else {
            resultDiv.innerHTML = `Error: ${data.error || data.message}`;
        }
    } catch (error) {
        console.error("Error during image upload:", error);
        resultDiv.innerHTML = "Error occurred during the upload.";
    }
});
