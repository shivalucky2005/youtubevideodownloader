// Frontend: Sending video link to FastAPI backend
async function downloadVideo() {
    const videoLink = document.getElementById("videoLink").value; // Assuming there's an input field with id="videoLink"
    
    try {
        const response = await fetch("http://127.0.0.1:8000/download", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ link: videoLink }),
        });

        if (response.ok) {
            const data = await response.json();
            alert(data.message);
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        alert(`An unexpected error occurred: ${error.message}`);
    }
}
  