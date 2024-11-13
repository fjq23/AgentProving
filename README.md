# AgentProving: 基于OpenAI API的归结推理自动证明工具
## 简介
AgentProving 是一款创新的自动证明工具，它利用了 OpenAI API 的强大能力来实现归结推理（Resolution Reasoning）的自动化。该工具专为逻辑推理和自动证明设计，可以帮助用户在逻辑学领域进行简单的逻辑证明和验证。
## 主要功能
- **归结推理实现**：通过LLM实现归结推理，用于解决逻辑命题问题。
- **OpenAI API 集成**：利用 OpenAI 的 GPT 模型处理复杂的逻辑表达式和推理任务。
- **自动证明**：自动执行逻辑证明过程，无需人工干预。
- **结果验证**：提供证明结果的验证，确保推理过程的正确性。

## 版本依赖
```commandline
httpx 0.28.0
openai 0.27.2
```

## 安装指南
1. 确保您的系统已经安装了 Python，并且版本至少为 3.8。
2. 安装所需的依赖库：
   ```sh
   pip install openai=0.27.2
   pip install httpx=0.28.0
   ```
   (请注意版本)
3. 获取 OpenAI API 密钥并设置环境变量： 
 
    在`AgentProving.py`的上部，填入您的 OpenAI API 密钥。

    ```
    import openai
    openai.api_key = "Your api key here"
    ```

## 使用说明
1. 选择证明模式：
    ```
    Choose your proving mode:
    - A. Proof by Contradiction
    - B. Goal-Oriented Proof
    Enter A or B:
    ```
   如果您希望用归谬法证明，选择`A`；如果您有证明目标，则选择`B`。
2. 输入证明目标（仅当Goal-Oriented Proof才需要）：
   ```
   You are in the 'Goal-Oriented Proof' mode. Please enter your proving target (an atomic proposition):
   ```
   证明目标应该为一个只含有取反号$\neg$（为了方便，用`-`表示）和$\vee$（为了方便，用小写字母`v`表示）的命题公式。
   例如`A`，`-PvQ`等等：

3. 输入子式列表：
   ```
    Enter your 1th element (1 out of 5):
    ```
   程序会输出一段格式为这样的提示，提示你依次输入列表中的子式。

   子式的格式要求与证明目标相同。

4. 等待AgentProving的证明：

   AgentProving会依次进行证明，每一次都会合并两个子式，并将新的子式加入子式列表。

   `CURRENT`字样后显示的是当前的式子。

   `HISTORY`字样后显示的是过去的式子以及智能体对式子分别进行的操作。

5. 证明结果的输出：

   如果证明成功（通常正确的输入会导出成功的证明）：

   程序将会输出`We got a contradiction here!`（模式： Proof by Contradiction）或者`We got {target} here!`（模式： Goal-Oriented Proof）
   
   之后，就会输出证明历史。
  

## 许可协议
AgentProving 项目遵循 MIT 许可协议，这意味着您可以自由地使用、修改和分发这个软件，但需要遵守 MIT 许可协议的相关条款。
