# EasyEsp
这是为ESP32 micropython 开发的一款热更新脚本,旨在为各位MicroPython爱好者带来更好的开发体验和开发效率.

## How to use

克隆git仓库到本地
```sh
git clone https://github.com/1zlab/esp-hot-loader.git
```
进入项目目录
```sh
cd 1ZLAB-EasyEsp
```
安装依赖
```sh
pip3 install -r requirements.txt
```


### GUI版本
```sh
python easyEsp.py
```
[]()








- 4 部署到esp32

```sh
sudo python ezesp.py deploy --com='/dev/ttyUSB0' --srcpath='./ezlab'
```
- 5 为获得esp32的局域网ip,暂时需要用户使用piccom或其他工具连接esp32,查看esp32打印的网络信息
- 6 重启esp32 按开发板上的RST,开始初始化程序,当初始化完毕后,再次重启,查看esp32的局域网ip
- 7 开启热更新模式
```sh
python ezesp.py hotload --path='.' --host='192.168.xxx.xxx' 
```
- 8 开始享受拔掉usb线,通过wifi热加载带来的乐趣吧...

## TODO:
- 创建消息队列 5s为一发送周期
- 完善README.md
- pyqtdeploy打包
