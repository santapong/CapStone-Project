import React from 'react';
import html2canvas from 'html2canvas';

const Export = ({ targetRef }) => {
  const handleScreenshot = () => {
    html2canvas(targetRef.current).then((canvas) => {
      const dataUrl = canvas.toDataURL(); // Get image URL
      const link = document.createElement('a');
      link.href = dataUrl;
      link.download = 'dashboard-screenshot.png';
      link.click(); // Trigger download
    });
  };

  return (
    <button
      onClick={handleScreenshot}
      className="btn"
    >
      Screenshot
    </button>
  );
};

export default Export;
