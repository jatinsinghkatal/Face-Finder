
const form = document.getElementById("upload-form");

        form.addEventListener("submit", async function (e) {
            e.preventDefault();  // Prevent the form from submitting the traditional way

            const formData = new FormData();
            formData.append("image", document.getElementById("image-file").files[0]);

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
                        document.getElementById("result").innerHTML = `Match found: ${data.matchedImage}`;
                    } else {
                        document.getElementById("result").innerHTML = "No match found.";
                    }
                } else {
                    document.getElementById("result").innerHTML = `Error: ${data.error || data.message}`;
                }
            } catch (error) {
                console.error("Error during image upload:", error);
                document.getElementById("result").innerHTML = "Error occurred during the upload.";
            }
        });