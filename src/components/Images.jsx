import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const apiAddress = '192.168.204.109:8000';

const Images = () => {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleFileChange = (event) => {
    setSelectedFiles(event.target.files);
  };

  const handleButtonClick = async () => {

    if (selectedFiles.length === 0) {
      alert('Please select images before submitting.');
      return;
    }

    setLoading(true);
    const formData = new FormData();
    for (let i = 0; i < selectedFiles.length; i++) {
      formData.append('image', selectedFiles[i]);
    }

    try {
      const response = await axios.post(`http://${apiAddress}/process2`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        withCredentials:true
      });
      console.log(response);
      navigate('/edit', { state: response.data });
      alert('Images uploaded successfully!');
    } catch (error) {
      console.error('Error uploading images:', error);
      alert('Failed to upload images.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center h-screen bg-gray-50 w-full">
      <div className="flex flex-col items-center md:flex-row bg-white shadow-xl rounded-lg overflow-hidden p-8 md:p-12 lg:p-16 max-w-5xl">
        <div className="flex-1 bg-gray-50 border border-gray-200 rounded-lg p-6 mt-8 md:mt-0 shadow-inner relative">
          <h2 className="text-2xl font-semibold text-gray-800 mb-6">Upload Slot Images</h2>
          <div className="mb-4">
            <input
              type="file"
              multiple
              accept="image/*"
              onChange={handleFileChange}
              className="block w-full text-sm text-gray-500 
                     file:mr-4 file:py-2 file:px-4 
                     file:rounded-lg file:border-0
                     file:text-sm file:font-semibold
                     file:bg-blue-50 file:text-blue-500
                     hover:file:bg-blue-100"
            />
          </div>
          <button
            onClick={handleButtonClick}
            disabled={loading}
            className={`w-full py-2 px-4 rounded-lg font-semibold transition duration-200
            ${loading ? 'bg-charcoal cursor-not-allowed' : 'bg-persian hover:bg-charcoal'}
            text-white shadow-sm flex items-center justify-center`}
          >
            {loading ? (
              <>
                <svg className="animate-spin mr-2 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
                </svg>
                Uploading...
              </>
            ) : (
              'Submit'
            )}
          </button>
          <div className='h-10 relative'>
          {loading && (
              <p className="text-sm text-gray-500 absolute">
                This may take up to 5-6 minutes, please don't refresh the page.
              </p>
            )}
          </div>
            
          
        </div>
      </div>
    </div>
  );
};

export default Images;
