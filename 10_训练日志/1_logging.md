# 日志记录 - Logging <!-- {docsify-ignore} -->



## 一、基础使用

<br />

### 1、日志的6个级别

对于 logging  日志，系统默认提供了6个级别

|      | 级别     | 级别数值 | 使用情况                                                     |
| ---- | -------- | -------- | ------------------------------------------------------------ |
| 1    | NOTSET   | /        | 不记录任何日志信息                                           |
| 2    | DEBUG    | 10       | 用于记录开发过程中的细节信息，例如函数调用、变量值等         |
| 3    | INFO     | 20       | 用于记录程序正常运行过程中的一般信息，例如请求开始、请求结束等 |
| 4    | WARNING  | 30       | 用于记录可能导致问题的潜在问题，例如磁盘空间不足、网络连接中断等 |
| 5    | ERROR    | 40       | 用于记录程序运行过程中发生的错误，例如函数调用失败、异常发生等 |
| 6    | CRITICAL | 50       | 用于记录严重的错误，例如程序崩溃等                           |

级别从低到高依次为 ： <mark>NOTSET   <   DEBUG   <   INFO   <  WARNING   <   ERROR  <  CRITICAL</mark>



---



### 2、打印日志

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

输出中包含 ：日志级别，记录器(以上的 "root" 就是记录器的名称），日志内容



logging 打印日志的效果和 print 类似，不一样的是，<font color="red"> 在默认情况下，只打印 warning 级别以上的日志 </font>， 低于该级别的日志消息将会被忽略

若想要修改日志打印级别，需要通过 `logging.basicConfig`  进行调整 （下面有介绍）



---



### 3、logging.basicConfig 

 通过 `logging.basicConfig` 函数对日志的 输出格式 及 方式 做相关配置

```python
logging.basicConfig(
    level=logging.DEBUG,  
    format='%(asctime)s %(name)s [%(pathname)s line:%(lineno)d] %(levelname)s %(message)s]', 
    datefmt='%Y-%m-%d %H:%M:%S',   
    filename='demo.log',
    filemode='w') 
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
- filemode：文件写入方式：
  - 'w'：覆盖文件中现有数据
  - 'a' : 追加到文件末尾


<br />

<br />



### 4、实例演示

```python
import numpy as np
import torch
import torch.nn as nn
from torchvision.datasets import mnist
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch.optim as optim
import matplotlib.pyplot as plt
import logging


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
logging.basicConfig(format="%(message)s", level=logging.INFO, filename='./mnist.log', filemode='w')

train_batch_size = 16
test_batch_size = 32
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize([0.5], [0.5])])

# 下载数据 & 导入数据
train_set = mnist.MNIST("/Users/enzo/Documents/GitHub/dataset", train=True, download=True, transform=transform)
test_set = mnist.MNIST("/Users/enzo/Documents/GitHub/dataset", train=False, transform=transform)

train_loader = torch.utils.data.DataLoader(train_set, batch_size=train_batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_set, batch_size=test_batch_size, shuffle=False)

# # 抽样查看图片
# examples = enumerate(train_loader)
# batch_index, (example_data, example_label) = next(examples)
# print(type(example_data))   # <class 'torch.Tensor'>
# print(example_data.shape)   # torch.Size([64, 1, 28, 28])

# for i in range(6):
#     plt.subplot(2, 3, i+1)
#     plt.tight_layout()
#     plt.imshow(example_data[i][0], cmap='gray')
#     plt.title("Ground Truth: {}".format(example_label[i]))
#     plt.xticks([])
#     plt.yticks([])
# plt.show()


class LeNet5(nn.Module):
    """ 使用sequential构建网络，Sequential()函数的功能是将网络的层组合到一起 """
    def __init__(self, in_channel, output):
        super(LeNet5, self).__init__()
        self.layer1 = nn.Sequential(nn.Conv2d(in_channels=in_channel, out_channels=6, kernel_size=5, stride=1, padding=2),   # (6, 28, 28)
                                    nn.Tanh(),
                                    nn.AvgPool2d(kernel_size=2, stride=2, padding=0))   # (6, 14, 14))
        self.layer2 = nn.Sequential(nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0),  # (16, 10, 10)
                                    nn.Tanh(),
                                    nn.AvgPool2d(kernel_size=2, stride=2, padding=0))   # (16, 5, 5)
        self.layer3 = nn.Conv2d(in_channels=16, out_channels=120, kernel_size=5)  # (120, 1, 1)
        self.layer4 = nn.Sequential(nn.Linear(in_features=120, out_features=84),
                                    nn.Tanh(),
                                    nn.Linear(in_features=84, out_features=output))

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = torch.flatten(input=x, start_dim=1)
        x = self.layer4(x)
        return x


model = LeNet5(1, 10)
model.to(device)

lr = 0.01
num_epoches = 20
momentum = 0.8

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)


for epoch in range(num_epoches):
    logging.info("epoch ：{}".format(epoch))


    if epoch % 5 == 0:
        optimizer.param_groups[0]['lr'] *= 0.1

    model.train()
    for i, (imgs, labels) in enumerate(train_loader):
        imgs, labels = imgs.to(device), labels.to(device)
        predict = model(imgs)
        loss = criterion(predict, labels)

        # back propagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # accurate rate
        result = torch.argmax(predict, dim=1)
        acc_num = (result == labels).sum().item()
        acc_rate = acc_num / imgs.shape[0]

        if i % 200 == 0:
            logging.info('loss : {:.3f}'.format(loss.item()))
            logging.info('acc_rate : {:.3f}'.format(acc_rate))

```





<br />

<br />



## 二、logging 的高级应用



logging 采用了模块化设计，主要由四个部分组成：

​	1、Loggers : 日志记录器，提供程序直接调用的接口

​	2、Handlers ： 日志处理器，将记录的日志发送到指定的位置（终端打印 or 保存到文件）

​	3、Filters ：日志过滤期，提供可更好的粒度控制，决定哪些日志被输出

​	4、Formatters ： 日志格式器，用于控制日志信息的输出格式



### 1、记录器 Loggers

```python
# 实例化一个记录器，并将记录器的名字设为 'training_log'
logger = logging.getLogger(name='training_log')

# 设置 logger 的日志级别为 info
logger.setLevel(logging.INFO)
```

如果 `logging.getLogger` 不设置参数name 的话，默认记录器的名字为 'root'



<br />

<br />



### 2、处理器 Handlers

```py
# 1、创建一个handler，该handler往console打印输出
consoleHandler = logging.StreamHandler() 
# 2、设置 consoleHandler 的日志级别为 debug
consoleHandler.setLevel(logging.DEBUG) 

# 3、再创建一个handler，该handler往文件中打印输出
# 未给fileHandler指定日志级别，它会默认使用logger 的日志级别 
fileHandler = logging.FileHandler(filename='demo.log ') 
```



StreamHandler 和 FileHandler 是最常用的两个 handler，其他的还有：

- BaseRotatingHandler

- RotatingFileHandler

- TimedRotatingFileHandle

- SocketHandler

- DatagramHandler

- SMTPHandler

- SysLogHandler

- NTEventLogHandler

- HTTPHandler

- WatchedFileHandler

- QueueHandler

- NullHandler

  

<br />

<br />

 

### 3、formatter 格式

```python
# 创建一个标准版日志打印格式
standard_formatter = logging.setFormatter('%(asctime)s %(name)s [%(pathname)s line:(lineno)d] %(levelname)s %(message)s]')

# 创建一个简单版日志打印格式
simple_formatter = logging.setFormatter('%(levelname)s %(message)s]')
```



<br />

<br />



### 4、创建关联

<img src="https://p.ipic.vip/6lfk9k.png" alt="image-20231017170616956" style="zoom:50%;" />



```python
# 让 consoleHandler 使用 标准版日志打印格式
consoleHandler.Formatter(standard_formatter)
# 让 fileHandler 使用 标准版日志打印格式
fileHandler.Formatter(simple_formatter)

# 给记录器绑定上 consoleHandler 和 fileHandler
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)
```



<br />

<br />



### 5、打印日志

让记录器对象 `logger` 调用日志方法，按照之前的设置，打印日志

```python
logger.debug('调试日志')
logger.info('消息日志')
logger.warning('警告日志')
logger.error('错误日志 ')
logger.critical('严重错误日志')
```



<br />

<br />



### 6、整体代码举例

  ```python
  import logging
  
  # ============================ 1、实例化 logger ============================
  # 实例化一个记录器，并将记录器的名字设为 'training_log'，并将日志级别为 info
  logger = logging.getLogger(name='training_log')
  logger.setLevel(logging.INFO)
  
  
  # ============================ 2、定义Handler ============================
  # 创建一个往 console打印输出的 Handler，日志级别为 debug
  consoleHandler = logging.StreamHandler() 
  consoleHandler.setLevel(logging.DEBUG) 
  # 再创建一个往文件中打印输出的handler， 默认使用logger 的日志级别 
  fileHandler = logging.FileHandler(filename='demo.log ') 
  
  
  # ============================ 3、定义打印格式 ============================
  # 创建一个标准版日志打印格式
  standard_formatter = logging.Formatter('%(asctime)s %(name)s [%(pathname)s line:(lineno)d] %(levelname)s %(message)s]')
  
  # 创建一个简单版日志打印格式
  simple_formatter = logging.Formatter('%(levelname)s %(message)s]')
  
  # ============================ 4、绑定 ============================
  # 让 consoleHandler 使用 标准版日志打印格式
  consoleHandler.setFormatter(standard_formatter)
  # 让 fileHandler 使用 标准版日志打印格式
  fileHandler.setFormatter(simple_formatter)
  
  # 给记录器绑定上 consoleHandler 和 fileHandler
  logger.addHandler(consoleHandler)
  logger.addHandler(fileHandler)
  
  # ============================ 5、打印 ============================
  logger.debug('调试日志')
  logger.info('消息日志')
  logger.warning('警告日志')
  logger.error('错误日志 ')
  logger.critical('严重错误日志')
  
  ```







## 三、通过配置文件处理日志

配置文件 ` log.conf` 

```python
[loggers]
keys=root,loss,accurate

[handlers]
keys=consoleHandler,lossFileHandler,accFileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=INFO
handlers=consoleHandler
qualname=root_log

[logger_loss]
level=INFO
handlers=lossFileHandler
qualname=loss_log
propagate = 0

[logger_accurate]
level=INFO
handlers=accFileHandler
qualname=accurate_log
propagate = 0

[handler_consoleHandler]
class=StreamHandler
args=(sys.stdout,)
level=INFO
formatters=simpleFormatter

[handler_lossFileHandler]
class=FileHandler
args=("loss.log", 'w')
level=INFO
formatters=simpleFormatter

[handler_accFileHandler]
class=FileHandler
args=("acc_rate.log", 'w')
level=INFO
formatters=simpleFormatter

[formatter_simpleFormatter]
format=%(message)s

```



