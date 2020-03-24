# Assets Survival Scan v1.0.1

[![Python 3.x](https://img.shields.io/badge/python-3.x-g.svg)](https://github.com/helGayhub233/ASscan)

一款偏向于域名的简单资产存活性检测脚本，基于状态码响应并判断网站当前访问状态。

<img src="https://github.com/helGayhub233/ASscan/blob/master/images/WX20200324-163634%402x.png" alt="Example" width="50%" height="50%" />

## 思路

200、3xx、4xx、5xx归类为正常访问(即开放了服务但不排除其他目录下可能存在其他应用)；  
访问异常、超时归类为无法访问；

## 环境

**版本**

- Python 3.x

**依赖**

- requests
- urllib3
- stringcolor

```
 $ pip install -r requirements.txt
```

## 使用

**参数**

- -u 单域名探测
- -i 列表探测(.txt)
- -o 列表导出(.txt)

单个URL检测
```
$ asscan.py -u domain.com
```

多个URL检测
```
$ asscan.py -i input.txt -o output.txt
```
## 问题

**Q1：** 遇到超时的域名建议多跑几遍或者根据情况延长`timeout`, 默认设置为3.5。





