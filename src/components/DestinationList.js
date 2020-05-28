import React from "react";
import backendServer from '../api/travellingdiaries';

const DestinationList = () => {
    const fetchDestinations = async () => {
    const response = await backendServer.get('/destinations/');
    console.log(response.data);
    };
    fetchDestinations();
  return (
      <div></div>
  );
};

export default DestinationList;
