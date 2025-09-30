# 题目：采集全部5页的彩票数据，计算全部中奖的总金额

## 地址:https://match.yuanrenxue.cn/match/6

![alt text](images/image.png)

#### 先观察请求，发现每次请求url中的q和m是变动的，q是一个拼接值，每次请求会将上次请求的q拼接上本页固定值。
images/
#### cook中m也是变动的，那就只找这三个值

![alt text](images/image-1.png)

#### 话不多说，直接hook，先看看url里的m是怎么生成的

#### 可以看到t和q完全一样，t应该是时间戳，q = 上个请求的q + 请求次数(从2开始) + '-' + t + "|"。我们每次请求都是独立的，所以不用考虑拼接，只构造第一个q就好

![alt text](images/image-2.png)

#### 跳转到加密函数r里看一下,整个加密函数层层嵌套，干脆全复制过来吧

![alt text](images/image-3.png)

#### 运行一下，看看有什么问题。

#### 果然报错了，代码中尝试给window复制，但是没找到window，那我手动加一个吧

![alt text](images/image-4.png)
![alt text](images/image-12.png)
#### 继续运行，提示ASN1未定义

![alt text](images/image-5.png)

#### 转到2585行看一下，原来ASN1是window对象，那我加个window就好

#### node环境没有window这个全局对象，window.ASN1 = u 看似给ASN1定义了，其实只局限在他的作用域，所以我们要显示指定ASN1的归属。
#### 而浏览器环境window属于全局对象，随便在哪定义都能被访问。这个问题就是浏览器环境和node环境的不同导致的

![alt text](images/image-7.png)

#### 有值了，怎么是false。而且一点提示都没有，只能慢慢调试了，从入口函数开始

![alt text](images/image-8.png)

#### 幸运的是一开始就发现问题了。我明明传了两个参数，time怎么是undefind

![alt text](images/image-10.png)

#### 打印一下window看看，居然是空。我一开始定义的window算什么，小丑吗？既然这样，干脆直接写死

![alt text](images/image-11.png)

#### 虽然参数有值了，但还是false,只能继续调试了

![alt text](images/image-13.png)

#### 对比浏览器，可以看到我的this.key没有数据，看看this.key是怎么生成的

![alt text](images/image-14.png)

#### 可以看到入口函数首先new了一个n('jsencrypt'),这个对象调用setPublicKey传递了一串字符，最后追踪到setkey，key = new qe(t)。在控制台我们也new一个，是能new出东西的

![alt text](images/image-15.png)

![alt text](images/image-16.png)

![alt text](images/image-17.png)

#### 回到编辑器这里，同样的断点位置却new了个空，那就继续看qe

![alt text](images/image-18.png)

#### 最终执行到这里，直接返回!1，浏览器却能继续执行，看来问题就出在这里了

![alt text](images/image-19.png)

#### 全部打断点！找找到底执行到哪一行才跳转的，发现问题出现在r = window.ASN1.decode(n)这一行。
#### 又是ASN1，不是都让你归属window了吗

![alt text](images/image-20.png)

#### 控制台看一下window.ASN1，没有问题，发现decode(n)里的参数是undefind,n的生成就在上面，还是控制台s.test(t)，返回false
#### 浏览器试一下，也返回false，那就是走了Base64.unarmor(t)这一个函数，先控制台运行一下

![alt text](images/image-21.png)

#### 直接报错了，浏览器却能执行，那就找到Base64声明的地方

![alt text](images/image-22.png)

#### 又是作用域的问题，给刚刚调用的地方明确调用对象再看看

![alt text](images/image-24.png)\

#### 顺利往下走了，虽然最终结果还是false，再看看this.key，有东西了，但不多。n的值不正常，继续找n是怎么生成的

![alt text](images/image-25.png)

#### 这两处有一处生成了n，浏览器和编辑器都进入了else条件，并且都能正常生成参数e

![alt text](images/image-26.png)

#### ae会返回一个new b(t,e)的值，控制台打印也能看到b函数，奇怪的是编辑器环境根本不会执行这个b，控制台执行也返回0，跟浏览器有点不一样
#### 继续跟浏览器对比，发现编辑器会先进入两次b，然后执行ae。浏览器则是执行到ae后通过ae跳转到b，问题会不会出在这里

![alt text](images/image-27.png)

#### 检查堆栈，发现编辑器执行var n和var g的间隙已经构建了两个n，所以会先执行两次b。

![alt text](images/image-28.png)

#### 本来打算继续深扒，奈何js水平有限，到这开始有点看不懂了。去网上找了找教程。发现有一串混淆代码，放到浏览器控制台运行返回false。将值改为false就能得到正确参数
#### 找遍了互联网也没有说明白那串加密数据是怎么找到的，这一题算是马马虎虎做完了，有思路的同学可以留言互相交流
#### web_js是根据我的思路修改的代码，main是互联网能成功运行的代码,两处都添加了window对象并显式将ASN1定义到window中，main在这基础上只将加密字符改为false

![alt text](images/image-29.png)

#### 正确请求到数据，但是发现只返回三等奖金额，那一二等奖应该是根据三等奖计算的

![alt text](images/image-30.png)

#### 到request下的ajax看看，找到了这一行，稍微计算了一下数值对的上，二等奖*8，一等奖 *15，总销售额 *24。稍微算一下答案就出来了

![alt text](images/image-31.png)

![alt text](images/image-32.png)