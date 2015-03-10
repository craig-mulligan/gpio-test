FROM resin/rpi-raspbian:wheezy

RUN apt-get update

RUN apt-get install -y libudev-dev python wget build-essential python-dev python-pip

RUN pip install RPi.Gpio

ADD gpio_example.py /App/

CMD ["python", "/App/gpio_example.py"]