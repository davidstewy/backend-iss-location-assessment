#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
import turtle
import time

__author__ = 'davidstewy'

# Part A.


def pull_astronauts():
    """Pulls JSON from URL and prints current astronauts and craft"""
    url = 'http://api.open-notify.org/astros.json'
    response = urllib2.urlopen(url)
    result = json.loads(response.read())
    response.close()
    astronauts = result['people']
    for astro in astronauts:
        print '{} is on Spacecraft {}'.format(astro['name'], astro['craft'])
    print 'Number of people currently in space = {}'.format(result['number'])

# Part B.


def spacestation_coord():
    """Pulls the current LAT / LON of the ISS from the URL"""
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib2.urlopen(url)
    result = json.loads(response.read())
    response.close()
    coordinates = result['iss_position']
    lat = coordinates['latitude']
    long = coordinates['longitude']
    timestamp = result['timestamp']
    print 'Latitude: ' + lat
    print 'Longitude: ' + long
    print 'Time data was pulled: {}'.format(time.ctime(timestamp))
    return lat, long, timestamp

# Part C


def create_map(lat, long):
    """Creates the world map and plots the location of the ISS"""
    world_map = turtle.Screen()
    world_map.setup(720, 360)
    world_map.bgpic('map.gif')
    world_map.setworldcoordinates(-180, -90, 180, 90)
    world_map.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(float(long), float(lat))

# Part D
    """Sends LAT/LON of Indy to URL, URL returns JSON timestamp of when ISS will
    passover the given LAT/LON. Plots Indy's location with a passover time."""
    indy_lat = 39.7684
    indy_long = -86.1581
    url = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'.format(
        indy_lat, indy_long)
    response = urllib2.urlopen(url)
    result = json.loads(response.read())
    response.close()
    passover_time = result['response'][0]['risetime']
    indy = turtle.Turtle()
    indy.penup()
    indy.goto(indy_long, indy_lat)
    indy.dot(7, 'yellow')
    indy.hideturtle()
    indy.color('yellow')
    indy.write(time.ctime(passover_time))


def main():
    pull_astronauts()
    coord = spacestation_coord()
    create_map(coord[0], coord[1])
    turtle.exitonclick()


if __name__ == '__main__':
    main()
