import React from "react";

const MenuButton = () => {
  return (
    <div className="component">
      <button className="cn-button" id="cn-button">
        <i className="fa fa-align-center" aria-hidden="true"></i>
      </button>
      <div className="cn-wrapper" id="cn-wrapper">
        <ul>
          <li>
            <a href="/">
              <p className="mt-2">
                <i className="fa fa-hotel" aria-hidden="true"></i>
                <span>Hotels</span>
              </p>
            </a>
          </li>
          <li>
            <a href="/">
              <p className="mt-2">
                <i className="fa fa-utensils" aria-hidden="true"></i>
                <span>DineIns</span>
              </p>
            </a>
          </li>
          <li>
            <a href="/">
              <p className="mt-2">
                <i className="fa fa-plane-departure" aria-hidden="true"></i>
                <span>Flights</span>
              </p>
            </a>
          </li>
          <li>
            <a href="/">
              <p className="mt-2">
                <i className="fa fa-train" aria-hidden="true"></i>
                <span>Trains</span>
              </p>
            </a>
          </li>
          <li>
            <a href="/">
              <p className="mt-2">
                <i className="fa fa-bus" aria-hidden="true"></i>
                <span>Buses</span>
              </p>
            </a>
          </li>
          <li>
            <a href="/">
              <p className="mt-2">
                <i className="fa fa-home" aria-hidden="true"></i>
                <span>Rentals</span>
              </p>
            </a>
          </li>
          <li>
            <a href="/">
              <p className="mt-2">
                <i className="fa fa-plus" aria-hidden="true"></i>
                <span>More</span>
              </p>
            </a>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default MenuButton;
