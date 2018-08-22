需要Redis、Selenium、Chrome、ChromeDriver、Xvfb、python3、pip3

# 在Ubuntu下部署(root权限需要)
## 更新 apt
`apt update`
## 安装 pip3
`apt install python3-pip`
## 安装 redis和selenium 模块
`pip3 install redis selenium`
## 安装 Chrome
```
apt-get install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -f
dpkg -i google-chrome*.deb
```
## 安装 Chromedriver
```
wget -N http://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
mv -f chromedriver /usr/local/share/chromedriver
ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```
## 使用 Xvfb 在字符界面运行 Chrome
```
apt-get -y install xvfb gtk2-engines-pixbuf
apt-get -y install xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable
apt-get -y install imagemagick x11-apps
Xvfb -ac :99 -screen 0 1280x1024x16 & export DISPLAY=:99
```