import React from "react";
import { Card, Row, Col, Form, Input } from "reactstrap";

const PostForm = () => {
  return (
    <Card style={{ zIndex: 99 }}>
      <div className="w-100">
        <Row className="p-3">
          <Col className="col-1">
            <img
              className="rounded-circle"
              width="50"
              src="./../../public/assets/images/pp.jpeg"
              alt="user"
            />
          </Col>
          <Col className="col ml-1">
            <Form>
              <Input
                className="form-control m-0 w-100"
                style={{ fontSize: 25 }}
                type="text"
                placeholder="What's up ? Jazz"
              />
            </Form>
          </Col>
        </Row>
        <Row className="p-3 text-center">
          <Col>
            <i
              className="text-primary fas fa-user-friends"
              aria-hidden="true"
            ></i>{" "}
            &nbsp; Tag Someone
          </Col>
          <Col>
            <i
              className="text-primary fas fa-user-friends"
              aria-hidden="true"
            ></i>{" "}
            &nbsp; Tag Someone
          </Col>
          <Col>
            <i
              className="text-primary fas fa-user-friends"
              aria-hidden="true"
            ></i>{" "}
            &nbsp; Tag Someone
          </Col>
        </Row>
      </div>
    </Card>
  );
};

export default PostForm;
