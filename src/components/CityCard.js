import React from "react";
import { Card, CardBody,CardHeader,CardFooter,Row,Col } from "reactstrap";

const CityCard = () => {

  const getYear = () => {
    return new Date().getFullYear();
}
  return (
    <Card className="border-0 shadow locationCard">
      <CardHeader className='border-0'>
        <Row>
          <Col className='col-8 p-3'>
          <h3 className='text-white'>Welcome User <br /> Dave</h3>
          </Col>
          <i className="fa fa-user text-white float-left userIcon" style={{fontSize:65}}></i>

          {/* <img src={weather.icon} className='weatherIcon' alt='weather'  /> */}

        </Row>
      </CardHeader>
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
                  <p>
                    Featured hotels:
                    <br />
                    <span className="badge badge-dark">Hotel 3</span>
                    <span className="badge badge-dark">Hotel 2</span>
                    <span className="badge badge-dark">Hotel 1</span>
                  </p>
                  <p>
                    Attractions:
                    <br />
                    <span className="badge badge-dark">Attraction 3</span>
                    <span className="badge badge-dark">Attraction 2</span>
                    <span className="badge badge-dark">Attraction 1</span>
                  </p>
                  <p className='p-0 m-0'>
                    Try a random place >
                   
                  </p>
                </CardBody>
                <CardFooter className='border-0'>
          <p className='text-white pl-2 pt-1 pb-0 m-0'>© {getYear()} TravellingDiaries, Inc.</p>
      </CardFooter>
              </Card>
  );
};

export default CityCard;
