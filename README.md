# Trying out Kivy

Used so I can work across multiple computers.

Since I've lately been hearing about [Kivy](http://kivy.org/#home) more and more and got my hands on an old iPhone 3 I've decided to go have a look at Kivy again. 

I'm a complete beginner here too, but if you can use anything from here, feel free to do so (this repo is not meant as a tutorial, so don't expect the code to be nicely commented, everything to work fine etc.) - I'll primarily be focusing on creating some simple/basic apps and testing out how they work on Android (Nexus 5) and iOS (iPhone 3G).

## Installation

I use Kivy in a virtualenv. Not sure what exactly is needed (as I might have some stuff installed previously), but this worked for me. (All commands below are using a virtualenv's pip)

Get the prerequisites for Pygame and some extras for Kivy

    sudo apt-get install python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev   libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev
    
Install Cython and then Pygame

    pip install cython
    pip install pygame

This worked for the basics, but stuff like gst-python and PyEnchant are listed as dependencies, so I installed those too via

    sudo apt-get install python-gst0.10
    pip install pyenchant
