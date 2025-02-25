import React, { useState, useEffect } from "react";

function Manage() {
  const [data, setData] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [startPage, setStartPage] = useState("");
  const [finalPage, setFinalPage] = useState("");
  const [sortConfig, setSortConfig] = useState({});
  const [loading, setLoading] = useState(false);
  const [deleteLoading, setDeleteLoading] = useState(false);
  const [documentToDelete, setDocumentToDelete] = useState(null);
  const API_URL = import.meta.env.VITE_API_URL
  const API_PORT = import.meta.env.VITE_API_PORT

  const fetchDocuments = async () => {
    try {
      const res = await fetch(`${API_URL}:${API_PORT}/document/documents`);
      const result = await res.json();
      let sortedData = Array.isArray(result.data) ? [...result.data] : [];

      Object.keys(sortConfig).forEach((column) => {
        const order = sortConfig[column];

        if (order !== "disabled") {
          sortedData.sort((a, b) => {
            const valA = a[column];
            const valB = b[column];

            if (typeof valA === "string" && typeof valB === "string") {
              return order === "asc" ? valA.localeCompare(valB) : valB.localeCompare(valA);
            } else {
              return order === "asc" ? valA - valB : valB - valA;
            }
          });
        }
      });

      setData(sortedData);
    } catch (error) {
      console.error("Error fetching documents:", error);
      setData([]);
    }
  };
  
  
  useEffect(() => {
    fetchDocuments();
  }, []);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setStartPage("");
    setFinalPage("");
  };

  const handleSort = (column) => {
    setSortConfig((prev) => {
      const currentOrder = prev[column] || "disabled";
      const newOrder = currentOrder === "disabled" ? "asc" : currentOrder === "asc" ? "desc" : "disabled";
      
      return { ...prev, [column]: newOrder };
    });
    fetchDocuments();
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
      const response = await fetch(`${API_URL}:${API_PORT}/document/document`, {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        await fetchDocuments(); // Fetch updated document list
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
      const response = await fetch(`${API_URL}:${API_PORT}/document/document`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ document_name: documentToDelete.document_name }), // Send document name
      });
  
      if (response.ok) {
        await fetchDocuments(); // Fetch updated document list
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
      <div className="p-6 bg-gray-800 w-[1250px] rounded-lg">
        <div className="flex justify-between mb-4">
          <h2 className="font-bold text-white text-lg">Manage Documents</h2>
          <button
            className="btn bg-blue-600"
            onClick={() => document.getElementById("upload-modal").showModal()}
            disabled={loading || deleteLoading}
          >
            Add
          </button>
        </div>
        <table className="table w-full text-white">
          <thead>
          <tr className="bg-gray-700 text-white">
          {["upload_time", "file_name", "file_size", "status"].map((column) => (
                <th key={column} className="cursor-pointer p-2" onClick={() => handleSort(column)}>
                  {column.replace("_", " ").toUpperCase()}{" "}
                  {sortConfig[column] === "asc"
                    ? "↑"
                    : sortConfig[column] === "desc"
                    ? "↓"
                    : "⏺"} {/* Use ⏺ for disabled */}
                </th>
              ))}
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
                    disabled={loading || deleteLoading}
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
          <h3 className="text-lg text-white font-semibold">Upload PDF File</h3>
          <input
            type="file"
            accept="application/pdf"
            onChange={handleFileChange}
            className="file-input text-white w-full my-4"
            disabled={loading}
          />

          <div className="flex space-x-4">
            <div className="w-1/2">
              <label className="block text-white">Start Page:</label>
              <input
                type="text"
                className="input text-white input-bordered w-full"
                value={startPage}
                onChange={(e) => setStartPage(e.target.value.replace(/\D/, ""))}
                placeholder="Enter start page"
                disabled={loading}
              />
            </div>
            <div className="w-1/2">
              <label className="block text-white">Final Page:</label>
              <input
                type="text"
                className="input text-white input-bordered w-full"
                value={finalPage}
                onChange={(e) => setFinalPage(e.target.value.replace(/\D/, ""))}
                placeholder="Enter final page"
                disabled={loading}
              />
            </div>
          </div>

          <div className="modal-action">
            <button
              className="btn bg-red-900"
              onClick={() => document.getElementById("upload-modal").close()}
              disabled={loading}
            >
              Cancel
            </button>
            <button className="btn bg-green-700" onClick={handleUpload} disabled={loading}>
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
