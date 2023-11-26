

# Flowers 数据集<!-- {docsify-ignore} -->



## 1、数据集下载

下载地址：https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz



----



## 2、数据集类别

| 类别       | 中文说明 | 图片数量 |
| ---------- | -------- | -------- |
| daisy      | 雏菊     | 633      |
| dandelion  | 蒲公英   | 898      |
| roses      | 玫瑰     | 641      |
| sunflowers | 向日葵   | 699      |
| tulips     | 郁金香   | 799      |



----



## 3、数据集结构

每个类别有一个文件夹



<img src="https://p.ipic.vip/ey8tlk.png" alt="5651695893355_.pic" style="zoom:50%;" />



----

<br/>

### 4、数据处理

```python
import os
import json
import random
from PIL import Image
import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms


def read_split_data(root, val_rate=0.2):
    
    assert os.path.exists(root), "dataset root: {} does not exist.".format(root)

    flower_class = [cla for cla in os.listdir(root) if os.path.isdir(os.path.join(root, cla))]
    flower_class.sort()
    class_indices = dict((k, v) for v, k in enumerate(flower_class))
    print(class_indices) 

    train_images_path = []
    train_images_label = []
    val_images_path = []
    val_images_label = []
    every_class_num = []
   
    for cla in flower_class:
        cla_path = os.path.join(root, cla)
        images = [os.path.join(root, cla, i) for i in os.listdir(cla_path)]
        images.sort()
        image_class = class_indices[cla]
        
        every_class_num.append(len(images))
        val_path = random.sample(images, k=int(len(images) * val_rate))
        
        # 划分训练集 和 验证集
        for img_path in images:
            if img_path in val_path:  
                val_images_path.append(img_path)
                val_images_label.append(image_class)
            else:  
                train_images_path.append(img_path)
                train_images_label.append(image_class)

    print("{} images were found in the dataset.".format(sum(every_class_num)))
    print("{} images for training.".format(len(train_images_path)))
    print("{} images for validation.".format(len(val_images_path)))
    assert len(train_images_path) > 0, "number of training images must greater than 0."
    assert len(val_images_path) > 0, "number of validation images must greater than 0."

    return train_images_path, train_images_label, val_images_path, val_images_label


class MyDataSet(Dataset):
    """自定义数据集"""

    def __init__(self, images_path, images_class, transform=None):
        self.images_path = images_path
        self.images_class = images_class
        self.transform = transform

    def __len__(self):
        return len(self.images_path)

    def __getitem__(self, item):
        img = Image.open(self.images_path[item])
        label = self.images_class[item]

        if self.transform is not None:
            img = self.transform(img)

        return torch.as_tensor(img), torch.as_tensor(label)


data_root = "dataset/flower_photos"
train_images_path, train_images_label, val_images_path, val_images_label = read_split_data(data_root)

# =============================== Transform ===============================
img_size = 224
train_transform = transforms.Compose([transforms.RandomResizedCrop(img_size),
                                        transforms.RandomHorizontalFlip(),
                                        transforms.ToTensor(),
                                        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

val_transform = transforms.Compose([transforms.Resize(int(img_size * 1.143)),
                                      transforms.CenterCrop(img_size),
                                      transforms.ToTensor(),
                                      transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

# =============================== DataSet ===============================

train_dataset = MyDataSet(images_path=train_images_path,
                          images_class=train_images_label,
                          transform=train_transform)

val_dataset = MyDataSet(images_path=val_images_path,
                        images_class=val_images_label,
                        transform=val_transform)

# =============================== DataLoader ===============================

train_loader = torch.utils.data.DataLoader(train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True,
                                           pin_memory=True,
                                           num_workers=num_workers)

val_loader = torch.utils.data.DataLoader(val_dataset,
                                         batch_size=batch_size,
                                         shuffle=False,
                                         pin_memory=True,
                                         num_workers=num_workers)

print("len(train_loader) = {}".format(len(train_loader)))
print("len(val_loader) = {}".format(len(val_loader)))
```



