# 题目：抓取全部5页直播间热度，计算前5名直播间热度的加和

## 地址:https://match.yuanrenxue.cn/match/5

![alt text](./images/image.png)

## 注意:  要用浏览器无痕模式打开，否则翻页不跳转，cookie也不会有变化

#### 首先打开控制台，发现一直在console，一秒钟上千条的节奏。电脑配置本来就不高，先把他置空吧

#### console.log = function(){}

![alt text](./images/image-1.png)

#### 照例进网络观察一下请求

#### cookie有效期只有50秒，过期以后参数f,m。cookie m,RM4hZBv0dDon443M都有变动，看来要获取这四个数据了

![alt text](./images/image-2.png)
![alt text](./images/image-3.png)

#### 先从url开始吧，f,m看起来像时间戳，而且前8位相同，应该有什么联系，hook看一下

![hook代码](./images/image-4.png)

#### 找到了，接下来通过堆栈看一下f和m是怎么生成的

![alt text](./images/image-5.png)

#### ajax这里第一次看到f和m，继续往下，request看到f和m是分别是由window.$_zw [23]和window. _$is赋值

![alt text](./images/image-7.png)

![alt text](./images/image-6.png)

#### 找一下这两个window对象吧，看一下是不是他俩生成的

#### 先全局搜索一下$_zw，发现286行新建了一个空数组赋给他，就从这开始找吧

![alt text](./images/image-8.png)

#### 往下稍微一滑，就看到这里push了一大串东西给$_zw,数了一下，$_t1是第23个push给他的，就是你了！

![alt text](./images/image-9.png)

#### 回头找找$_t1，就在不远处，可以看到就是一个时间戳，数值和$_zw[23]也能对上

![alt text](./images/image-10.png)

#### 连脑子都不用动，直接全拿过来，这样f就有了，因为f是string属性，所以末尾加一个toString()做个类型转换

Date.parse(new Date()).toString()

#### 接下来就是_$is了，全局搜索没搜到，还是hook一下

![alt text](./images/image-11.png)

#### hook秒了，window._$is是由 _$yw赋值，看看 _$yw是什么情况吧。另外上面的m是我们要找的cookie，先记一下一会回来细看

![alt text](./images/image-12.png)

#### 跳转到函数发现只是new Date().valueOf()，_$yw在返回值的基础上toString()了一下，这样两个参数都有了，接下来开始找cookie

new Date().valueOf().toString()

![alt text](./images/image-13.png)

#### hook一下cookie，先都跑一遍，发现m好像出现了五次，最后一次出现前还设置了两次RM4hZBv0dDon443M，有点奇怪

![alt text](./images/image-14.png)

#### 跟随m执行打断点，发现m最后一次执行和前四次执行的不是一个函数，可以判断这次执行就是最终m的值。可以扒代码了

![alt text](./images/image-23.png)

#### 继续下一步，看看RM4hZBv0dDon443M是怎么来的吧,依旧hook

#### 可以看到这个cookie是用数组构成的，这样就防止全局搜索直接搜到了

#### 跟m一样，RM也出现了5次，前三次undefind,后两次有值，进堆栈看到值是window._$ss生成的，那就监听一下这个属性

![alt text](./images/image-16.png)

#### 为了不被搜到真是煞费苦心，两个s都是混淆后的字符，等价于window['_$ss'] = _0x29dd83 ['toString'] ()

#### _0x29dd83函数就在上面，看到mode和padding就知道是个加密函数

![alt text](./images/image-18.png)

#### 这一大坨真不想看，让ai帮忙解析一下吧，对照ai结果看了几个字符，发现没什么问题，接下来找数据和密钥吧
```

_0x29dd83 = _$Tk['AES']['encrypt'](
    _$Ww, 
    _0x4e96b4[_0xc77418('0x6', 'OCbs')], 
    {
        'mode': _$Tk['mode']['ECB'],

        'padding': _$Tk['pad']['Pkcs7']
    }
),
```
#### 抬头一看，数据不就在上面吗，看来也是加密的，那就看看_$pr是怎么生成的吧

#### 和cookie，m一样，_$pr.push也执行五次，前四次一个函数，第五次另一个函数，跳到函数位置把生成数据的函数拿过来，手动构造一下就可以

![alt text](./images/image-25.png)

![alt text](./images/image-24.png)

```
pr = [];
for (i = 1; i < 5; i++) {
    var _$Wa = Date.parse(new Date());
    pr.push(_0x474032(_$Wa))
}
//console.log(_$Wa)
var _$yw = new Date().valueOf().toString();
pr.push(_0x474032(_$yw));
```

#### _$pr已经知道怎么生成了，把这个段代码原样拿过来 _$Ww 就有了

![alt text](./images/image-21.png)

#### 给_0x4e96b4[_0xc77418('0x6', 'OCbs')] 打个断点，跳转到函数定义位置，剩下就是苦力活了，一点点扒

#### 这里有个坑，如果扒下来的代码直接运行，会报一个execjs._exceptions.ProgramError: RangeError: Invalid array length错误

#### 这是因为原代码中有一个反调试代码，交给ai稍微处理一下就好

![alt text](./images/image-22.png)

#### 现在全部参数都得到了，循环请求页面把值放到一个数组里，给所有热度值排个序，最后算一下数组前五个值的和就好