const apiKey = "5d6340fd102e2b7ff8556f85530790e7"; // Replace with your actual API key
const weatherApiUrl = "https://api.openweathermap.org/data/2.5/weather";
const forecastApiUrl = "https://api.openweathermap.org/data/2.5/forecast";

const kelvinToCelsius = (kelvin) => (kelvin - 273.15).toFixed(1);
const kelvinToFahrenheit = (kelvin) => ((kelvin - 273.15) * 9/5 + 32).toFixed(1);

const displayWeather = (data) => {
    const { main, wind, weather, name, sys } = data;
    
    document.getElementById("cityName").textContent = name;
    document.getElementById("cityCode").textContent = sys.country;
    document.getElementById("mainTemperature").textContent = `${kelvinToCelsius(main.temp)} °C`;
    document.getElementById("tempDescription").textContent = weather[0].description;
    document.getElementById("humidity").textContent = main.humidity;
    document.getElementById("wind").textContent = wind.speed;
    document.getElementById("mainTempHot").textContent = kelvinToCelsius(main.temp_max);
    document.getElementById("mainTempLow").textContent = kelvinToCelsius(main.temp_min);
    document.getElementById("main-icon").className = `wi wi-owm-${data.weather[0].id}`;
};

const displayForecast = (data) => {
    const forecastDays = [1, 2, 3, 4];
    forecastDays.forEach((day, index) => {
        const dayForecast = data.list[(day * 8) - 1]; // 8 data points per day
        document.getElementById(`forecast-day-${index + 1}-name`).textContent = new Date(dayForecast.dt * 1000).toLocaleDateString("en-US", { weekday: 'long' });
        document.getElementById(`forecast-day-${index + 1}-main`).textContent = `${kelvinToCelsius(dayForecast.main.temp)} °C`;
        document.getElementById(`forecast-day-${index + 1}-ht`).textContent = `${kelvinToCelsius(dayForecast.main.temp_max)}°C`;
        document.getElementById(`forecast-day-${index + 1}-lt`).textContent = `${kelvinToCelsius(dayForecast.main.temp_min)}°C`;
        document.getElementById(`forecast-day-${index + 1}-icon`).className = `wi wi-owm-${dayForecast.weather[0].id}`;
    });
};

const getWeatherData = async (city) => {
    try {
        const response = await fetch(`${weatherApiUrl}?q=${city}&appid=${apiKey}`);
        if (!response.ok) throw new Error("City not found");
        const weatherData = await response.json();
        displayWeather(weatherData);
        getForecastData(weatherData.coord.lat, weatherData.coord.lon);
    } catch (error) {
        console.error(error);
        $("#protocol-modal").modal("show");
    }
};

const getForecastData = async (lat, lon) => {
    try {
        const response = await fetch(`${forecastApiUrl}?lat=${lat}&lon=${lon}&appid=${apiKey}`);
        if (!response.ok) throw new Error("Forecast data not found");
        const forecastData = await response.json();
        displayForecast(forecastData);
    } catch (error) {
        console.error(error);
        $("#protocol-modal").modal("show");
    }
};

document.getElementById("refreshButton").addEventListener("click", (e) => {
    e.preventDefault();
    const city = prompt("Enter city name:");
    if (city) {
        getWeatherData(city);
    }
});

// Load default weather data
getWeatherData("Orchha"); // Change to desired default city
