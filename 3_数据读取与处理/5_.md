我们在做训练的时候，我们免不了要读入数据，而针对数据的不同存储方式，我们也有不同的读入方法，从而方便我们将训练数据与其标签一一对应上。









## torchvision.datasets.ImageFolder

**方式一**

使用于从一个存放了所有类别数据的文件夹中读取数据。通过重写torch.utils.data.Dataset，构建数据读取方式（自己做处理将数据和标签一一对应上），最后通过迭代器 torch.utils.data.DataLoader 的调用，按照batch_size 分批次读取数据。 如下有两个例子：

【kaggle数据集 - dog breed 举例】数据预处理、重写Dataset、DataLoader读取数据
torch.utils.data.Dataset 和 torch.utils.data.DataLoader 基础使用



**方式二**



若数据结构如下图所示，则可以是用 `torchvision.datasets.ImageFolder` 生成 dataset

<img src="https://p.ipic.vip/8y666g.png" alt="数据存储结构" style="zoom:50%;" />

```python
from torchvision import datasets, transforms

my_trans = transforms.Compose([transforms.RandomResizedCrop(224),
                               transforms.ToTensor()])

train_data = datasets.ImageFolder('./animals/train', transform=my_trans)
print(train_data.class_to_idx)    # 查看分类名称(文件名) 对应的标签数值
print(train_data[0][0].size())    # 第一张图片的尺寸，就是我们 transforms.RandomResizedCrop 设定的裁剪尺寸

for i in range(len(train_data)):
    print(train_data[i][1])   # 查看训练数据集中所有图片映射到的标签值
```


输出：

<img src="https://p.ipic.vip/xrm779.png" alt="在这里插入图片描述" style="zoom:50%;" />