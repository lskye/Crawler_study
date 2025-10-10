# 题目：抓取这5页的数字，计算加和并提交结果

## 地址:https://match.yuanrenxue.cn/match/12

![alt text](images/image.png)

#### 观察请求，发现只有请求地址m有变化，找一下m的生成方式。每次请求将我们自己生成的m加进去就行

![alt text](images/image-1.png)

#### 打断点监控url变化

![alt text](images/image-2.png)

#### 通过堆栈找到m生成的地方
#### btoa就是base64加密。用yuanrenxue + 当前页数进行base64加密

![alt text](images/image-3.png)

#### 原样生成一个，请求的时候放到url里就行