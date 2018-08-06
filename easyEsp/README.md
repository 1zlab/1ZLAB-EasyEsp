# esp-hot-loader
这是为ESP32 micropython 开发的一款热更新脚本,旨在为各位MicroPython爱好者带来更好的开发体验和开发效率.

## How to use
- 1 克隆git仓库到本地
```sh
git clone https://github.com/1zlab/esp-hot-loader.git
```
- 2 进入工程目录
```sh
cd esp-hot-loader
```
- 3 更改配置文件 ezlab/esp_config.json
```json
{
    "wifi_name": "xxxx",
    "wifi_pwd": "xxxx",
    "is_developing": "1" 
}
```
分别对应为:
> - wifi名称
> - wifi密码
> - 是否开启开发(热更新)模式,1为开启,0为关闭 

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
- 使用UDP广播自动捕获 esp32 内网ip
- 完善README.md
