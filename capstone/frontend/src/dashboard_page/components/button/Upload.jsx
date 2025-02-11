import React, { useState } from "react";

const Upload = () => {
 // State to store the selected file
 const [selectedFile, setSelectedFile] = useState(null);

 // Handle file input change
 const handleFileChange = (event) => {
   const file = event.target.files[0];  // Get the selected file
   if (file && file.type === "application/pdf") {
     setSelectedFile(file);  // Update the state with the selected file
   } else {
     alert("Please select a valid PDF file.");
   }
 };

 // Optional: Handle form submission or file upload logic
 const handleSubmit = () => {
   if (selectedFile) {
     console.log("Selected file:", selectedFile);
     // Here you can handle the file upload to the server or other logic
   } else {
     alert("No file selected.");
   }
 };

 // Send file to Backend
 const handleFileUpload = async () => {
  if (selectedFile) {
    const formData = new FormData();
    formData.append("document", selectedFile);  // Append the file

    try {
      const response = await fetch("http://localhost:8000/document", {
        method: "POST",
        body: formData,  // Send the FormData with the file
      });

      if (response.ok) {
        alert("File uploaded successfully!");
      } else {
        alert("Failed to upload file.");
      }
    } catch (error) {
      alert("An error occurred while uploading the file.");
    }
  } else {
    alert("No file selected.");
  }
};

  return (
    <>
  <button className="btn" onClick={()=>document.getElementById('Upload').showModal()}>Upload Document</button>
  <dialog id="Upload" className="modal">
    <div className="modal-box">
      <h3 className="font-bold text-3xl text-white">Upload Document</h3>
      <input 
        id="UploadFIleInput"
        type="file"
        accept="application/pdf"
        onChange={handleFileChange}
        className="file-input file-input-bordered w-full max-w-xs mt-4 text-white bg-black"   
      />
      <button className="btn" onClick={handleFileUpload}>test</button>
      {/* <p className="py-4 text-white">Press ESC key or click outside to close</p> */}
    </div>
    <form method="dialog" className="modal-backdrop">
      <button>close</button>
    </form>
  </dialog>
    </>
  );
};

export default Upload;
