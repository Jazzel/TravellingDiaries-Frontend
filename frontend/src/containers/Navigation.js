import React from "react";
import { Row, Col } from "reactstrap";
import { Navbar, NavbarBrand, Nav, NavItem, NavLink } from "reactstrap";

const Navigation = (props) => {
  return (
    <header>
      <Navbar color="light" light expand="lg">
        <Row className="w-100">
          <Col lg="4">
            <Nav className="mr-auto w-100" navbar>
              <NavItem>
                <NavLink href="/components/">New</NavLink>
              </NavItem>
            </Nav>
          </Col>
          <Col lg="4">
            <NavbarBrand className="w-100  text-center" href="/">
              <h3 className="styled-font">TravellingDiaries</h3>
            </NavbarBrand>
          </Col>
          <Col lg="4">
            <Nav className="ml-auto float-right w-100" navbar>
              <NavItem>
                <NavLink href="/components/"></NavLink>
              </NavItem>
            </Nav>
          </Col>
        </Row>
      </Navbar>
    </header>
  );
};

export default Navigation;
