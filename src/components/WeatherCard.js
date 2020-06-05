import React, { useEffect, useState } from "react";
import { Card,CardHeader, CardBody, Row, Col, CardFooter } from "reactstrap";

const WeatherCard = () => {
  const [weather, setWeather] = useState([]);

  useEffect(() => {
    const hours = new Date().getHours();
    const isDayTime = hours > 6 && hours < 20;
    let time = '';

    if(isDayTime === true){
      time = 'Day';
    }
    else{
      time = 'Night';
    }
    
    const fetchWeatherData = async () => {
      const city = 'Karachi';
      const response = await fetch(
        "http://dataservice.accuweather.com/forecasts/v1/daily/5day/261158?apikey=sMXa6WnLgzFCBq8HQ7TCAwa0aVah0q7U&details=true&metric=true"
      );
      const responseData = await response.json();
        const icon = responseData["DailyForecasts"][0][time]["Icon"];
        let link = '';
      if(icon > 10){
        link = 'https://developer.accuweather.com/sites/default/files/'
      }
      else{
        link = 'https://developer.accuweather.com/sites/default/files/0'
      }

      const weatherData = {
        city: city,
        headLine: responseData["Headline"]['Text'],
        iconPhrase: responseData["DailyForecasts"][0][time]['IconPhrase'],
        maxTemperature: responseData["DailyForecasts"][0]['Temperature']["Maximum"]['Value'] + 'C',
        minTemperature: responseData["DailyForecasts"][0]['Temperature']["Minimum"]['Value']+ 'C',
        maxFeelsLike: responseData["DailyForecasts"][0]['RealFeelTemperature']["Maximum"]['Value'] + 'C',
        minFeelsLike: responseData["DailyForecasts"][0]['RealFeelTemperature']["Minimum"]['Value']+ 'C',
        windSpeed:responseData["DailyForecasts"][0][time]['Wind']['Speed']['Value'] + responseData["DailyForecasts"][0][time]['Wind']['Speed']['Unit'],
        phrase: responseData["DailyForecasts"][0][time]['ShortPhrase'],
        precipitationProbability:responseData["DailyForecasts"][0][time]['PrecipitationProbability'],
        thunderstormProbability:responseData["DailyForecasts"][0][time]['ThunderstormProbability'],
        icon: link+icon+'-s.png'
      };
      setWeather(weatherData);
    };
    fetchWeatherData();
  }, []);

  const getYear = () => {
    return new Date().getFullYear();
}

  return (
    <Card className="border-0 shadow weatherCard">
      <CardHeader className='border-0'>
        <Row>
          <Col className='col-8 p-3'>
          <h3 className='text-white'>{weather.phrase}.</h3>
          </Col>
          <img src={weather.icon} className='weatherIcon' alt='weather' height='100' />

        </Row>
      </CardHeader>
      <CardBody className='bg-light'>
          <h3>{'Min: '+weather.minTemperature }</h3>
  <h3>{'Max: '+ weather.maxTemperature}</h3>

  <p>{weather.headLine}.</p>

            <p>
              Feels like: {weather.minFeelsLike +'~'+weather.maxFeelsLike}<br />
              Wind speed: {weather.windSpeed } <br />
              Precipitation Probability : {weather.precipitationProbability} % <br />
              Thunderstorm Probability : {weather.thunderstormProbability} % <br />
            </p>

      </CardBody>
      <CardFooter className='border-0'>
          <p className='text-white pl-2 pt-1 pb-0 m-0'>© {getYear()} AccuWeather, Inc.</p>
      </CardFooter>
    </Card>
  );
};

export default WeatherCard;
