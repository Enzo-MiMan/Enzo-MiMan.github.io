参考视频 ： https://www.bilibili.com/video/BV17B4y1z7EL



### 1、日志级别

对于 logging  日志，系统默认提供了6个级别，级别从低到高依次为： 

<mark>NOTSET  <  DEBUG  <  INFO  <  WARNING  <  ERROR  <  CRITICAL</mark>

- **DEBUG**：用于记录开发过程中的细节信息，例如函数调用、变量值等。
- **INFO**：用于记录程序正常运行过程中的一般信息，例如请求开始、请求结束等。
- **WARNING**：用于记录可能导致问题的潜在问题，例如磁盘空间不足、网络连接中断等。
- **ERROR**：用于记录程序运行过程中发生的错误，例如函数调用失败、异常发生等。
- **CRITICAL**：用于记录严重的错误，例如程序崩溃等。
- **NOTSET**：用于表示不记录任何日志信息。

```python
import logging

logging.debug('调试日志')
logging.info('消息日志')
logging.warning('警告日志')
logging.error('错误日志 ')
logging.critical('严重错误日志')
```



每次指定日志的时候，都会指定该日志是什么级别

代码运行时，系统默认只打印 warning 级别以上的日志

可以给日志对象(Logger Instance) 设置日志级别，低于该级别的日志消息将会被忽略

也可以给Hanlder设置日志级别，对于低于该级别的日志消息, Handler也会忽略。



---



### 2、打印日志

打印日志的效果和 print 类似，不一样的是，在默认情况下，只打印 warning 级别以上的日志

若想要修改日志打印级别，需要通过 `logging.basicConfig`  进行调整 （如下第3点有介绍）

<sub>日志级别的优先级从低到高依次为： NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL</sub>

```python
import logging

logging.debug('调试日志')
logging.info('消息日志')
logging.warning('警告日志')
logging.error('错误日志 ')
logging.critical('严重错误日志')
```

输出：

```
WARNING:root:警告日志 
ERROR:root:错误日志 
CRITICAL:root:严重错误日志
```





---



### 3、logging.basicConfig 

 通过 `logging.basicConfig` 函数对日志的 输出格式 及 方式 做相关配置

```python
# 日志基本配置
logging.basicConfig(
    level=40,  
    format='%(asctime)s %(name)s [%(pathname)s line:(lineno)d] %(levelname)s %(message)s]',  
    datefmt='%Y-%m-%d %H:%M:%S',   
    filename='user.log') 
```

参数：

- level：指定打印的日志级别， debug：10,   info：20,   warning：30,   error：40,   critical：50
- format：日志输出格式，相关格式化串如下：

```
% (name)s           Logger的名字(get1ogger时指定的名字）
%(levelno)d         数字形式的日志级别
%(levelname)s       文本形式的日志级别
%(pathname)s        调用日志输出位置的完整路径名
%(filename)s        调用日志输出的文件名
%(module)s          调用日志输出日志的模块名
%(funcName)s        调用日志输出日志的函数名
%(1ineno)d          调用日志输出两数的语句所在的代码行
%(created)f         当前时间，用UNIx标准的表示时间的浮 点数表示
%(relativecreated)d 输出日志信息时的，自Loqger创建以 来的毫秒数
%(asctime)s         字符串形式的当前时间，默认格式是“2023-10-05 12:13:33,231”
%(thread)d          线程ID，可能没有
%(threadName)s      线程名，可能没有
%(process)d         进程ID，可能没有
%(message)s         用户输出的消息
```

- datefmt：修改 asctime 的时间格式
- filename：若不指定此配置，默认打印在控制台； 指定后，打印到指定路径文件























