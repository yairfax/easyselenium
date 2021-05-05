#!/bin/sh

MAJOR_VER=$(google-chrome --version | awk '{print $3}' | cut -f1 -d '.')
CHROMEDRIVER_VER=$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${MAJOR_VER})

wget "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VER}/chromedriver_linux64.zip"
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/