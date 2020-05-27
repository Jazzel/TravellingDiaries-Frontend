import React, { useEffect, useState } from "react";
import { Card, CardBody, CardImg } from "reactstrap";

const WeatherCard = () => {
  const [weather, setWeather] = useState([]);

  useEffect(() => {
    const fetchWeatherData = async () => {
      const city = "Karachi";
      const response = await fetch(
        "http://api.openweathermap.org/data/2.5/weather?q=" +
          city +
          "&units=metric&appid=ab1511265be0e3512b8a68c06a71358f"
      );
      const __response = await fetch(
        "http://dataservice.accuweather.com/forecasts/v1/daily/5day/261158?apikey=sMXa6WnLgzFCBq8HQ7TCAwa0aVah0q7U&details=true"
      );
      const __responseData = await __response.json();

      console.log(__responseData);
      // const responseData = await response.json();
      // const weatherData = {
      //   city: city,
      //   temperature: responseData["main"]["temp"],
      //   description: responseData["weather"][0]["description"],
      //   icon: responseData["weather"][0]["icon"],
      // };
      // setWeather(weatherData);
    };
    fetchWeatherData();
  }, []);

  return (
    <Card className="border-0 shadow weatherCard">
      <CardImg
        top
        src={
          "http://openweathermap.org/themes/openweathermap/assets/vendor/owm/img/widgets/" +
          weather.icon +
          ".png"
        }
        style={{ zIndex: -1 }}
      />
      <CardBody className="bg-light">
        <h4 className="card-title">
          <p>
            <img src="http://openweathermap.org/img/w/02n.png" alt="Image" />
            <img src="https://www.accuweather.com/images/weathericons/01n.png"  alt="Image" />
            &nbsp; Weather - {weather.temperature}° C
          </p>
        </h4>
        <hr />
        <p style={{ textTransform: "capitalize" }}>
          {weather.description} - Good Evening !!
        </p>
      </CardBody>
    </Card>
  );
};

export default WeatherCard;
