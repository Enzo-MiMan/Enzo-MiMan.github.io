# 期望最大化 EM 

## 1）简介

EM ： Expectation Maximization，期望最大化算法

- 解决的问题 ： 用于计算 含有 隐变量（Hidden Variable）的混合模型的参数估计  （极大似然估计，或 极大后验概率估计）

- EM算法是一种迭代算法，每一次迭代由两步组成：
  1. E步（求期望）：对参数的期望值进行计算。
  2. M步（极大化）：找到一个 参数值，使得 期望函数 的值达到极大值。



> 一个场景举例：
>
> 学校有 A、B 两个班级，这两个班级的学生都参加了同一场考试，现在老师已经拿到了这两个班所有同学的考试成绩，但是试卷上没有学生的姓名和班级，老师想来猜测一下哪些成绩是属于1班的，哪些成绩是属于2班的。 
>
> &nbsp;
>
> 通常情况下，每个班级内同学的成绩都是服从正态分布的，因为这是两个班级的成绩，所以老师尝试使用 2个高斯分布来拟合，这种模型就被称为 :   <font color=Red>高斯混合模型</font>
>
> &nbsp;
>
>  <font color=Red>EM 就可以用来 找出两个正态分布 用来 近似/拟合  两个班级的成绩分布。</font> 也就是做 混合模型的参数估计，其中：
>
> - 混合模型：这里 指的就是 两个高斯分布模型的混合。
> - 参数估计：这里 指的就是计算出 这两个高斯分布的均值和方差。 参数$\theta$ 指的是 均值 和 方差的整体 ： $\theta = {\mu，\sigma}$





<img src="https://p.ipic.vip/zi5lem.jpg" width="900">



&nbsp;

----





## 2）EM 算法公式  

$$
\begin{align}
\hat \theta^{(t+1)} 
& = \mathop{\arg \max}\limits_{\theta} \int_{z}log \; p(x, z|\theta) p(z|x, \theta^{(t)}) dz \notag \\
& \; \notag \\
& = \mathop{\arg \max}\limits_{\theta} \;E_{z|x, \theta}[log \; p(x, z|\theta)] \notag \\
\end{align}
$$

&nbsp;

EM算法是一种迭代算法，每一次迭代由两步组成：

1. E步（求期望）：对参数的期望值进行计算。
2. M步（极大化）：找到一个点，使得期望值的函数达到极大值。



> <font color=Red>隐变量</font> 与 <font color=Red>参数</font> 的解释
>
> 在信用卡用户信用评分模型中，假设一个用户有很多特征（年龄，性别，收入等），但这些特征只能观察到部分，比如只观察到年龄和性别，而收入是隐含的。通过EM算法，我们可以估计出用户的收入水平，进而更准确地评估其信用风险。
>
> $信用风险 = a \times 年龄 + b \times I_{性别} + c \times 收入$
>
> - 收入就是 隐变量，文中用 $z$ 表示
>
> - 年龄，性别，收入 的权重  $a, b, c$ 就是 信用风险模型 的参数:  $\theta = \{a., b, c\}$



----

Reference ： 

1、https://www.bilibili.com/video/BV1RT411G7jJ

