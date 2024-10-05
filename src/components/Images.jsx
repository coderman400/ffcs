import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const apiAddress = 'ffcs.onrender.com';

const Images = () => {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [credits, setCredits] = useState('');
  const [creditsError, setCreditsError] = useState('');
  const [timing, setTiming] = useState('morning');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleFileChange = (event) => {
    setSelectedFiles(event.target.files);
  };

  const handleCreditsChange = (event) => {
    setCredits(event.target.value);
  };
  const handleTimingChange = (event) => {
    setTiming(event.target.value);
  };

  const handleButtonClick = async () => {
    const creditsValue = parseInt(credits, 10);
    if (creditsValue < 16 || creditsValue > 27 || isNaN(creditsValue)) {
      setCreditsError('Credits value must be between 16 and 27.');
      return;
    }

    if (selectedFiles.length === 0) {
      alert('Please select images before submitting.');
      return;
    }

    setLoading(true);
    setCreditsError('');

    const formData = new FormData();

    formData.append('credits', creditsValue);
    formData.append('timing', timing);

    for (let i = 0; i < selectedFiles.length; i++) {
      formData.append('image', selectedFiles[i]);
    }

    try {
      const response = await axios.post(`https://${apiAddress}/process`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response.data);
      navigate('/result', { state: response.data });
      alert('Images uploaded successfully!');
    } catch (error) {
      console.error('Error uploading images:', error);
      alert('Failed to upload images.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center h-screen bg-gray-50">
      <div className="flex flex-col md:flex-row bg-white shadow-xl rounded-lg overflow-hidden p-8 md:p-12 lg:p-16 max-w-5xl">
        <div className="flex-1 p-4">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">Timetable Preference</h2>
          <form className="space-y-4">
            <div>
              <label htmlFor="credits" className="block text-gray-600 font-medium mb-1">
                Credits:
              </label>
              <input
                type="number"
                value={credits}
                onChange={handleCreditsChange}
                id="credits"
                className={`w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 
                ${creditsError ? 'border-red-500' : 'border-gray-300'}`}
                placeholder="Enter credits (16 - 27)"
              />
              {creditsError && (
                <p className="text-red-500 text-sm mt-1">{creditsError}</p>
              )}
            </div>
            <div>
              <label htmlFor="time" className="block text-gray-600 font-medium mb-1">
                Preferred Timing:
              </label>
              <select
                id="time"
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
                onChange={handleTimingChange}
              >
                <option value="morning">Morning</option>
                <option value="afternoon">Afternoon</option>
              </select>
            </div>
          </form>
        </div>

        <div className="flex-1 bg-gray-50 border border-gray-200 rounded-lg p-6 md:ml-8 mt-8 md:mt-0 shadow-inner relative">
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
                     file:bg-blue-50 file:text-blue-700
                     hover:file:bg-blue-100"
            />
          </div>
          <button
            onClick={handleButtonClick}
            disabled={loading}
            className={`w-full py-2 px-4 rounded-lg font-semibold transition duration-200
            ${loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 hover:bg-blue-600'}
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
          {loading && (
            <p className="absolute bottom-4 left-4 text-sm text-gray-500">
              This may take up to 5-6 minutes, please don't refresh the page.
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Images;
