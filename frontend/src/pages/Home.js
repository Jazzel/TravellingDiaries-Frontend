import React from "react";
import Navigation from "../containers/Navigation";
import SearchBar from "../containers/SearchBar";
import MenuButton from "../components/MenuButton";
import "./Home.css";
import { Card, CardHeader, CardBody, CardImg } from "reactstrap";
import { Row, Col } from "reactstrap";
import PostForm from "../components/PostForm";
import WeatherCard from "../components/WeatherCard";

const Home = () => {
  return (
    <React.Fragment>
      <Navigation />
      <SearchBar />
      <Card className="border-0">
        <CardHeader className="headImage"></CardHeader>
        <CardBody className="headCard w-100">
          <Row>
            <Col className="col-3">
              <Card className="border-0 shadow locationCard">
                <CardImg
                  top
                  src={
                    "http://openweathermap.org/themes/openweathermap/assets/vendor/owm/img/widgets/02n.png"
                  }
                  style={{ zIndex: -1 }}
                />
                <CardBody className="bg-light">
                  <h4 className="card-title">
                    <p>
                      <i className="fa fa-map-marker-alt float-left"></i>
                      &nbsp; Karachi, Sindh, Pakistan
                    </p>
                  </h4>
                  <p>
                    Featured destinations:
                    <br />
                    <span className="badge badge-dark">Destination 3</span>
                    <span className="badge badge-dark">Destination 2</span>
                    <span className="badge badge-dark">Destination 1</span>
                  </p>
                </CardBody>
              </Card>
            </Col>
            <Col className="col-6">
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
            <Col className="col-3">
              <WeatherCard />
            </Col>
          </Row>
        </CardBody>
      </Card>
    </React.Fragment>
  );
};

export default Home;
