# Temperature Sensor Simulation

This example demonstrate a sensor data emitting real-time temperature.
User can provide a config to chose a scale (Fahrenheit, Celsius, Kelvin)

# To install docker 
please follow instruction @ https://docs.docker.com/get-docker/

# To build docker image
```
cd sensor

sudo docker build . -t sensor `

```

# To run the container:

```sudo docker run -p 80:80 sensor:latest```

Open a browser and type http://127.0.0.1/sensor/
On every refersh a new temperature value should appear

Config can be access @ http://127.0.0.1/sensor/config








