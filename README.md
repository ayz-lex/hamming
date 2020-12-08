# Overview

## Introduction

This project consists of two parts: 

1. A mathematical exploration of the history and math behind the Hamming Code (7, 4).
2. A program that simulates the process of encoding, correcting, and decoding as described by the Hamming Code.

To understand what the Hamming Code is, skip to the background section first to get an understanding of how the process is meant to work. Then, you can run the sample program to see it in action! 

## Setup

First, clone the repository to a directory you would like. Once navigated to the directory that you want to run the program run the following command: 

``` git clone https://github.com/ayz-lex/hamming.git```

Navigate to inside the project folder by the command:

``` cd hamming ```


Make sure you have Python installed on your computer. Directions to install Python can be found on this page: https://www.python.org/downloads/.

There are two options. The program has a built in virtual environment that contains the necessary numpy packages required for the program inside of it. To run this virtual environment, you will need to have Python 3.8+, as well as pipenv installed.

Directions to install Python can be found above.

Directions to install pipenv can be found here: https://pypi.org/project/pipenv/. To install pipenv, you might need to install pip. That can be found here: https://pip.pypa.io/en/stable/installing/.

Now that everything is installed, you can create the virtual environment by the command:

``` pipenv install ```

To be able to run commands within the virtual environment, run:

``` pipenv shell ```

That completes the setup for this option.

The other option is to just install numpy, and not deal with the pipenv stuff. Because the program is fairly lightweight and only requires one library, you can simply install numpy, and the virtual environment is no longer needed.

Installing numpy requires pip. The guide to install pip is here: https://pip.pypa.io/en/stable/installing/.

Once you have pip, installation is farily easy. the guide install numpy is here: https://numpy.org/install/.

## Encoding

The sender.py file is responsible for encoding a given bit string.

Once setup is complete, you can run the program. To do this run the following command: 

``` python sender.py ```

if that doesn't work run this instead:

``` python3 sender.py ```

if that doesn't work either, than you should if python is properly installed. If that doesn't work, make sure you set everything up properly (described in the setup portion of this README). If that doesn't work, you are on your own.

The rest of the program is self-explanatory, as the following print statements guide you through the process.

## Correction + Decoding

The receiver.py file is responsible for encoding a given bit string.

Once setup is complete, you can run the program. To do this run the following command: 

``` python receiver.py ```

if that doesn't work run this instead:

``` python3 receiver.py ```

if that doesn't work either, than you should if python is properly installed. If that doesn't work, make sure you set everything up properly (described in the setup portion of this README). If that doesn't work, you are on your own.

The rest of the program is self-explanatory, as the following print statements guide you through the process.