import React from "react";
import Navigation from "../components/Navigation";
import SearchBar from "../components/SearchBar";
import MenuButton from "../components/MenuButton";
import "./Home.css";
import { Card, CardHeader, CardBody, CardImg } from "reactstrap";
import { Row, Col } from "reactstrap";
import PostForm from "../components/PostForm";
import WeatherCard from "../components/WeatherCard";
import CityCard from "../components/CityCard";

const Home = () => {
  return (
    <React.Fragment>
      <Navigation />
      <SearchBar />
      <Card className="border-0">
        <CardHeader className="headImage"></CardHeader>
        <CardBody className="headCard w-100">
          <Row>
            <Col className="col-lg-3 col-md-6 d-none d-sm-none d-md-block">
              <CityCard />
            </Col>
            <Col className="col d-md-none d-lg-block">
              <MenuButton />
              <br />
              <br />
              <PostForm />
              <div className="container-fluid p-0 m-0">
                <h2 className="mt-5 ml-3">Selected: Attractions ........</h2>
                <hr />
                <h2 className="mt-5 ml-3">Trending near you ........</h2>
                <hr />
                <div className="p-0" id="post-section"></div>
              </div>
            </Col>
            <Col className="col-lg-3 col-md-6 d-none d-sm-none d-md-block">
              <WeatherCard />
            </Col>
          </Row>
          <Row className='d-none d-md-block d-lg-none'>
            <br />
            <br />
          <Col className="col">
              <PostForm />
              <div className="container-fluid p-0 m-0">
                <h2 className="mt-5 ml-3">Selected: Attractions ........</h2>
                <hr />
                <h2 className="mt-5 ml-3">Trending near you ........</h2>
                <hr />
                <div className="p-0" id="post-section"></div>
              </div>
            </Col>
          </Row>
        </CardBody>
      </Card>
    </React.Fragment>
  );
};

export default Home;
