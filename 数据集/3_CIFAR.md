## 一、官网地址

数据集官网地址 ： https://www.cs.toronto.edu/~kriz/cifar.html



---



## 二、CIFAR-10 数据集

### 1、数据集介绍

- CIFAR-10 数据集由 60000张 32 × 32 彩色图像组成
- 60000张图片包括： 50000张训练图像 + 10000张测试图像
- 数据集包括 10个类，每个类有6000张图像
  
  <img src="https://p.ipic.vip/bzlw1k.png" alt="5661695893815_.pic" style="zoom:50%;" />
  
- 这些类是完全互斥的：汽车和卡车之间没有重叠。“汽车”包括轿车、suv之类的东西。“卡车”只包括大卡车。这两项都不包括皮卡。



----



### 2、数据集下载

| **数据集版本**             | **点击下载**                                                 | **数据集大小** |
| -------------------------- | ------------------------------------------------------------ | -------------- |
| python 版本                | [CIFAR-10 python version](https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz) | 163 MB         |
| matlab 版本                | [CIFAR-10 Matlab version](https://www.cs.toronto.edu/~kriz/cifar-10-matlab.tar.gz) | 175 MB         |
| binary 版本（适用于c语言） | [CIFAR-10 binary version (suitable for C programs)](https://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz) | 162 MB         |



----



### 3、数据集结构 （python 版本）

- Python 版本的数据集下载并解压后，数据结构如下：
  - 5个 train batch  + 1个 test batch，每个 batch 10000张图片
  
  - test batch 包含10000张图片，是从每一个类别的图片中 分别随机抽取出1000张图像 组成的集合
  
  - train batch 是由剩下的 50000张图片打乱顺序，然后随机分成5份。 所以每个 train batch 中，10个种类的图片数量不是相等的，会出现一个类别的图片数量比另一个类别图片数量多的情况
  
    <img src="https://p.ipic.vip/au7yif.png" alt="5671695893872_.pic" style="zoom: 50%;" />
  
- python版本 的数据集结构 与 Matlab版本的数据集结构是相同的。

- 数据集中的文件 data_batch_1、data_batch_2、…、data_batch_5 以及 test_batch， 每一个都是由cPickle生成的Python“pickle”对象。



----



### 4、数据集解析

1. 需要将 数据集地址 data_path 更换为 数据集在你本地的地址
2. 需要将 图片存储地址 save_path 更换为 你本地的存储地址

```Python
import os
import pickle
import cv2


def unpickle(file):
    with open(file, 'rb') as f:
        dict = pickle.load(f, encoding='bytes')
    return dict


if __name__ == '__main__':
    # 数据集地址
    data_path = "/Users/enzo/Documents/GitHub/dataset/CIFAR/cifar-10-batches-py"

    # 5个 train batch 和 1个 test batch 的文件夹名称
    batches = ['data_batch_1', 'data_batch_2', 'data_batch_3', 'data_batch_4', 'data_batch_5', 'test_batch']

    # 从 'batches.meta' 文件中 获取10个类别
    meta_file = os.path.join(data_path, 'batches.meta')
    meta_dict = unpickle(meta_file)
    label_name = [label.decode() for label in meta_dict[b'label_names']]  # ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    # 图片存储地址
    save_path = "/Users/enzo/Documents/GitHub/dataset/CIFAR/cifar-10-images"


    if not os.path.exists(save_path):
        os.mkdir(save_path)

    for batch in batches:
        batch_file = os.path.join(data_path, batch)
        batch_dict = unpickle(batch_file)

        images = batch_dict[b'data']
        labels = batch_dict[b'labels']

        save_file = os.path.join(save_path, batch)
        if not os.path.exists(save_file):
            os.mkdir(save_file)

        for index, image in enumerate(images):
            image = image.reshape(-1, 1024).reshape(-1, 32, 32).transpose(1, 2, 0)
            image_name = str(index) + '_' + label_name[labels[index]] + '.png'
            cv2.imwrite(os.path.join(save_file, image_name), cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
```

- batches.meta 文件 包含的内容
  
  <img src="https://p.ipic.vip/p5kaar.png" alt="WeChat31f9568671be4ce5d71fdc68a653cf81" style="zoom:40%;" />
  
  - Label_names：一个包含10个元素的列表，表示10个类别
  
  - ------
- data_batch_1,  data_batch_2,  data_batch_3,  data_batch_4,  data_batch_5,  test_batch 文件 包含的内容
  
  <img src="https://p.ipic.vip/iw4y8n.png" alt="WeChat54cd87dbf4e0bad60f7d3cac64554588" style="zoom:40%;" />
  
  - data：一个 10000x3072 的 uint8 数组。数组的每一行存储一个3x32x32彩色图像。前1024个条目包含红色通道值，中间1024个包含绿色通道值，最后1024个包含蓝色通道值
  - labels：一个包含10000个数字的列表，取值范围从0到9，表示每个图像所属的类别
  
  - ------
- 解析后 保存的图像文件结构

<img src="https://p.ipic.vip/lr082q.png" alt="WeChatf72f2861a45623cb83198a1904bd711d" style="zoom: 25%;" />

----



### 5、下载处理好的图像

链接：https://pan.quark.cn/s/a8008d57a24c

提取码：DDZT



----



## 三、CIFAR-100 数据集

### 1、数据集介绍

- 有100个类，每个类包含600张图像

- 每个类有500个训练图像 和 100个测试图像

- CIFAR-100中的100个类被分成20个超类，如下 ： 

  - | Superclass                     | Classes                                               |
    | ------------------------------ | ----------------------------------------------------- |
    | aquatic mammals                | beaver, dolphin, otter, seal, whale                   |
    | fish                           | aquarium fish, flatfish, ray, shark, trout            |
    | flowers                        | orchids, poppies, roses, sunflowers, tulips           |
    | food containers                | bottles, bowls, cans, cups, plates                    |
    | fruit and vegetables           | apples, mushrooms, oranges, pears, sweet peppers      |
    | household electrical devices   | clock, computer keyboard, lamp, telephone, television |
    | household furniture            | bed, chair, couch, table, wardrobe                    |
    | insects                        | bee, beetle, butterfly, caterpillar, cockroach        |
    | large carnivores               | bear, leopard, lion, tiger, wolf                      |
    | large man-made outdoor things  | bridge, castle, house, road, skyscraper               |
    | large natural outdoor scenes   | cloud, forest, mountain, plain, sea                   |
    | large omnivores and herbivores | camel, cattle, chimpanzee, elephant, kangaroo         |
    | medium-sized mammals           | fox, porcupine, possum, raccoon, skunk                |
    | non-insect invertebrates       | crab, lobster, snail, spider, worm                    |
    | people                         | baby, boy, girl, man, woman                           |
    | reptiles                       | crocodile, dinosaur, lizard, snake, turtle            |
    | small mammals                  | hamster, mouse, rabbit, shrew, squirrel               |
    | trees                          | maple, oak, palm, pine, willow                        |
    | vehicles 1                     | bicycle, bus, motorcycle, pickup truck, train         |
    | vehicles 2                     | lawn-mower, rocket, streetcar, tank, tractor          |

备注 ： 以上分类中，虽然蘑菇(mushrooms) 不是真正的水果或蔬菜，熊(bear)也不是真正的食肉动物。



----



### 2、数据集下载

| **数据集版本** | **点击下载**                                                 | **数据集大小** |
| -------------- | ------------------------------------------------------------ | -------------- |
| python 版本    | [CIFAR-100 python version](https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz) | 161 MB         |
| matlab 版本    | [CIFAR-100 Matlab version](https://www.cs.toronto.edu/~kriz/cifar-100-matlab.tar.gz) | 175 MB         |
| binary 版本    | [CIFAR-100 binary version (suitable for C programs)](https://www.cs.toronto.edu/~kriz/cifar-100-binary.tar.gz) | 161 MB         |



----



### 3、数据集结构 （python 版本）

<img src="https://p.ipic.vip/vx6z8y.png" alt="WeChat7e9ff121e23f5b6f10a015ae10750041" style="zoom:25%;" />

----



### 4、数据集解析

```Python
import os
import pickle
import cv2


def unpickle(file):
    with open(file, 'rb') as f:
        dict = pickle.load(f, encoding='bytes')
    return dict


if __name__ == '__main__':
    # 数据集地址
    data_path = "/Users/enzo/Documents/GitHub/dataset/CIFAR/cifar-100-python"

    # 从 'batches.meta' 文件中 获取10个类别
    meta_file = os.path.join(data_path, 'meta')
    meta_dict = unpickle(meta_file)
    coarse_label_names = [label.decode() for label in meta_dict[b'coarse_label_names']]  # ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    fine_label_name = [label.decode() for label in meta_dict[b'fine_label_names']]

    # 图片存储地址
    save_path = "/Users/enzo/Documents/GitHub/dataset/CIFAR/cifar-100-images"
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    for file in ["test"]:
        file_name = os.path.join(data_path, file)
        data_dict = unpickle(file_name)

        images = data_dict[b'data']
        # coarse_label = data_dict[b'coarse_labels']
        fine_label = data_dict[b'fine_labels']

        save_file = os.path.join(save_path, file)
        if not os.path.exists(save_file):
            os.mkdir(save_file)

        for index, image in enumerate(images):
            image = image.reshape(-1, 1024).reshape(-1, 32, 32).transpose(1, 2, 0)
            image_name = str(index) + '_' + fine_label_name[fine_label[index]] + '.png'
            cv2.imwrite(os.path.join(save_file, image_name), cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
```

- batches.meta 文件 包含的内容 : 
  - coarse_label_names ： 20个粗分类 
  
  - fine_label_names ： 100个细分类

    <img src="https://p.ipic.vip/e7em06.png" alt="WeChat1704ee12425379005be4714e33e954b4" style="zoom:25%;" />
  
- train 文件包含的内容
  - data：一个 50000x3072 的 uint8 数组。表示一共有 50000张图像，数组的每一行为一张图像：3072 = 3x32x32。前1024个条目包含红色通道值，中间1024个包含绿色通道值，最后1024个包含蓝色通道值
  
  - coarse_labels：50000张图像所对应的粗类别
  
  - fine_labels：50000张图像所对应的细类别
  
    <img src="https://p.ipic.vip/8ndc4j.png" alt="WeChat781882c8e75f635aaeef3b31ca6de81f" style="zoom:25%;" />
  
- test 文件包含的内容
  - data：一个 10000x3072 的 uint8 数组。表示一共有 10000张图像，数组的每一行为一张图像：3072 = 3x32x32。前1024个条目包含红色通道值，中间1024个包含绿色通道值，最后1024个包含蓝色通道值
  
  - coarse_labels：10000张图像所对应的粗类别
  
  - fine_labels：10000张图像所对应的细类别
  
    <img src="https://p.ipic.vip/lqu4cb.png" alt="WeChat7fd3294cfa7863cc4e7d9abdaa516bb3" style="zoom:25%;" />



----



### 5、下载处理好的图像

链接：https://pan.quark.cn/s/c024374f96b2

提取码：WZMq