

# MNIST 数据集 <!-- {docsify-ignore} -->

**mnist 全称：mixed national institute of standards and technology database**



## 一、通过 torchvision 下载数据



###  1、torchvision 官网地址

 官网地址 ： https://pytorch.org/vision/main/generated/torchvision.datasets.MNIST.html





###  2、函数介绍

```Python
train_dataset = torchvision.datasets.MNIST('./data', 
                                           train=True, 
                                           transform=transform, 
                                           download=True)
```

 参数：

- root ：需要下载至地址的根目录位置
- train：默认是True
  - 如果是True, 下载训练集 train.pt
  - 如果是False，下载测试集 test.pt 
- transform：一系列作用在PIL图片上的转换操作，返回一个转换后的版本
- download：是否下载到 root指定的位置。 如果指定的root位置已经存在该数据集，则不再下载







###  3、下载代码

```Python
import torchvision.datasets

# 更换为你的本地下载地址
data_path = "/Users/enzo/Documents/GitHub/dataset/MNIST"

train_dataset = torchvision.datasets.MNIST('data_path', train=True, download=True)
test_dataset = torchvision.datasets.MNIST('data_path', train=False, download=False)
```

 说明 ： 

  当下载训练集时（即  train=True， download=True 时），会自动一并下载测试集，所以，在指定测试集时（train=False），可以指定 download=False， 因为 在 下载训练集时，测试集已经一并下载下来了。  如果指定 train=False， download=False 也没关系，系统检测到已经下载了测试集后，就不会再重复下载。







###   4、下载后数据结构

<img src="https://p.ipic.vip/mixdna.png" alt="5611695892735_.pic" style="zoom:50%;" />

  后缀为 .gz 的4个文件是压缩文件，下载下来后，文件会自动解压，得到如下4个文件：

- train-images-idx3-ubyte ： 训练集图像数据，包含 60,000张 28x28像素的灰度图像
- train-labels-idx1-ubyte ： 训练集标签数据，包含 60,000个 标签
- t10k-labels-idx1-ubyte ： 测试集图像数据，包含 10,000张 28x28像素的灰度图像
- t10k-images-idx3-ubyte ： 测试集标签数据，包含 10,000个标签







###  5、数据集解析及可视化

```Python
import torchvision.datasets
import matplotlib.pyplot as plt


data_path = "/Users/enzo/Documents/GitHub/dataset/MNIST"

train_dataset = torchvision.datasets.MNIST('data_path', train=True, download=True)
test_dataset = torchvision.datasets.MNIST('data_path', train=False, download=False)

train_images = train_dataset.data
train_labels = train_dataset.targets
test_images = train_dataset.data
test_labels = train_dataset.targets

# 可视化
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.title(train_labels[i].item())
    plt.axis("off")
    plt.imshow(train_images[i])
plt.show()
```



<img src="https://p.ipic.vip/x9wz4s.png" alt="5621695892886_.pic" style="zoom:50%;" />

----



## 二、通过 kaggle 下载数据

### 1、数据集地址

​	Kaggle MNIST数据集地址 ： https://www.kaggle.com/competitions/digit-recognizer/data

<img src="https://p.ipic.vip/pfjbil.png" alt="5631695892964_.pic" style="zoom: 67%;" />

###  2、数据结构

<img src="https://p.ipic.vip/oxcrp1.png" alt="5641695893009_.pic" style="zoom:50%;" />

 说明 ：sample_submission.csv 是kaggle 比赛提交文档参考，可忽略







### 3、数据说明

- 图像为单通道的灰度图，尺寸为 28x28，总共784个像素
- 训练数据集(train.csv) 有 42000行 785列
  - 42000行 表示 42000张图像
  -  785列中的 第0列是label，后面的 784列表示图像的 28x28个像素
- 测试数据集(test.csv) 有 28000行 784列 
  - 28000行 表示 28000张图像
  - 784列表示图像的 28x28个像素，测试数据集没有标签





### 4、数据集解析 及可视化

```Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 更换为你的本地数据集地址
train_file = "/Users/enzo/Documents/GitHub/dataset/MNIST/digit-recognizer/train.csv"
test_file = "/Users/enzo/Documents/GitHub/dataset/MNIST/digit-recognizer/test.csv"

train_data = pd.read_csv(train_file)
train_images = np.array(train_data.iloc[:, 1:]).reshape((-1, 28, 28))
train_labels = np.array(train_data.iloc[:, 0])

test_data = pd.read_csv(test_file)
test_images = np.array(test_data).reshape((-1, 28, 28))


# 可视化
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.title(train_images[i].item())
    plt.axis("off")
    plt.imshow(train_images[i])
plt.show()
```

<img src="https://p.ipic.vip/7jq24g.png" alt="WeChatbe7a8c37a2fc41eb0ea9654c7534d31a" style="zoom: 25%;" />

