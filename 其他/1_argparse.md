

## **简介**

argparse 模块是 Python 标准库中提供的一个 <mark>命令行解析模块</mark> ，它可以让使用者以类似 Unix/Linux 命令参数的方式输入参数（在终端以命令行的方式指定参数），argparse 会自动将命令行指定的参数解析为 Python 变量，从而让使用者更加快捷的处理参数。



使用举例

```python
import argparse

parser = argparse.ArgumentParser(description="description")

parser.add_argument('-gf', '--girlfriend', choices=['jingjing', 'lihuan'])
parser.add_argument('food')
parser.add_argument('--house', type=int, default=0)

args = parser.parse_args()
print('args :',args)
print('girlfriend :', args.girlfriend)
print('food :', args.food)
print('house :', args.house)
```


---



## **使用步骤**

#### 1）导入argparse模块，并创建解释器 

```python
import argparse

# 创建解释器
parser = argparse.ArgumentParser(description="可写可不写，此处会在命令行参数出现错误的时候，随着错误信息打印出来。")
```

#### 2）添加所需参数 

```python
parser.add_argument('-gf', '--girlfriend', choices=['jingjing', 'lihuan'])
# --girlfriend 代表完整的参数名称，可以尽量做到让人见名知意，需要注意的是如果想通过解析后的参数取出该值，必须使用带--的名称
# -gf 代表参数名缩写，在命令行输入 -gf 和 --girlfriend 的效果是一样的，用简称的作用是简化参数输入
# choices 代表输入参数的值只能是这个choices里面的内容，其他内容则会保错

parser.add_argument('food')
# 该种方式则要求必须输入该参数； 输入该参数不需要指定参数名称，指定反而会报错，解释器会自动将输入的参数赋值给food

parser.add_argument('--house', type=int, default=0)
# type  代表输入参数的类型，从命令行输入的参数，默认是字符串类型
# default 如果不指定该参数的值，则会使用该默认值
```

#### 3）解析参数
```python
# 进行参数解析
args = parser.parse_args() 
```



完整代码

```python
import argparse

parser = argparse.ArgumentParser(description="description")

parser.add_argument('-gf', '--girlfriend', choices=['jingjing', 'lihuan'])
parser.add_argument('food')
parser.add_argument('--house', type=int, default=0)

args = parser.parse_args()
print('args :', args)
print('gf :', args.girlfriend)
print('food :', args.food)
print('house :', args.house)
```

终端运行结果：

<img src="https://p.ipic.vip/51okka.png" alt="image-20230924164226469" style="zoom: 67%;" style="left;" />



----



## **其他参数说明**

#### 1）参数：action 
向 `add_argument` 方法中传入参数 `action=‘store_true’/‘store_false’` ，解析出来就是 bool型 参数 True/False，具体规则为:
- store_true：如果未指定该参数，默认状态下其值为False；若指定该参数，将该参数置为 True
- store_false：如果未指定该参数，默认状态下其值为True；若指定该参数，将该参数置为 False

```python
import argparse

parser = argparse.ArgumentParser(description="description")

parser.add_argument('--pa', '-a', action='store_true')
parser.add_argument('--pb', '-b', action="store_false")
args = parser.parse_args() 
print(args)
```

```python
>> python test.py
Namespace(pa=False, pb=True)

>> python test.py -a -b
Namespace(pa=True, pb=False)
```



若 该参数 <mark>同时指定了 action 和 default</mark>，在未指定该参数的情况下，以 default 值为准；在指定该参数的情况下，以 action 的值为准。


```python
import argparse

parser = argparse.ArgumentParser(description="description")

parser.add_argument('--pa','-a',action='store_true')
parser.add_argument('--pb','-b',action="store_true",default=True)
parser.add_argument('--pc','-c',action="store_true",default=False)

parser.add_argument('--pd','-d',action='store_false')
parser.add_argument('--pe','-e',action="store_false",default=True)
parser.add_argument('--pf','-f',action="store_false",default=False)

args = parser.parse_args()
print(args)
```

```python
>> python test.py
Namespace(pa=False, pb=True， pc=False, pd=True, pe=True, pf=False)

>> python test.py -a -b -c -d -e -f
Namespace(pa=True, pb=True， pc=True, pd=False, pe=False, pf=False)
```

---

## **使用 pycharm 传递参数给 argparse**
 上面的操作，我们是通过 命令行 给 python 程序传递参数，一般适合于我们在 GPU 等 linux 操作系统中训练模型使用。
但是在平时我们调试算法的时候就会很不方便，没有办法利用 IDE 进行debug，所以接下来介绍如何在 Pycharm 中传递参数给 argparse，方便 pycharm 进行运行这类python程序。

1、如下图，点击 Edit configurations

<img src="https://p.ipic.vip/o594kv.png" alt="在这里插入图片描述" style="zoom:35%;" />

2、在Parameters中添加需要的参数（只写参数），多个参数之间用空格隔开

<img src="https://p.ipic.vip/s7k00n.png" alt="在这里插入图片描述" style="zoom:35%;" />

3、最后直接运行，可以看到，把我们设置在Parameters里面设置的参数，会在Run的时候自动补全



<img src="https://p.ipic.vip/g8jkzk.png" alt="在这里插入图片描述" style="zoom:35%;" />



----



## **代码实例**

以下代码来自 DDPM :  https://github.com/abarankab/DDPM/blob/main/scripts/train_cifar.py

```python
import torch
import datetime
import argparse


def diffusion_defaults():
    defaults = dict(
        num_timesteps=1000,
        schedule="linear",
        loss_type="l2",
        use_labels=False,

        base_channels=128,
        channel_mults=(1, 2, 2, 2),
        num_res_blocks=2,
        time_emb_dim=128 * 4,
        norm="gn",
        dropout=0.1,
        activation="silu",
        attention_resolutions=(1,),

        ema_decay=0.9999,
        ema_update_rate=1,
    )
    return defaults


def add_dict_to_argparser(parser, default_dict):
    for k, v in default_dict.items():
        v_type = type(v)
        if v is None:
            v_type = str
        parser.add_argument(f"--{k}", default=v, type=v_type)


def create_argparser():
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    run_name = datetime.datetime.now().strftime("ddpm-%Y-%m-%d-%H-%M")
    defaults = dict(
        learning_rate=2e-4,
        batch_size=2,
        iterations=800000,

        log_to_wandb=True,
        log_rate=1000,
        checkpoint_rate=1000,
        log_dir="~/ddpm_logs",
        project_name="Enzo_ddpm",
        run_name=run_name,

        model_checkpoint=None,
        optim_checkpoint=None,

        schedule_low=1e-4,
        schedule_high=0.02,

        device=device,
    )
    defaults.update(diffusion_defaults())
    parser = argparse.ArgumentParser()
    add_dict_to_argparser(parser, defaults)
    return parser


if __name__ == '__main__':
  	args = create_argparser().parse_args()
    print(args)
```



输出：

```python
Namespace(activation='silu', 
          attention_resolutions=(1,), 
          base_channels=128, 
          batch_size=2, 
          channel_mults=(1, 2, 2, 2), 
          checkpoint_rate=1000, 
          device=device(type='cpu'), 
          dropout=0.1, 
          ema_decay=0.9999, 
          ema_update_rate=1, 
          iterations=800000, 
          learning_rate=0.0002, 
          log_dir='~/ddpm_logs', 
          log_rate=1000, 
          log_to_wandb=True, 
          loss_type='l2', 
          model_checkpoint=None, 
          norm='gn', 
          num_res_blocks=2, 
          num_timesteps=1000, 
          optim_checkpoint=None, 
          project_name='Enzo_ddpm', 
          run_name='ddpm-2023-09-24-18-17', 
          schedule='linear', 
          schedule_high=0.02, 
          schedule_low=0.0001, 
          time_emb_dim=512, 
          use_labels=False)

```

