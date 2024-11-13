# AgentProving自动证明报告
2023012238 符家祺
## 具体代码实现设计

### 项目结构
```
AgentProving
├── AgentProving.py 
├── formula.py # 数学支持
├── gpt_text.py # OpenAI API调用
├── prompt.py # 提示词
├── test_A.in # 示例输入A
└── test_B.in # 示例输入B
```

### 设计与实现

#### 基本思路
为了实现归结推理的自动证明，我首先想到的思路是：利用LLM的强大推理能力，发动LLM解决数学问题。

如何做到这一点呢？

参考人类：当人类看到一个数学题目的时候，他会一步一步地做。同时，在做这一步的时候，可能会参考之前自己采取的步骤，避免重复操作等无谓行为。

#### 状态抽象
为了模仿人类的解题思路，我进行了这样的抽象：

我们设当前的状态为$State$，$State$和当前的公式$current\_formula$以及过去的状态$history\_formulas\_and\_operations$有关。

其中的公式，具有`[element_0, element_1,..., element_k] => Target`的格式。如果是归谬，那么`Target`就是`None`，如果是有目标命题的证明，那目标就是那个命题。

于是，便可表示为：

$$当前状态 = State(current\_formula, history\_formulas\_and\_operations)$$

简记为：
$$State(c, h)$$

其中的$h$是一个有序列表，其元素格式为$(formula, operation)$的二元对，即历史的一个式子，以及在这个式子下采取的操作。

#### 操作抽象
光有状态$State$是不够的，要发挥主观能动性，还需要真正动手去做。

于是，我们对操作也进行抽象。

先考虑归结推理中会出现哪些操作呢？很显然，只会是两个命题公式进行合并。于是，我想到可以将操作表示为$opr(i, j)$，其中的$i,j$是相关的命题公式在式子里面的秩。

特别地，当当前的状态已经可以结束，操作为`STOP`。

## 测试情况


## 参考