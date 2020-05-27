import React from "react";
import { Container, Row, Col } from "reactstrap";
import { Navbar, Nav, NavItem, NavLink } from "reactstrap";
import { Form, FormGroup, Input } from "reactstrap";

const SearchBar = (props) => {
  return (
    <header>
      <Navbar color="light" light expand="lg">
        <Container>
          <Row>
            <Nav className="mr-auto" navbar>
              <NavItem className="active">
                <NavLink href="#">Default : Attractions </NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="#"> Last selected : Hotels</NavLink>
              </NavItem>
            </Nav>
          </Row>
          <Row className="w-50">
            <Nav className="ml-auto w-100" navbar>
              <Row className="w-100">
                <Col className="p-0">
                  <Form className="form-inline w-100 my-2 my-lg-0">
                    <FormGroup className="m-0 w-75 ml-auto">
                      <Input
                        type="text"
                        name=""
                        className="w-100"
                        id=""
                        placeholder="Search nearby"
                      />
                    </FormGroup>
                  </Form>
                </Col>
                <Col lg="4">
                  <div className="border-left pt-2 pl-2 pr-0">
                    Try a random place
                  </div>
                </Col>
              </Row>
            </Nav>
          </Row>
        </Container>
      </Navbar>
    </header>
  );
};

export default SearchBar;
