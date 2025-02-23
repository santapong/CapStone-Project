import React, { useState, useEffect } from "react";

function Manage() {
  const [data, setData] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [startPage, setStartPage] = useState("");
  const [finalPage, setFinalPage] = useState("");
  const [loading, setLoading] = useState(false); // Loading state for upload
  const [deleteLoading, setDeleteLoading] = useState(false); // Loading state for delete
  const [documentToDelete, setDocumentToDelete] = useState(null); // Track document to delete

  useEffect(() => {
    fetch("/document/documents")
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((error) => console.error("Error fetching documents:", error));
  }, []);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setStartPage("");
    setFinalPage("");
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a file.");
      return;
    }

    const start = parseInt(startPage, 10);
    const end = parseInt(finalPage, 10);

    if (isNaN(start) || isNaN(end) || start < 1 || end < start) {
      alert("Invalid page range!");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);
    formData.append("data", JSON.stringify({ start_page: start, final_page: end }));

    setLoading(true);

    try {
      const response = await fetch("/document/uploadfile", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const newDocument = await response.json();
        setData([...data, newDocument]);
        document.getElementById("upload-modal").close();
        setSelectedFile(null);
        setStartPage("");
        setFinalPage("");
      } else {
        console.error("Failed to upload document");
      }
    } catch (error) {
      console.error("Error uploading document:", error);
    } finally {
      setLoading(false);
    }
  };

  const confirmDelete = (doc) => {
    setDocumentToDelete(doc);
    document.getElementById("delete-modal").showModal();
  };

  const handleDelete = async () => {
    if (!documentToDelete) return;

    setDeleteLoading(true);

    try {
      const response = await fetch(`/document/delete/${documentToDelete.id}`, {
        method: "DELETE",
      });

      if (response.ok) {
        setData(data.filter((doc) => doc.id !== documentToDelete.id));
        document.getElementById("delete-modal").close();
      } else {
        console.error("Failed to delete document");
      }
    } catch (error) {
      console.error("Error deleting document:", error);
    } finally {
      setDeleteLoading(false);
      setDocumentToDelete(null);
    }
  };

  return (
    <div className="min-h-screen bg-gray-500 flex items-center justify-center">
      <div className="p-6 bg-gray-800 w-[500px] rounded-lg">
        <div className="flex justify-between mb-4">
          <h2 className="text-white text-lg">Manage Documents</h2>
          <button
            className="btn btn-primary"
            onClick={() => document.getElementById("upload-modal").showModal()}
            disabled={loading || deleteLoading} // Disable when uploading or deleting
          >
            Add
          </button>
        </div>
        <table className="table w-full text-white">
          <thead>
            <tr>
              <th className="px-2 py-1 border-b">Document Name</th>
              <th className="px-2 py-1 border-b">Pages</th>
              <th className="px-2 py-1 border-b">Upload At</th>
              <th className="px-2 py-1 border-b">Actions</th>
            </tr>
          </thead>
          <tbody>
            {data.map((row) => (
              <tr key={row.id}>
                <td className="px-2 py-1 border-b">{row.document_name}</td>
                <td className="px-2 py-1 border-b">{row.pages}</td>
                <td className="px-2 py-1 border-b">{row.upload_at}</td>
                <td className="px-2 py-1 border-b">
                  <button
                    className="btn btn-error btn-sm"
                    onClick={() => confirmDelete(row)}
                    disabled={loading || deleteLoading} // Disable during loading
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Upload Modal */}
      <dialog id="upload-modal" className="modal">
        <div className="modal-box">
          <h3 className="text-lg font-semibold">Upload PDF File</h3>
          <input
            type="file"
            accept="application/pdf"
            onChange={handleFileChange}
            className="file-input w-full my-4"
            disabled={loading}
          />

          <div className="flex space-x-4">
            <div className="w-1/2">
              <label className="block">Start Page:</label>
              <input
                type="text"
                className="input input-bordered w-full"
                value={startPage}
                onChange={(e) => setStartPage(e.target.value.replace(/\D/, ""))}
                placeholder="Enter start page"
                disabled={loading}
              />
            </div>
            <div className="w-1/2">
              <label className="block">Final Page:</label>
              <input
                type="text"
                className="input input-bordered w-full"
                value={finalPage}
                onChange={(e) => setFinalPage(e.target.value.replace(/\D/, ""))}
                placeholder="Enter final page"
                disabled={loading}
              />
            </div>
          </div>

          <div className="modal-action">
            <button
              className="btn"
              onClick={() => document.getElementById("upload-modal").close()}
              disabled={loading}
            >
              Cancel
            </button>
            <button className="btn btn-primary" onClick={handleUpload} disabled={loading}>
              {loading ? "Uploading..." : "Upload"}
            </button>
          </div>
        </div>
      </dialog>

      {/* Delete Confirmation Modal */}
      <dialog id="delete-modal" className="modal">
        <div className="modal-box">
          <h3 className="text-lg font-semibold text-red-500">Confirm Delete</h3>
          <p>Are you sure you want to delete <strong>{documentToDelete?.document_name}</strong>?</p>
          
          <div className="modal-action">
            <button
              className="btn"
              onClick={() => document.getElementById("delete-modal").close()}
              disabled={deleteLoading}
            >
              Cancel
            </button>
            <button className="btn btn-error" onClick={handleDelete} disabled={deleteLoading}>
              {deleteLoading ? "Deleting..." : "Delete"}
            </button>
          </div>
        </div>
      </dialog>
    </div>
  );
}

export default Manage;
