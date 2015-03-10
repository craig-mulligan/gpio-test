FROM resin/rpi-raspbian:wheezy

RUN apt-get update

RUN apt-get install -y python wget build-essential python-dev python-pip mplayer

RUN pip install pyttsx pycurl

ADD gpio_example.py /App/

CMD udevd & python /App/gpio_example.py