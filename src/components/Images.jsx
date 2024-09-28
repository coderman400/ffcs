import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
// Replace with your API address if you have one
const apiAddress = '192.168.57.109:8000';

const Images = () => {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // Handle file input changes  
  const handleFileChange = (event) => {
    setSelectedFiles(event.target.files);
  };

  // Handle the button click to send data
  const handleButtonClick = async () => {
    if (selectedFiles.length === 0) {
      alert('Please select images before submitting.');
      return;
    }

    setLoading(true);

    // Create a FormData object to hold the files
    const formData = new FormData();
    for (let i = 0; i < selectedFiles.length; i++) {
      formData.append('image', selectedFiles[i]);
    }

    try {
      const response = await axios.post(`http://${apiAddress}/process`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response.data);
      navigate('/result', {state: response.data})
      alert('Images uploaded successfully!');
    } catch (error) {
      console.error('Error uploading images:', error);
      alert('Failed to upload images.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="bg-white border-2 border-dashed border-gray-300 rounded-lg p-10 shadow-lg">
        <h2 className="text-xl font-semibold text-gray-700 mb-4">Upload Images</h2>
        <input
          type="file"
          multiple
          accept="image/*"
          onChange={handleFileChange}
          className="block w-full text-sm text-gray-500 
                     file:mr-4 file:py-2 file:px-4 
                     file:rounded-full file:border-0
                     file:text-sm file:font-semibold
                     file:bg-blue-50 file:text-blue-700
                     hover:file:bg-blue-100 mb-4"
        />
        <button
          onClick={handleButtonClick}
          disabled={loading} // Disable button during loading
          className={`w-full py-2 px-4 rounded font-semibold transition duration-200
            ${loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 hover:bg-blue-600'}
            text-white`}
        >
          {loading ? 'Uploading...' : 'Submit'}
        </button>
      </div>
    </div>
  );
};

export default Images;
