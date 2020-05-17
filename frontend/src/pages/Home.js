import React from "react";
import Navigation from "../containers/Navigation";
import SearchBar from "../containers/SearchBar";

const Home = () => {
  return (
    <React.Fragment>
      <Navigation />
      <SearchBar />
    </React.Fragment>
  );
};

export default Home;
