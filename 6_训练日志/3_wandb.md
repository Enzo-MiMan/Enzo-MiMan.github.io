







## 简介

wandb 是一个用于跟踪、可视化和协作机器学习项目的工具。它可以帮助用户记录模型训练过程中的超参数和输出指标，然后可视化和比较结果，并快速与同事共享结果。

官网地址 ： https://wandb.ai/site

<img src="https://p.ipic.vip/ofw8wa.png" alt="image-20230924213456548" style="zoom:25%;" style="left;"/>



![image-20231025134249818](https://p.ipic.vip/s2yu6j.png)

----



## 安装  与 登录

### Step 1 : 安装

```Python
pip install wandb
```

### Step 2 : 注册账号并登录

在官网 https://wandb.ai/site ，注册一个账号并登录

<img src="https://p.ipic.vip/ofw8wa.png" alt="image-20230924213456548" style="zoom: 19%;" style="left;"/>



### Step 3 : 客户端登录

在你的项目的 shell 中输入 ：

```
wandb login
```

![image-20231025122004758](https://p.ipic.vip/52m8mw.png)

点击如上色框框起来的链接，会跳转到如下网页，点击复制 key

![image-20231025122317450](https://p.ipic.vip/klepaz.png)

回到 shell，control + v  并回车 

wandb 就会提示你，你的 key 已经被存到了 .netrc 的文件中，此时你就已经登录成功了

![image-20231025122835515](https://p.ipic.vip/9why7w.png)

接下来，你就可以在代码中直接调用 wandb 的 api，相关数据就会直接上传到 wandb 云端啦

<br />

---

<br />

### 运行中遇到错误

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

按照提示 sign in 或 sign up，注册并且登录之后，重新点击上方链接，会看到如下的key，复制 key

<img src="https://p.ipic.vip/k45vem.png" alt="img" style="zoom:30%;" style="left;" />

然后回到终端 control+v 粘贴， 然后回车

接下来会提示你输入一个项目名，你自己起一个项目名，然后回车

<img src="https://p.ipic.vip/3uzkjh.png" alt="img" style="zoom:50%;" style="left;" />

如果碰到如下报错

![img](https://p.ipic.vip/plaf2d.png)

检查代码中是否有 `entity`  参数，若有，将 `entity` 参数注释掉 （ `entity` 是你的用户名/团队名，如果你没有该用户/团队权限，就会报如上的错误）

<img src="https://p.ipic.vip/cmc34w.png" alt="img" style="zoom:50%;" style="left;" />



<br />

-----



<br />

## 基础使用 与 可视化

### 1、举例

官网 Tutorials : https://docs.wandb.ai/tutorials/experiments

```python
import wandb
import random
import datetime


run_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
wandb.init(
    project="wandb_demo",       # 项目名
    name=f"run-{run_name}",     # 本次 run 的名称
    config={                    # 记录需要跟踪的超参数
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    })

# 模拟训练过程，并记录相关指标 ： acc， loss
epochs = 10
offset = random.random() / 5
for epoch in range(2, epochs):
    acc = 1 - 2 ** -epoch - random.random() / epoch - offset
    loss = 2 ** -epoch + random.random() / epoch + offset

    # 记录相关指标
    wandb.log({"acc": acc, "loss": loss})

# 结束 wandb
wandb.finish()
```

- `wandb.init()`
- `wandb.log()`
- `wandb.finish()`



<br />

<br />



### 2、常用函数

官方文档地址 ： https://docs.wandb.ai/ref/python

#### 1）wandb.init()

这个函数的作用与平常定义类里面的init函数作用类似，都是起初始化的作用。

`wandb.init()` 中有20多个参数，这里只列出几个重要的，加以解释：

  ```python
wandb.init(project='project',
           entity='team_name',
           name='run_name',
           config=config)
  ```

1. `project`：用于指定项目名称

   wandb 在运行的过程中会自动帮你创建一个以此命名的项目文件，run 结果 都会存放在这个项目文件里。

   如果没有指定项目名称，run 结果 会放在一个 "Uncategorized" 未分类项目中

2. `entity` :  用户名或团队名称 (可以是团队或组织的名称，也可以是团队或组织的 ID)，你可以将本次run 的记录发送到这个指定的用户名下 或 团队下。如果没有指定 entity，则记录将被发送到 您的用户名下。

3. `name`：此次run的名称。不设置的话，默认情况下，会生成一个随机的两个单词的名称，

4. `conifg`： 用于记录训练配置、超参数。传入的数据格式为 字典



举例 ：

```python
wandb.init(
    project="wandb_demo",       # 项目名
    name=f"run-{run_name}",     # 本次 run 的名称
    config={                    # 记录需要跟踪的超参数
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    })
```



![image-20231031134602980](https://p.ipic.vip/433cyr.png)



<br />

<br />

#### 2）wandb.config()

`wandb.config()` 用于保存训练配置，这些配置包含超参数、数据集名称、模型类型 等等

- 可以在 `wandb.init() ` 中对 config 进行定义
- 之后可以使用 `wandb.config.update()`  对 config 进行追加。它将传入的键值对追加到 config 中。如果传入的键值对中包含已经存在的键，则将新值覆盖旧值。

- 如果在`wandb.init() ` 中没有设置 conifg，那么就使用 `wandb.config.update()` 进行具体内容的输入。

举例：

```python
import wandb
import datetime

run_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
wandb.init(
    project="wandb_demo",       # 项目名
    name=f"run-{run_name}",     # 本次 run 的名称
    config={                    # 记录需要跟踪的超参数
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
    })

print(wandb.config.learning_rate)   # 0.02
print(wandb.config.epochs)   # 10

wandb.config.update({"batch_size": 64})
print(wandb.config.batch_size)

# 结束 wandb
wandb.finish()
```

![image-20231031140100126](https://p.ipic.vip/cpldrv.png)



<br />

<br />



#### 3）wandb.log() 

`wandb.log()` 会将数据记录到当前的历史记录，换句话说就是每次运行到这里，系统就会将log内的参数值自动上传更新，一般数据会直接绘制成表格。

```python
wandb.log({"acc": acc, 
           "loss": loss})
```

![image-20231031140150329](https://p.ipic.vip/tzxuuv.png)



![image-20231031140222588](https://p.ipic.vip/c51k43.png)

<br />

<br />

 #### 4）wandb.finish() 

用于通知 Wandb 服务器该运行已经结束，并将所有数据上传到服务器。

<br />

<br />

----





### 3、页面层级 与 页面操作



![image-20231101203258825](https://p.ipic.vip/vzdhcy.png)









