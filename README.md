# Assets Survival Scan v1.0.1

[![Python 3.x](https://img.shields.io/badge/python-3.x-g.svg)](https://github.com/helGayhub233/ASscan)

一款偏向于域名的简单资产存活性检测脚本，基于状态码响应判断网站当前访问状态。

<img src="/Users/poco/Desktop/WX20200324-163634@2x.png" alt="Example" style="zoom:50%;" />

## 环境

**版本**

- Python 3.7

**依赖**

- argparse
- requests
- urllib3
- stringcolor

> $ pip install -r requirements.txt

## 使用

**参数**

- -u 单个域名探测
- -i 以列表形式探测(.txt)
- -o 列表导出(.txt)

单个URL检测

> $ asscan.py -u domain.com

多个URL检测

> $asscan.py -i input.txt -o output.txt

## 问题

**Q1：** 遇到超时的域名建议多跑几遍或者根据情况延长`timeout`, 默认设置为3.5。





