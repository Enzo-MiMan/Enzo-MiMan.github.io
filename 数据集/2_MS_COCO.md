![image-20230928145121382](https://p.ipic.vip/gu9kq4.png)



## 1、简介

MS COCO ：Microsoft Common Objects in Context

​                      是一个由微软公司创建的用于图像识别和物体检测的大型数据集。

官网地址：https://cocodataset.org/

论文地址:  https://arxiv.org/pdf/1405.0312.pdf



----



## 2、数据集说明

### 1）数据集特征

<img src="https://p.ipic.vip/676skv.png" alt="5681695896943_.pic" style="zoom: 45%;" />

** stuff 指的是 天空，街道， 草地等这种没有明显边界的目标

<img src="https://p.ipic.vip/xo5p94.png" alt="5691695896964_.pic" style="zoom: 50%;" />



### 2）MS COCO 2014 版本 与 MS COCO 2017 版本的区别

- 2017版数据集 是对 2014版数据集 的扩展和更新
- 2017版 和 2014版 使用完全相同的图像，不一样的是：
  - 2017版 训练集/验证集 的划分是 118K/5K
  - 2014版 是 83K/41K
- 2017版中用于 检测类任务 / 关键点检测 的注释 和 2014版 是一样的， 

​         但是增加了 40K 张训练图像 （118k 训练集中的子集） 和 所有验证集 的stuff 标注 （后面有介绍 stuff categories）

2017年的测试集只有两个部分(开发集/挑战集)，而2014版的测试集有四个部分(开发集/标准集/储备集/挑战集)。

2017版 发布12万张来自COCO的无标记图像，这些图像遵循与标记图像相同的类分布 ，可用于半监督学习。



### 3）80个 类别

![5701695897020_.pic](https://p.ipic.vip/2lh2sc.png)



## 3、数据集下载

官网下载地址：https://cocodataset.org/#download

或者，直接点击如下链接直接下载

| 目标检测任务语义分割任务实例分割任务（以上3个任务使用相同数据文件） | 2014 数据集                                                  | 训练数据集                                                   |      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 验证数据集                                                   |                                                              |                                                              |      |
| 标注文件                                                     |                                                              |                                                              |      |
| 2017 数据集                                                  | 训练数据集                                                   | [2017 Train images [118K/18GB\]](http://images.cocodataset.org/zips/train2017.zip) |      |
| 验证数据集                                                   | [2017 Val images [5K/1GB\]](http://images.cocodataset.org/zips/val2017.zip) |                                                              |      |
| 标注文件                                                     | [2017 Train/Val annotations [241MB\]](http://images.cocodataset.org/annotations/annotations_trainval2017.zip) |                                                              |      |







## 5、数据集解析

### 1）目标检测任务

####   a、数据结构

```Python
.
├── annotations
│   ├── captions_train2017.json          图像描述的 训练集标注文件
│   ├── captions_val2017.json            图像描述的 验证集标注文件
│   ├── instances_train2017.json         对应目标检测、分割任务的 训练集标注文件
│   ├── instances_val2017.json           目标检测、分割任务的 验证集标注文件
│   ├── person_keypoints_train2017.json  人体关键点检测的 训练集标注文件
│   └── person_keypoints_val2017.json    人体关键点检测的 验证集标注文件
├── train2017
│   ├── 000000000009.jpg
│   ├── 000000000025.jpg
│   ├── 000000000030.jpg
│   ├── 000000000034.jpg
│   ├── 000000000036.jpg
│   └── ... (共118287张图像)
└── val2017
    ├── 000000000139.jpg
    ├── 000000000285.jpg
    ├── 000000000632.jpg
    ├── 000000000724.jpg
    ├── 000000000776.jpg
    └── ... (共5000张图像)
```

 **instances_train2017.json 文件的数据结构如下 （ instances_val2017.json 文件结构也是一样 ）**

![5711695897153_.pic](https://p.ipic.vip/nhc8b4.png)





####  b、数据集解析









### 2）语义分割任务





### 3）实例分割任务





---







## 附件

### 1）80个 类别

| supercategory | id   | name           |
| :------------ | :--- | :------------- |
| person        | 1    | person         |
| vehicle       | 2    | bicycle        |
| vehicle       | 3    | car            |
| vehicle       | 4    | motorcycle     |
| vehicle       | 5    | airplane       |
| vehicle       | 6    | bus            |
| vehicle       | 7    | train          |
| vehicle       | 8    | truck          |
| vehicle       | 9    | boat           |
| outdoor       | 10   | traffic light  |
| outdoor       | 11   | fire hydrant   |
| outdoor       | 13   | stop sign      |
| outdoor       | 14   | parking meter  |
| outdoor       | 15   | bench          |
| animal        | 16   | bird           |
| animal        | 17   | cat            |
| animal        | 18   | dog            |
| animal        | 19   | horse          |
| animal        | 20   | sheep          |
| animal        | 21   | cow            |
| animal        | 22   | elephant       |
| animal        | 23   | bear           |
| animal        | 24   | zebra          |
| animal        | 25   | giraffe        |
| accessory     | 27   | backpack       |
| accessory     | 28   | umbrella       |
| accessory     | 31   | handbag        |
| accessory     | 32   | tie            |
| accessory     | 33   | suitcase       |
| sports        | 34   | frisbee        |
| sports        | 35   | skis           |
| sports        | 36   | snowboard      |
| sports        | 37   | sports ball    |
| sports        | 38   | kite           |
| sports        | 39   | baseball bat   |
| sports        | 40   | baseball glove |
| sports        | 41   | skateboard     |
| sports        | 42   | surfboard      |
| sports        | 43   | tennis racket  |
| kitchen       | 44   | bottle         |
| kitchen       | 46   | wine glass     |
| kitchen       | 47   | cup            |
| kitchen       | 48   | fork           |
| kitchen       | 49   | knife          |
| kitchen       | 50   | spoon          |
| kitchen       | 51   | bowl           |
| food          | 52   | banana         |
| food          | 53   | apple          |
| food          | 54   | sandwich       |
| food          | 55   | orange         |
| food          | 56   | broccoli       |
| food          | 57   | carrot         |
| food          | 58   | hot dog        |
| food          | 59   | pizza          |
| food          | 60   | donut          |
| food          | 61   | cake           |
| furniture     | 62   | chair          |
| furniture     | 63   | couch          |
| furniture     | 64   | potted plant   |
| furniture     | 65   | bed            |
| furniture     | 67   | dining table   |
| furniture     | 70   | toilet         |
| electronic    | 72   | tv             |
| electronic    | 73   | laptop         |
| electronic    | 74   | mouse          |
| electronic    | 75   | remote         |
| electronic    | 76   | keyboard       |
| electronic    | 77   | cell phone     |
| appliance     | 78   | microwave      |
| appliance     | 79   | oven           |
| appliance     | 80   | toaster        |
| appliance     | 81   | sink           |
| appliance     | 82   | refrigerator   |
| indoor        | 84   | book           |
| indoor        | 85   | clock          |
| indoor        | 86   | vase           |
| indoor        | 87   | scissors       |
| indoor        | 88   | teddy bear     |
| indoor        | 89   | hair drier     |
| indoor        | 90   | toothbrush     |