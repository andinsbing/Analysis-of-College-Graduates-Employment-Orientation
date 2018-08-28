#! /bin/bash
apt update
apt install python3-pip -y
pip3 install redis selenium

apt-get install libxss1 libappindicator1 libindicator7 -y
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -f
dpkg -i google-chrome*.deb

wget -N http://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
apt install unzip -y
unzip chromedriver_linux64.zip
chmod +x chromedriver
mv -f chromedriver /usr/local/share/chromedriver
ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

apt-get -y install xvfb gtk2-engines-pixbuf
apt-get -y install xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable
apt-get -y install imagemagick x11-apps
Xvfb -ac :99 -screen 0 1280x1024x16 & export DISPLAY=:99

apt install redis-server -y 

echo "everything is OK!"
exit 0
