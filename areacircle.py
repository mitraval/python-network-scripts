import requests
import netmiko
#import test_areacircle
from math import pi

def area_of_circle(r):
    if r < 0:
        raise ValueError('Negative radius value error')
    return pi*(r**2)
