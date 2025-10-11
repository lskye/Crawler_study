# 题目：抓取这5页的数字，计算加和并提交结果

## 地址:https://match.yuanrenxue.cn/match/13

![alt text](images/image.png)

#### 观察请求，过一段时间翻页都会重新加载，yuanrenxue_cookie会有变化。找到cookie的生成方式即可

![alt text](images/image-1.png)

#### 经过各种搜索断点找堆栈，都没找到这个cookie生成的地方，再回头观察一下请求。发现同一个页面有两个请求。
#### 可能是第一个请求生成cookie传递给第二个，刚才针对第二个请求的操作都是白忙活

![alt text](images/image-3.png)

#### 请求一下第一个看一下，返回一段js，将document.cookie设置为一串拼接字符串。document.cookie = yuanrenxue=......。这就是我们要找的cookie了

![alt text](images/image-5.png)

#### 使用正则把我们要的数据提取出来

![alt text](images/image-6.png)

#### 因为两个请求是连续的动作，而requests每次请求都是独立的，所以要使用session
#### 使用session获取第一个请求的返回值，将字符串拼接起来传给第二个请求当cookie就完成了