

b站视频 ：https://www.bilibili.com/video/BV1bM411L7Qi

----



# DataLoader 参数详解  <!-- {docsify-ignore} -->



![image-20231011203134620](https://p.ipic.vip/q5a6cd.png)

<br />

<br />

## 1、参数 pin_memory

<img src="https://p.ipic.vip/1safk1.png" alt="image-20231011204043526" style="zoom: 45%;" />



<mark>Pinned memory (锁页内存)</mark> 是指将一部分内存锁定在物理内存中，防止这部分内存被交换到磁盘上或被其他程序使用，可以提高访问速度和可靠性。避免了数据从主机内存到 GPU 显存的复制过程中的页面交换问题。这种固定在物理内存中的内存称为 Pinned memory。



<mark>Pageable memory (可分页内存)</mark>  ： 是一种将物理内存划分成固定的页面，并在需要时将页面交换到磁盘上以释放内存空间的技术。

- 其中内存被划分为固定大小的块，称为页（page）
- 在使用 Pageable memory 传输数据时，数据存储在 虚拟内存 中，然后通过页面文件的方式管理数据的加载和卸载。



<mark>虚拟内存</mark>：将计算机可用的 物理内存 和 磁盘空间 组合使用，以提供更大的可用内存空间。它使用一个虚拟地址空间来代替物理地址空间，使得每个进程都认为自己有独立的内存。当进程需要访问一个虚拟地址时，操作系统会将它映射到物理地址空间中的一个位置，这个过程称为地址转换。如果物理内存不足，操作系统会将物理内存中一些不常用的数据暂存到磁盘上。







<br />

<br />

## 2、参数 num_workers



当 num_workers 参数设置得太高时，可能会导致系统资源不足。

为避免这种情况，通常建议将 num_workers 参数设置为等于或小于 CPU 核心数，以有效平衡数据加载效率和系统资源占用率。

```python
batch_size = 16
nw = min([os.cpu_count(), batch_size if batch_size > 1 else 0, 8])   # number of workers
train_dataloader = torch.utils.data.DataLoader(train_dataset,
                                               batch_size=batch_size,
                                               num_workers=nw,
                                               shuffle=True,
                                               pin_memory=True,
                                               collate_fn=train_dataset.collate_fn)
```



<br />

<br />

## 3、参数 collate_fn

<br />

#### 例1: 分类任务

![image-20231011204944012](https://p.ipic.vip/pv9c66.png)



<br />

<br />

#### 例2: 目标检测任务



![image-20231011205431500](https://p.ipic.vip/cwwgjd.png)





<br />

<br />

<br />

<br />





