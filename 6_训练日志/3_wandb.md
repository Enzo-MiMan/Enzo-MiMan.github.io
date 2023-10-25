







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





----



