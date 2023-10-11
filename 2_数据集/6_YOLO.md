# YOLO 数据集格式格式  <!-- {docsify-ignore} -->



## 1、格式介绍

YOLO数据集格式:  使用 .txt 的文本文件 来存储目标检测任务中使用的图像标注信息

每张图像的 bbox标注 存储在一个 .txt 文件中

.txt 文件中的每一行，为图像中的一个bounding box 信息，每一行的格式如下:

```Python
<object-class> <x> <y> <width> <height>
```

- `object-class`  ：对象类别
- `x`  ：bounding box 的中心点 x坐标。是归一化后的值（由图像的宽度归一化），取值范围为[0, 1]
- `y`  ：bounding box 的中心点y坐标，是归一化后的值（由图像的高度归一化），取值范围为[0, 1]
- `width`：bounding box 的宽度，是归一化后的值（由图像的宽度归一化）。取值范围为[0,1]。
- `height`：bounding box 的高度，是归一化后的值（由图像的高度归一化）。取值范围为[0,1]。





## 2、举例 

一张图像中有 1匹马 和 3个人

<img src="https://p.ipic.vip/85hhxw.png" alt="WeChatbbd705075cc08c08812fb7bb84d570d8" style="zoom:50%;" />

其标注文件 

```Python
13 0.339 0.6693333333333333 0.402 0.42133333333333334
15 0.379 0.5666666666666667 0.158 0.38133333333333336
15 0.612 0.7093333333333334 0.084 0.3466666666666667
15 0.555 0.7026666666666667 0.078 0.34933333333333333
```

类别信息

```Python
{
    "aeroplane": 1,
    "bicycle": 2,
    "bird": 3,
    "boat": 4,
    "bottle": 5,
    "bus": 6,
    "car": 7,
    "cat": 8,
    "chair": 9,
    "cow": 10,
    "diningtable": 11,
    "dog": 12,
    "horse": 13,
    "motorbike": 14,
    "person": 15,
    "pottedplant": 16,
    "sheep": 17,
    "sofa": 18,
    "train": 19,
    "tvmonitor": 20
}
```







## 3、 x、y、width、height   的归一化

以上面的例子中的 horse 来说：

- 图像的尺寸是： （image_width， image_height）=（500， 375）
- horse 的 左上角坐标为：（xmin，ymin）=（69，172）
- horse 的 右下角坐标为：（xmax，ymax）=（270，330）

计算 x_center、y_center、bbox_width、bbox_height

- 中心点x坐标为：`x_center` =（xmin + xmax) / 2 = 169.5
- 中心点y坐标为：`y_center` =（ymin + ymax) / 2 = 251.0
- bbox 的宽度：`bbox_width` = xmax - xmin =  201.0
- bbox 的高度：`bbox_height` = ymax - ymin =  158.0

归一化：

- `x` = x_center / image_width = 0.339
- `y` = y_center / image_height = 0.6693333333333333
- `w` = bbox_width / image_width = 0.402
- `h` = bbox_height / image_height = 0.42133333333333334