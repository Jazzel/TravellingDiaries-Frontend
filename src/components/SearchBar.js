import React from "react";
import { Container, Row, Col } from "reactstrap";
import { Navbar, Nav, NavItem, NavLink } from "reactstrap";
import { Form, FormGroup, Input } from "reactstrap";

const SearchBar = (props) => {
  return (
    <header>
      <Navbar className='d-none d-sm-none d-md-block' color="light" light expand="lg">
        <Container>
          <Row className='w-100 p-0 m-0'>
            <Col className='col-6'>
            <Nav className="mr-auto" navbar>
              <NavItem className="active">
                <NavLink href="#">Default : Attractions </NavLink>
              </NavItem>
              <NavItem>
                <NavLink href="#"> Last selected : Hotels</NavLink>
              </NavItem>
            </Nav>
            </Col>
            <Col className='col-6'>
            <Nav className="ml-auto w-100 pt-1" navbar>
              <Row className='w-100'>
                <Col className='col-md-12' >
                  <Form className="form-inline float-left w-100 my-2 my-lg-0">
                    <FormGroup className="m-0 w-100 pt-0">
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
              </Row>
            </Nav>
            </Col>
          </Row>
        </Container>
      </Navbar>
    </header>
  );
};

export default SearchBar;
