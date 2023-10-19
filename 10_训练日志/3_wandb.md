

## 简介

wandb 是一个用于跟踪、可视化和协作机器学习项目的工具。它可以帮助用户记录模型训练过程中的超参数和输出指标，然后可视化和比较结果，并快速与同事共享结果。

官网地址 ： https://wandb.ai/site

<img src="https://p.ipic.vip/ofw8wa.png" alt="image-20230924213456548" style="zoom:25%;" style="left;"/>



----



## 安装 wandb 

如果还没有安装，请安装 wandb

```Python
pip install wandb
```

若代码运行时，遇到如下报错

```Python
wandb.errors.UsageError: api_key not configured (no-tty). call wandb.login(key=[your_api_key])
```

需要重新设置一下wandb，在终端输入如下命令：

```Python
wandb init
```

然后你会看到如下提示，点击红色框框起来的链接

<img src="https://p.ipic.vip/j72kq7.png" alt="img" style="zoom: 50%;" style="left;" />

按照提示 sign in 或 sign up，注册并且登录之后，重新点击上方链接，会看到如下的key

<img src="https://p.ipic.vip/k45vem.png" alt="img" style="zoom:30%;" style="left;" />

点击复制，然后回到终端 control+v 粘贴， 然后回车

接下来会提示你输入一个项目名，你自己起一个项目名，然后回车

<img src="https://p.ipic.vip/3uzkjh.png" alt="img" style="zoom:50%;" style="left;" />

如果碰到如下报错

![img](https://p.ipic.vip/plaf2d.png)

将`entity='treaptofun'`注释掉

<img src="https://p.ipic.vip/cmc34w.png" alt="img" style="zoom:50%;" style="left;" />





----



## 常用函数

官方文档地址 ： https://docs.wandb.ai/ref/python

### 1）wandb.init()
这个函数的作用与平常定义类里面的init函数作用类似，都是起初始化的作用。

`wandb.init()` 中有20多个参数，这里只列出几个重要的参数，并加以解释：

  ```python
  wandb.init(project='project',
             entity='team_name',
             name='name',
             config=config,
             resume='None')
  ```

1. `project`：(str, optional)  用于指定项目名称

   wandb 在运行的过程中会自动帮你创建一个以此命名的项目文件，run 结果 都会存放在这个项目文件里。如果没有指定项目名称，run 结果 会放在一个 "Uncategorized" 未分类项目中

2. `entity` :  用于指定实验所属的团队或组织 (可以是团队或组织的名称，也可以是团队或组织的 ID)

   当指定了 entity 参数后，实验数据将存储在该团队或组织下。这样，团队成员可以通过 wandb 网站或 API 查看和分析实验数据。

3. `name`：(str, optional) 此次运行的简短名称。默认情况下，会生成一个随机的两个单词的名称，

4. `conifg`：(dict, argparse, absl.flags, str, optional)  用于设置 `wandb.config`

5. `resume`：用于设置可恢复行为，通俗的理解就是当遇见意外中断时是否可继续。通常设置为默认None。

举例：

```python
run = wandb.init(project=args.project_name,
                 entity=args.team_name,
                 config=vars(args),
                 name=args.run_name)
```



### 2）wandb.watch()

```python
watch(models,
      log = "gradients",
      log_freq = 1000)
```

1. models：要跟踪的模型

2. log：要记录的数据。可以是  "gradients", "parameters", "all", or None  中的一个

3. log_freq：记录数据的频率。



### 3）wandb.config()
`wandb.config()` 用于保存训练配置，这些配置包含超参数、数据集名称或模型类型等输入设置，以及其他自变量。

在使用的时候可以在 `wandb.init()`中就进行对 config的定义，这时候就能够直接对config内容进行输入。

如果在`wandb.init()`中没有设置conifg，那么就使用 `wandb.config.update()` 进行具体内容的输入。

```python
# wandb.init() 中定义了config
config = dic(learing rate=0.1,batch size=2,epoch=50)

# wandb.init() 中没有定义config
wandb.config.update(dic(learing rate=0.1,batch size=2,epoch=50))
```



### 3）wandb.log() 
`wandb.log()` 会将数据记录到当前的历史记录，换句话说就是每次运行到这里，系统就会将log内的参数值自动上传更新，一般数据会直接绘制成表格。

```python
wandb.log({'loss': loss, 
           'epoch': epoch, 
           'learning rate': cur_lr，
           'images': wandb.Image(images.float()),
           'masks': {'true': wandb.Image(targets.float()),
                     'pred': wandb.Image(pred.float())}
          })
```



### 4）wandb.Image()

`wandb.Image()` 用于图像的显示，numpy格式的数组或者PIL实例转化为PNG，从而在网页上直接显示出来。

```python
Image(data_or_path: "ImageDataOrPathType",
      mode: Optional[str] = None,
      caption: Optional[str] = None,
      grouping: Optional[int] = None,
      classes: Optional[Union['Classes', Sequence[dict]]] = None,
      boxes: Optional[Union[Dict[str, 'BoundingBoxes2D'], Dict[str, dict]]] = None,
      masks: Optional[Union[Dict[str, 'ImageMask'], Dict[str, dict]]] = None
     )
```


