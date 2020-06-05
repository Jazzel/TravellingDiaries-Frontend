import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Redirect,
  Switch,
} from "react-router-dom";
import Home from "./pages/Home";
import HomePage from "./pages/Index";
import "./App.css";
import Login from "./pages/Login";
import Login1 from "./pages/Login1";

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact>
          <Home />
        </Route>
        <Route path="/home" exact>
          <HomePage />
        </Route>
        <Route path="/login" exact>
          <Login />
        </Route>
        <Route path="/logins" exact>
          <Login1 />
        </Route>
        <Redirect to="/" />
      </Switch>
    </Router>
  );
};

export default App;
